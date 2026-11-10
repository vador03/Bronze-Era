"""Install a generated image or reused advance art as an EU5 building icon."""

from __future__ import annotations

import argparse
from io import BytesIO
from pathlib import Path

from PIL import Image

from build_advance_icon import ROOT, normalize_image


ICON_DIR = ROOT / "main_menu/gfx/interface/icons/buildings"
REFERENCE = ICON_DIR / "palace_economy_building.dds"
SIZES = [125, 62, 31, 15, 7, 3, 1]


def payload(image: Image.Image) -> bytes:
    buffer = BytesIO()
    image.save(buffer, format="DDS", pixel_format="DXT5")
    data = buffer.getvalue()
    if data[84:88] != b"DXT5":
        raise ValueError("Pillow did not encode DXT5")
    return data[128:]


def install(name: str, source: Path, preview: Path | None, replace: bool = False) -> Path:
    destination = ICON_DIR / f"{name}.dds"
    if destination.exists() and not replace:
        raise FileExistsError(destination)
    if not REFERENCE.exists():
        raise FileNotFoundError(REFERENCE)

    if source.suffix.lower() == ".dds":
        image = Image.open(source).convert("RGBA")
    else:
        image = normalize_image(source)
    image = image.resize((125, 125), Image.Resampling.LANCZOS)

    header = REFERENCE.read_bytes()[:128]
    if header[84:88] != b"DXT5":
        raise ValueError("Building reference is not DXT5")
    data = header + b"".join(
        payload(image.resize((size, size), Image.Resampling.LANCZOS))
        for size in SIZES
    )
    if len(data) != 21984:
        raise ValueError(f"Unexpected DDS size: {len(data)}")
    with Image.open(BytesIO(data)) as check:
        verified = check.convert("RGBA")
        alpha = verified.getchannel("A")
        if check.size != (125, 125) or alpha.getextrema() != (0, 255):
            raise ValueError(f"Building DDS validation failed: {destination}")
        if any(alpha.getpixel(point) != 0 for point in [(0, 0), (124, 0), (0, 124), (124, 124)]):
            raise ValueError(f"Building DDS corners are not transparent: {destination}")
        if preview is not None:
            preview.parent.mkdir(parents=True, exist_ok=True)
            verified.save(preview)
    destination.write_bytes(data)
    return destination


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("name", help="Building identifier and DDS basename")
    parser.add_argument("source", type=Path, help="Generated PNG or advance icon DDS")
    parser.add_argument("--preview", type=Path, help="Optional decoded PNG for visual review")
    parser.add_argument("--replace", action="store_true", help="Replace an icon created in this run")
    args = parser.parse_args()
    print(install(args.name, args.source, args.preview, args.replace))


if __name__ == "__main__":
    main()
