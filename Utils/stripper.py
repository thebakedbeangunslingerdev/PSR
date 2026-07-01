import os

def run_stripper():
    user_input = input("Give in your characters that you would like removed: ")
    targets = [c.strip().strip('"').strip("'") for c in user_input.split(",")]
    if not user_input.strip():
        targets = []
    
    file_path = input("Specify the name/path: ").strip('\'"')
    
    if not os.path.exists(file_path):
        print(f"Error: File '{file_path}' not found.")
        return

    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    cleaned_content = content
    for char in targets:
        if char: 
            cleaned_content = cleaned_content.replace(char, "")

    print("Output:", cleaned_content)