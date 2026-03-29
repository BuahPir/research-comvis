import os
from rfdetr import RFDETRMedium, RFDETRSmall

# 1. The 'r' here is the magic fix! It forces Python to read the exact path.
DATASET_DIR = r"./data"


if __name__ == '__main__':
    # 2. A safety check to ensure the path is working before the heavy model loads
    train_json = os.path.join(DATASET_DIR, "train", "_annotations.coco.json")
    if not os.path.exists(train_json):
        print(f"❌ ERROR: Python still can't find {train_json}")
        exit()

    print("✅ Dataset verified! Initializing model...")

    # 3. Initialize and train
    model = RFDETRSmall()

    model.train(
        dataset_dir=DATASET_DIR, 
        epochs=50,                  # How many times it loops through your data
        batch_size=2,               # Images processed at once (lower this if your GPU runs out of memory)
        grad_accum_steps=4,         # Helps simulate a larger batch size
        lr=1e-4,                    # The learning rate
        output_dir="runs/training",  # Where your final weights will be saved
        early_stopping=True,
        early_stopping_patience=15,
        early_stopping_min_delta=0.005,
    )