import os
import shutil

from similarity.cosine import cosine_similarity


def task(path: str, threshold: float = 0.99999):
    files = [os.path.join(path, f) for f in os.listdir(path)]
    removed = []

    for i in range(len(files)):
        if removed.__contains__(files[i]):
            continue
        if not os.path.isfile(files[i]):
            task(path=files[i], threshold=threshold)

        print(files[i])

        i_wait_to_move = False
        new_dir = os.path.join(os.path.dirname(files[i]), str(i) + ".dup")
        for j in range(i + 1, len(files)):
            if removed.__contains__(files[i]):
                break
            if removed.__contains__(files[j]) or not os.path.isfile(files[j]):
                continue
            v = cosine_similarity(files[i], files[j])
            if (v > threshold).all():
                i_wait_to_move = True
                if not os.path.exists(new_dir):
                    os.mkdir(new_dir)
                shutil.move(files[j], os.path.join(new_dir, os.path.basename(files[j])))
                removed.append(files[j])

        if i_wait_to_move:
            shutil.move(files[i], os.path.join(new_dir, os.path.basename(files[i])))
            removed.append(files[i])


if __name__ == '__main__':
    task(path="../stickers", threshold=0.9999)
