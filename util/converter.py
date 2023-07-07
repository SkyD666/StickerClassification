import os

from PIL import Image
import pillow_avif      # need


def to_png(dir_path: str, suffix: str = ""):
    only_files = [f for f in os.listdir(dir_path) if
                  os.path.isfile(os.path.join(dir_path, f)) and os.path.basename(f).upper().endswith(suffix.upper())]
    for file in only_files:
        im = Image.open(os.path.join(dir_path, file)).convert("RGB")
        im.save(os.path.join(dir_path, f"{os.path.splitext(file)[0]}.jpg"), "jpeg")


if __name__ == '__main__':
    to_png("H:\\StickerClassification\\stickers\\多啦A梦", suffix=".png")
