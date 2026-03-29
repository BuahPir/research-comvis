import os

train_json = "./data/train/_annotations.coco.json"
valid_json = "./data/val/_annotations.coco.json"

print("--- DIAGNOSTIC CHECK ---")
print(f"Checking Train JSON: {train_json}")
print(f"Exists? -> {os.path.exists(train_json)}")

print(f"\nChecking Valid JSON: {valid_json}")
print(f"Exists? -> {os.path.exists(valid_json)}")