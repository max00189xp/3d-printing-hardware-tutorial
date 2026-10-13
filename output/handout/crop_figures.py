from pathlib import Path
from PIL import Image

root = Path(__file__).parent
im = Image.open(root / 'images/source-page.png')
w, h = im.size
# Coordinates normalized to the visually inspected full-page reference.
regions = {
    '01-machine': (0.04, 0.10, 0.48, 0.415),
    '02-extrusion': (0.04, 0.417, 0.48, 0.632),
    '03-workflow': (0.04, 0.632, 0.458, 0.760),
    '04-motion': (0.04, 0.765, 0.440, 0.985),
    '05-components': (0.478, 0.135, 0.925, 0.455),
    '06-coordinates': (0.478, 0.459, 0.925, 0.620),
    '07-materials': (0.478, 0.622, 0.925, 0.805),
    '08-troubleshooting': (0.450, 0.805, 0.928, 0.911),
}
for name, box in regions.items():
    crop = im.crop(tuple(round(v * (w if i % 2 == 0 else h)) for i, v in enumerate(box)))
    crop.save(root / 'images' / (name + '.png'))
print('Created', len(regions), 'figures')
