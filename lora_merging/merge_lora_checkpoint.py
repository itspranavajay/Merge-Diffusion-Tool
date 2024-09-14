from tqdm import tqdm
from helpers.tensor_utils import resize_tensor_shapes

def merge_lora_into_checkpoint(lora, checkpoint, merge_weight=0.5):
    print(f"Merging LoRA into checkpoint with weight: {merge_weight}")
    merged = {}
    all_keys = set(checkpoint.keys()).union(set(lora.keys()))

    for key in tqdm(all_keys, desc="Merging LoRA into Checkpoint", unit="layer"):
        ckpt_tensor, lora_tensor = checkpoint.get(key), lora.get(key)
        if ckpt_tensor is not None and lora_tensor is not None:
            ckpt_tensor, lora_tensor = resize_tensor_shapes(ckpt_tensor, lora_tensor)
            merged[key] = ckpt_tensor + merge_weight * lora_tensor
        elif ckpt_tensor is not None:
            merged[key] = ckpt_tensor
        else:
            merged[key] = merge_weight * lora_tensor

    return merged
