import json
import os

# --- CONFIGURATION ---
coco_annotations_path = "./annotations/annotations.json"
splits_file_path = "./annotations/train_val_test_distribution_file.json"
output_dir = "data/"  # Where the new JSON files will be saved

# 1. Load the original data
print("Loading original COCO annotations...")
with open(coco_annotations_path, 'r') as f:
    coco_data = json.load(f)

with open(splits_file_path, 'r') as f:
    splits = json.load(f)

os.makedirs(output_dir, exist_ok=True)

# 2. Extract the static parts (these stay exactly the same for all splits)
base_data = {
    "info": coco_data.get("info", {}),
    "licenses": coco_data.get("licenses", []),
    "categories": coco_data.get("categories", [])
}

# 3. Create helper maps for blazing fast lookups
# Maps filename -> full image dictionary
image_map = {img['file_name']: img for img in coco_data.get('images', [])}

# Groups all annotations by their specific image_id
anno_map = {}
for ann in coco_data.get('annotations', []):
    img_id = ann['image_id']
    if img_id not in anno_map:
        anno_map[img_id] = []
    anno_map[img_id].append(ann)

# 4. Process each split
for split_name, filenames in splits.items():
    print(f"\nProcessing '{split_name}' split...")
    
    split_images = []
    split_annotations = []
    
    for filename in filenames:
        if filename in image_map:
            # Grab the image data
            img_dict = image_map[filename]
            split_images.append(img_dict)
            
            # Grab all annotations linked to this image's ID
            img_id = img_dict['id']
            if img_id in anno_map:
                split_annotations.extend(anno_map[img_id])
        else:
            print(f"  [Warning] Image '{filename}' found in distribution file but NOT in annotations.json.")
    
    # Construct the final COCO dictionary for this split
    split_coco_data = base_data.copy()
    split_coco_data["images"] = split_images
    split_coco_data["annotations"] = split_annotations
    
    # Save the new file
    output_filename = os.path.join(output_dir, f"{split_name}_annotations.json")
    with open(output_filename, 'w') as f:
        # We don't use indent=4 here to save file size, but you can add it if you want it readable
        json.dump(split_coco_data, f) 
        
    print(f"  Saved {len(split_images)} images and {len(split_annotations)} annotations to '{output_filename}'")

print("\nAll COCO annotations successfully split!")