# Merge Diffusion Tool

**Merge Diffusion Tool** is an open-source tool designed to merge LoRA models, integrate LoRA models into checkpoints, and merge two checkpoints. It supports Flux Dev, Flux Schnell, Stable Diffusion 1.5, SD2, SD3, and SDXL models.

## Features

- **Merge two LoRA models** with custom blend ratios.
- **Merge LoRA into a checkpoint** model with specified weight.
- **Merge two checkpoints** with a custom blend ratio.
- Supports `.safetensors` format for efficient and safe storage of models.

## Installation

To install the required dependencies, simply run:

```bash
pip install -r requirements.txt
```

## Requirements

- Python 3.8+
- PyTorch
- Safetensors library

## Usage

The `Merge Diffusion Tool` can handle three types of merging operations:

1. **Merge Two LoRA Models**
2. **Merge LoRA into a Checkpoint**
3. **Merge Two Checkpoints**

### Command-Line Arguments

| Argument           | Description                                                                                  |
|--------------------|----------------------------------------------------------------------------------------------|
| `--operation`      | The operation to perform. Options: `merge_loras`, `merge_lora_checkpoint`, `merge_checkpoints`. |
| `--model1`         | Path to the first model file.                                                                 |
| `--model2`         | Path to the second model file (optional for LoRA into checkpoint).                            |
| `--output`         | Path where the merged model will be saved.                                                    |
| `--alpha`          | Blend ratio for merging two models (default is 0.5).                                          |
| `--merge_weight`   | Weight for merging LoRA into a checkpoint (default is 0.5).                                   |

### Example 1: Merging Two LoRA Models

To merge two LoRA models:

```bash
python main.py --operation merge_loras --model1 lora1.safetensors --model2 lora2.safetensors --output output_lora.safetensors --alpha 0.7
```

In this case, the LoRA models will be merged with a blend ratio of 70% from `lora1.safetensors` and 30% from `lora2.safetensors`.

### Example 2: Merging LoRA into a Checkpoint

To merge a LoRA model into a checkpoint:

```bash
python main.py --operation merge_lora_checkpoint --model1 lora_model.safetensors --model2 checkpoint_model.safetensors --output output_checkpoint.safetensors --merge_weight 0.6
```

In this case, the LoRA model will be merged into the checkpoint with 60% influence from the LoRA model.

### Example 3: Merging Two Checkpoints

To merge two checkpoint models:

```bash
python main.py --operation merge_checkpoints --model1 checkpoint1.safetensors --model2 checkpoint2.safetensors --output output_checkpoint.safetensors --alpha 0.5
```

Here, both checkpoint models will be merged with a 50-50 blend ratio.

## Supported Formats

- `.safetensors`: This format is used for loading and saving all models to ensure safe handling and efficient merging operations.

## Support

For further support, please join our [Discord server](https://discord.gg/wtyHstGZ).

## Contributing

Contributions are welcome! Please open an issue or a pull request for bug fixes, improvements, or new features.

