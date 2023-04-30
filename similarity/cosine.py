from typing import Union

import numpy as np
from PIL import Image
from numpy import linalg, dot, ndarray

vector_cache = {}
norm_cache = {}


def image_similarity_vectors_via_numpy(images: list, paths: list) -> ndarray:
    vectors = []
    norms = []
    for i in range(len(images)):
        arr = np.array(images[i].getdata())
        vector = np.mean(arr, axis=1)
        vectors.append(vector)
        vector_cache[paths[i]] = vector
        norm = linalg.norm(vector, 2)
        norms.append(norm)
        norm_cache[paths[i]] = norm
    a, b = vectors
    a_norm, b_norm = norms
    return dot(a / a_norm, b / b_norm)


def image_similarity_vectors_via_numpy_cached(images: list) -> ndarray:
    a, b = vector_cache[images[0]], vector_cache[images[1]]
    a_norm, b_norm = norm_cache[images[0]], norm_cache[images[1]]
    return dot(a / a_norm, b / b_norm)


def cosine_similarity(image_1_path: str, image_2_path: str, size=(200, 200)) -> Union[ndarray, ndarray]:
    if len(vector_cache) > 5000 or len(norm_cache) > 5000:
        vector_cache.clear()
        norm_cache.clear()

    if vector_cache.__contains__(image_1_path) and norm_cache.__contains__(image_1_path) and \
            vector_cache.__contains__(image_2_path) and norm_cache.__contains__(image_2_path):
        return image_similarity_vectors_via_numpy_cached([image_1_path, image_2_path])
    else:
        image_1 = Image.open(image_1_path).resize(size).convert("RGBA")
        image_2 = Image.open(image_2_path).resize(size).convert("RGBA")
        return image_similarity_vectors_via_numpy([image_1, image_2], [image_1_path, image_2_path])
