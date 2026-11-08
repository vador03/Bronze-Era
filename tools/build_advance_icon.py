"""Install a generated transparent PNG as an EU5 advance icon DDS."""

from __future__ import annotations

import argparse
from io import BytesIO
from pathlib import Path

from PIL import Image, ImageFilter


ROOT = Path(__file__).resolve().parents[1]
ICON_DIR = ROOT / "main_menu/gfx/interface/advance"
GAME_REFERENCE = Path(
    r"C:\Program Files (x86)\Steam\steamapps\common\Europa Universalis V"
    r"\game\main_menu\gfx\interface\advance\agriculture_advance.dds"
)
SIZES = [256, 128, 64, 32, 16, 8, 4, 2, 1]


def normalize_image(source: Path) -> Image.Image:
    image = Image.open(source).convert("RGBA")
    alpha = image.getchannel("A")
    if alpha.getextrema() == (255, 255):
        raise ValueError(f"Source has no transparent pixels: {source}")

    # Remove isolated translucent fringe from image generation before resampling.
    alpha = alpha.filter(ImageFilter.MinFilter(3))
    alpha = alpha.point(lambda value: 0 if value < 12 else 255 if value > 248 else value)
    image.putalpha(alpha)
    box = alpha.point(lambda value: 255 if value >= 32 else 0).getbbox()
    if box is None:
        raise ValueError(f"Source has no visible subject: {source}")

    image = image.crop(box)
    scale = 224 / max(image.size)
    size = tuple(max(1, round(dimension * scale)) for dimension in image.size)
    image = image.resize(size, Image.Resampling.LANCZOS)
    canvas = Image.new("RGBA", (256, 256), (0, 0, 0, 0))
    canvas.alpha_composite(image, ((256 - size[0]) // 2, (256 - size[1]) // 2))
    return canvas


def dxt5_payload(image: Image.Image) -> bytes:
    buffer = BytesIO()
    image.save(buffer, format="DDS", pixel_format="DXT5")
    data = buffer.getvalue()
    if data[84:88] != b"DXT5":
        raise ValueError("Pillow did not encode DXT5")
    return data[128:]


def install(name: str, source: Path, preview: Path | None) -> Path:
    destination = ICON_DIR / f"{name}.dds"
    if destination.exists():
        raise FileExistsError(destination)
    if not GAME_REFERENCE.exists():
        raise FileNotFoundError(GAME_REFERENCE)

    image = normalize_image(source)
    reference_header = GAME_REFERENCE.read_bytes()[:128]
    if reference_header[84:88] != b"DXT5":
        raise ValueError("Game reference is not DXT5")
    data = reference_header + b"".join(
        dxt5_payload(image.resize((size, size), Image.Resampling.LANCZOS))
        for size in SIZES
    )
    if len(data) != 87536:
        raise ValueError(f"Unexpected DDS size: {len(data)}")
    ICON_DIR.mkdir(parents=True, exist_ok=True)
    destination.write_bytes(data)

    with Image.open(destination) as check:
        verified = check.convert("RGBA")
        alpha = verified.getchannel("A")
        if check.size != (256, 256) or alpha.getextrema() != (0, 255):
            raise ValueError(f"DDS validation failed: {destination}")
        if any(alpha.getpixel(point) != 0 for point in [(0, 0), (255, 0), (0, 255), (255, 255)]):
            raise ValueError(f"DDS corners are not transparent: {destination}")
        if preview is not None:
            preview.parent.mkdir(parents=True, exist_ok=True)
            verified.save(preview)
    return destination


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("name", help="Advance identifier and DDS basename")
    parser.add_argument("source", type=Path, help="Generated PNG with alpha")
    parser.add_argument("--preview", type=Path, help="Optional decoded PNG for visual review")
    args = parser.parse_args()
    print(install(args.name, args.source, args.preview))


if __name__ == "__main__":
    main()
