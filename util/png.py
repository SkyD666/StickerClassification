import os
import subprocess


def png_iccp(png_dir: str):
    files = [os.path.join(png_dir, f) for f in os.listdir(png_dir)]

    for i in range(len(files)):
        if not os.path.isfile(files[i]):
            png_iccp(png_dir=files[i])
            continue

        if files[i].upper().endswith(".PNG"):
            subprocess.call(f"pngcrush -ow -rem allb -reduce \"{os.path.abspath(files[i])}\"", shell=True)


if __name__ == '__main__':
    png_iccp("..\\stickers\\多啦A梦\\新建文件夹")
