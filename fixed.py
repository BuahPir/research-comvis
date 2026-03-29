import json

# Replace with the name of your broken JSON file
input_file = "./data/test/test_annotations.json"  
output_file = "./data/test/_annotations.coco.json"

print(f"Reading and cleaning {input_file}...")

try:
    # 1. Read the raw text
    with open(input_file, 'r', encoding='utf-8') as f:
        raw_text = f.read()

    # 2. Replace illegal non-breaking spaces (\xa0) with standard spaces
    cleaned_text = raw_text.replace('\xa0', ' ')

    # 3. Parse the cleaned text into a Python dictionary
    data = json.loads(cleaned_text)

    # 4. Save it back out with perfect standard formatting
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)

    print(f"Success! Your valid JSON has been saved to {output_file}")

except json.JSONDecodeError as e:
    print(f"Could not fix the JSON. Still encountering an error at: {e}")
except FileNotFoundError:
    print(f"Could not find the file named {input_file}. Check your spelling!")