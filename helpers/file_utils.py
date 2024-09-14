from safetensors.torch import load_file, save_file

def load_model(file_path):
    return load_file(file_path)

def save_model(merged_model, output_file):
    print(f"Saving merged model to {output_file}")
    save_file(merged_model, output_file) 
