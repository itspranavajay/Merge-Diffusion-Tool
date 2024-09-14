from tqdm import tqdm
from helpers.tensor_utils import resize_tensor_shapes

def merge_checkpoints(ckpt1, ckpt2, blend_ratio=0.5):
    print(f"Merging checkpoints with blend ratio: {blend_ratio}")
    merged = {}
    all_keys = set(ckpt1.keys()).union(set(ckpt2.keys()))

    for key in tqdm(all_keys, desc="Merging Checkpoints", unit="layer"):
        t1, t2 = ckpt1.get(key), ckpt2.get(key)
        if t1 is not None and t2 is not None:
            t1, t2 = resize_tensor_shapes(t1, t2)
            merged[key] = blend_ratio * t1 + (1 - blend_ratio) * t2
        elif t1 is not None:
            merged[key] = t1
        else:
            merged[key] = t2

    return merged
