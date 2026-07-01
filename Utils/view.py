import os

def run_view():
    file_path = input("Enter the file name or path to view: ").strip('\'"')
    
    if not os.path.exists(file_path):
        print(f"Error: File '{file_path}' not found.")
        return
        
    if os.path.isdir(file_path):
        print(f"Error: '{file_path}' is a directory. Use 'peek'.")
        return

    try:
        print("\n--- File Contents ---")
        with open(file_path, "r", encoding="utf-8") as f:
            print(f.read())
        print("---------------------\n")
    except Exception as e:
        print(f"Error reading file: {e}")