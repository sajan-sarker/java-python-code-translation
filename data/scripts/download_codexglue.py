import os
from datasets import load_dataset

def download_codexglue(output_dir):
    os.makedirs(output_dir, exist_ok=True)  # create output directory  
    
    # load CodeXGLUE code-to-text python and java datasets
    java = load_dataset("google/code_x_glue_ct_code_to_text", "java")
    python = load_dataset("google/code_x_glue_ct_code_to_text", "python")
    
    # save to disk
    java.save_to_disk(os.path.join(output_dir, 'codexglue_java'))
    python.save_to_disk(os.path.join(output_dir, 'codexglue_python'))
    print(f"Dataset save to {output_dir}")

if __name__ == "__main__":
    output_dir = "./data/raw"
    download_codexglue(output_dir)
