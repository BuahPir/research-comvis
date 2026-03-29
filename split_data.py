import json
import os
import shutil

# --- CONFIGURATION ---
json_file_path = "./annotations/train_val_test_distribution_file.json"
source_images_folder = "images/"  # <-- CHANGE THIS
output_dataset_folder = "data/"              # Where the new folders will be created

# 1. Load the JSON file
with open(json_file_path, 'r') as file:
    splits = json.load(file)

# 2. Iterate through "train", "val", and "test"
for split_name, image_list in splits.items():
    
    # Create the target directory (e.g., custom_dataset/train/)
    target_dir = os.path.join(output_dataset_folder, split_name)
    os.makedirs(target_dir, exist_ok=True)
    
    print(f"Moving {len(image_list)} images into '{target_dir}'...")
    
    # 3. Copy each image to its new home
    for image_name in image_list:
        source_path = os.path.join(source_images_folder, image_name)
        target_path = os.path.join(target_dir, image_name)
        
        # Check if the image actually exists before copying to prevent crashes
        if os.path.exists(source_path):
            shutil.copy(source_path, target_path)
            
            # --- LABEL HANDLING (See note below) ---
            # label_name = image_name.rsplit('.', 1)[0] + '.txt'
            # label_source = os.path.join("path/to/labels", label_name)
            # label_target = os.path.join(target_dir, label_name)
            # if os.path.exists(label_source):
            #     shutil.copy(label_source, label_target)
                
        else:
            print(f"  [Warning] Could not find {image_name} in source folder.")

print("\nDataset successfully split!")