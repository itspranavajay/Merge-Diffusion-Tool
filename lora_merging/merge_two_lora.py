from tqdm import tqdm
from helpers.tensor_utils import resize_tensor_shapes

def merge_lora_models(lora1, lora2, blend_ratio=0.5):
    print(f"Merging LoRA models with blend ratio: {blend_ratio}")
    merged = {}
    all_keys = set(lora1.keys()).union(set(lora2.keys()))

    for key in tqdm(all_keys, desc="Merging LoRA", unit="layer"):
        t1, t2 = lora1.get(key), lora2.get(key)
        if t1 is not None and t2 is not None:
            t1, t2 = resize_tensor_shapes(t1, t2)
            merged[key] = blend_ratio * t1 + (1 - blend_ratio) * t2
        elif t1 is not None:
            merged[key] = t1
        else:
            merged[key] = t2

    return merged
