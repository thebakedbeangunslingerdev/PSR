import os
import shutil

def run_discard(args, base_dir):
    if not args:
        print("Error: Specify a file to discard. Usage: discard <filename>")
        return

    # Clean quotes off the filename argument
    target_file = args.strip('\'"')
    
    # Securely pin the absolute path to your root .TRASH.CAN folder
    trash_folder = os.path.join(base_dir, ".TRASH.CAN")

    # Safety checks before moving
    if not os.path.exists(target_file):
        print(f"Error: '{target_file}' not found in the current directory.")
    elif os.path.isdir(target_file):
        print(f"Error: '{target_file}' is a folder. This command is for files only.")
    else:
        try:
            # Make sure the trash directory exists
            os.makedirs(trash_folder, exist_ok=True)
            
            # Combine the trash path with just the name of the file
            dest_path = os.path.join(trash_folder, os.path.basename(target_file))
            
            # Safely move the file
            shutil.move(target_file, dest_path)
            print(f"Successfully moved '{os.path.basename(target_file)}' to .TRASH.CAN")
        except Exception as e:
            print(f"PSR Error: Could not discard file. Reason: {e}")