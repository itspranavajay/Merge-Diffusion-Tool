from lora_merging.merge_two_lora import merge_lora_models
from lora_merging.merge_lora_checkpoint import merge_lora_into_checkpoint
from checkpoint_merging.merge_checkpoints import merge_checkpoints
from helpers.file_utils import load_model, save_model

def main():
    import argparse
    parser = argparse.ArgumentParser(description="Merging LoRA and Checkpoint Models")
    parser.add_argument("--operation", type=str, required=True, choices=["merge_loras", "merge_lora_checkpoint", "merge_checkpoints"], help="Choose operation")
    parser.add_argument("--model1", type=str, required=True, help="Path to the first model file")
    parser.add_argument("--model2", type=str, required=False, help="Path to the second model file")
    parser.add_argument("--output", type=str, required=True, help="Path for the output merged model")
    parser.add_argument("--alpha", type=float, default=0.5, help="Blend ratio for merging two models")
    parser.add_argument("--merge_weight", type=float, default=0.5, help="Weight for merging LoRA into a checkpoint")
    
    args = parser.parse_args()

    # Load models
    model1 = load_model(args.model1)
    model2 = load_model(args.model2) if args.model2 else None

    # Perform merging operations
    if args.operation == "merge_loras":
        if model2 is None:
            print("Error: Please provide two LoRA models for merging.")
            return
        merged_model = merge_lora_models(model1, model2, args.alpha)
    
    elif args.operation == "merge_lora_checkpoint":
        if model2 is None:
            print("Error: Please provide a checkpoint to merge the LoRA into.")
            return
        merged_model = merge_lora_into_checkpoint(model1, model2, args.merge_weight)
    
    elif args.operation == "merge_checkpoints":
        if model2 is None:
            print("Error: Please provide two checkpoints for merging.")
            return
        merged_model = merge_checkpoints(model1, model2, args.alpha)

    # Save the merged model
    save_model(merged_model, args.output)

if __name__ == "__main__":
    main()
