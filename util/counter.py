import os


def counter(dir_path: str):
    classifications = os.listdir(dir_path)
    print("分类：数量")
    d = dict(
        sorted(
            {c: len(os.listdir(os.path.join(dir_path, c))) for c in classifications}.items(),
            key=lambda x: x[1],
            reverse=True,
        )
    )
    for c in d:
        print(f"{c}：{d[c]}")


if __name__ == '__main__':
    counter("../stickers")
