"""Install a transparent EU5 situation or institution icon."""

from __future__ import annotations

import argparse
from io import BytesIO
from pathlib import Path

from PIL import Image

from build_advance_icon import ROOT, normalize_image


SIZES = [128, 64, 32, 16, 8, 4, 2, 1]
GAME_ICONS = Path(
    r"C:\Program Files (x86)\Steam\steamapps\common\Europa Universalis V"
    r"\game\main_menu\gfx\interface\icons"
)


def payload(image: Image.Image) -> bytes:
    buffer = BytesIO()
    image.save(buffer, format="DDS", pixel_format="DXT5")
    data = buffer.getvalue()
    if data[84:88] != b"DXT5":
        raise ValueError("Pillow did not encode DXT5")
    return data[128:]


def clean_resampled_alpha(image: Image.Image) -> Image.Image:
    # Downsampling can revive near-transparent RGB noise from generated PNGs.
    # DXT5 then quantizes that tiny alpha into visible red/yellow edge pixels.
    alpha = image.getchannel("A").point(lambda value: 0 if value < 32 else value)
    image.putalpha(alpha)
    clean = Image.new("RGBA", image.size, (0, 0, 0, 0))
    clean.alpha_composite(image)
    return clean


def install(kind: str, name: str, source: Path, preview: Path | None, replace: bool) -> Path:
    destination = ROOT / f"main_menu/gfx/interface/icons/{kind}/{name}.dds"
    if destination.exists() and not replace:
        raise FileExistsError(destination)
    reference = GAME_ICONS / kind / "_default.dds"
    if not reference.exists():
        raise FileNotFoundError(reference)

    if source.suffix.lower() == ".dds":
        image = Image.open(source).convert("RGBA")
        image = image.resize((116, 116), Image.Resampling.LANCZOS)
        canvas = Image.new("RGBA", (128, 128), (0, 0, 0, 0))
        canvas.alpha_composite(image, (6, 6))
        image = canvas
    else:
        image = normalize_image(source)
        image = image.resize((128, 128), Image.Resampling.LANCZOS)
        image = clean_resampled_alpha(image)

    header = reference.read_bytes()[:128]
    if header[84:88] != b"DXT5":
        raise ValueError("Reference is not DXT5")
    data = header + b"".join(
        payload(image.resize((size, size), Image.Resampling.LANCZOS))
        for size in SIZES
    )
    if len(data) != 22000:
        raise ValueError(f"Unexpected DDS size: {len(data)}")

    with Image.open(BytesIO(data)) as check:
        verified = check.convert("RGBA")
        alpha = verified.getchannel("A")
        if check.size != (128, 128) or alpha.getextrema() != (0, 255):
            raise ValueError(f"DDS validation failed: {destination}")
        if any(alpha.getpixel(point) != 0 for point in [(0, 0), (127, 0), (0, 127), (127, 127)]):
            raise ValueError(f"DDS corners are not transparent: {destination}")
        if preview is not None:
            preview.parent.mkdir(parents=True, exist_ok=True)
            verified.save(preview)
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_bytes(data)
    return destination


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("kind", choices=("situations", "institutions"))
    parser.add_argument("name", help="Situation or institution identifier")
    parser.add_argument("source", type=Path, help="Generated PNG or existing DDS art")
    parser.add_argument("--preview", type=Path)
    parser.add_argument("--replace", action="store_true")
    args = parser.parse_args()
    print(install(args.kind, args.name, args.source, args.preview, args.replace))


if __name__ == "__main__":
    main()
