import torch
import torch.nn.functional as F

def resize_tensor_shapes(tensor1, tensor2):
    if tensor1.size() == tensor2.size():
        return tensor1, tensor2

    max_shape = [max(s1, s2) for s1, s2 in zip(tensor1.shape, tensor2.shape)]
    tensor1_resized = F.pad(tensor1, (0, max_shape[-1] - tensor1.size(-1)))
    tensor2_resized = F.pad(tensor2, (0, max_shape[-1] - tensor2.size(-1)))

    return tensor1_resized, tensor2_resized
