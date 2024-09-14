
# Merge Diffusion Tool

Merge Diffusion Tool is an open-source project designed to merge LoRA models, checkpoints, and other diffusion models. It supports popular models like Flux AI, Stable Diffusion, and many more.

## Features
- Merge two LoRA models
- Merge a LoRA model into a checkpoint
- Merge two checkpoints
- Supports models like Flux Dev, Flux Schnell, SD1.5, SD2, SDXL, SD3

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/MergeDiffusionTool.git
   cd MergeDiffusionTool
   ```

2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

To start merging models, run the tool:

```bash
python main.py --operation merge_loras --model1 model1.safetensors --model2 model2.safetensors --output merged_model.safetensors --alpha 0.5
```

### Example Operations
- `merge_loras`: Merge two LoRA models.
- `merge_lora_checkpoint`: Merge LoRA into a checkpoint.
- `merge_checkpoints`: Merge two checkpoints.

## Join the Community

For any questions or support, join our Discord server:
[Discord Support](https://discord.gg/wtyHstGZ)

## License
This project is licensed under the MIT License.
