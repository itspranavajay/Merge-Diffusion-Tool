# Merge Diffusion Tool

**Merge Diffusion Tool** is an open-source solution developed by **EnhanceAI.art**, providing seamless ways to blend LoRA models, integrate LoRA into checkpoints, and merge Stable Diffusion checkpoints. Enhance your AI workflows with this powerful merging tool, designed to support a wide range of diffusion models like **Flux Dev**, **Flux Schnell**, **Stable Diffusion 1.5**, **SD2**, **SD3**, and **SDXL**.

Discover more advanced AI tools at [EnhanceAI.art](https://enhanceai.art).

## Features

- **Merge Two LoRA Models** with adjustable blending ratios.
- **Integrate LoRA into a Checkpoint** for enhanced model performance.
- **Merge Two Checkpoints** using custom blend ratios.
- Full support for `.safetensors` format, ensuring efficient and safe handling.

### Key Advantages:
- Streamline your AI model merging process.
- Built with flexibility to cater to diverse AI model formats.
- Completely open-source with community support via Discord.

---

## Installation

To set up the tool, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/itspranavajay/Merge-Diffusion-Tool.git
   cd merge-diffusion-tool
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Dependencies:

- **Python 3.8+**
- **PyTorch** for deep learning operations.
- **Safetensors** library for model file handling.

---

## Usage

The **Merge Diffusion Tool** provides three main operations:

1. **Merge Two LoRA Models**
2. **Merge LoRA into a Checkpoint**
3. **Merge Two Checkpoints**

### Command-Line Arguments:

| Argument         | Description                                                                 |
|------------------|-----------------------------------------------------------------------------|
| `--operation`    | Select operation: `merge_loras`, `merge_lora_checkpoint`, `merge_checkpoints`|
| `--model1`       | Path to the first model file.                                                |
| `--model2`       | Path to the second model file (optional for LoRA into checkpoint).           |
| `--output`       | Output path for the merged model.                                            |
| `--alpha`        | Blend ratio for merging models (default: 0.5).                               |
| `--merge_weight` | Weight for merging LoRA into checkpoint (default: 0.5).                      |

### Example 1: Merging Two LoRA Models

```bash
python main.py --operation merge_loras --model1 lora1.safetensors --model2 lora2.safetensors --output output_lora.safetensors --alpha 0.7
```

This command merges `lora1.safetensors` and `lora2.safetensors`, with 70% contribution from `lora1`.

### Example 2: Merging LoRA into a Checkpoint

```bash
python main.py --operation merge_lora_checkpoint --model1 lora_model.safetensors --model2 checkpoint_model.safetensors --output output_checkpoint.safetensors --merge_weight 0.6
```

In this example, the LoRA model merges into the checkpoint with 60% influence.

### Example 3: Merging Two Checkpoints

```bash
python main.py --operation merge_checkpoints --model1 checkpoint1.safetensors --model2 checkpoint2.safetensors --output output_checkpoint.safetensors --alpha 0.5
```

Merges both checkpoint models in a 50-50 blend.

---

## Supported Formats

- **`.safetensors`**: Ensures safe, optimized storage and handling of AI models.

---

## Donation EnhanceAI.art

👏 If you find this tool helpful, please consider supporting the development by checking out our pricing plans at [enhanceai.art/pricing](https://enhanceai.art/pricing). By purchasing any plan, not only will you be supporting future open-source projects like this, but you'll also unlock **many exclusive AI features** that will greatly enhance yourself AI workflows!

---

## Support

For assistance, join our [Discord server](https://discord.gg/wtyHstGZ) to connect with the community and developers.

---

## Contributing

We welcome contributions! Feel free to open issues, submit pull requests, or suggest features that would improve this tool. All contributions are highly appreciated.
