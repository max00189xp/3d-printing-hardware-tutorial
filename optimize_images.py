"""Create small WebP reading images; preserve every original PNG."""
from pathlib import Path
from PIL import Image, ImageOps

root = Path(__file__).resolve().parent / 'output/handout/images'
target = root / 'web'
target.mkdir(exist_ok=True)
original_total = preview_total = 0
for source in sorted(root.glob('0*.png')):
    with Image.open(source) as original:
        preview = ImageOps.contain(original.convert('RGB'), (900, 1000))
        output = target / (source.stem + '.webp')
        preview.save(output, 'WEBP', quality=88, method=6)
    original_total += source.stat().st_size
    preview_total += output.stat().st_size
    print(f'{source.stem}: {source.stat().st_size:,} -> {output.stat().st_size:,} bytes')
print(f'Total: {original_total:,} -> {preview_total:,} bytes; saved {1-preview_total/original_total:.1%}')
