import os

def run_scribe():
    filename = input("Enter filename to create/edit: ").strip('\'"')
    if not filename:
        print("Error: Filename cannot be empty.")
        return

    print("--- PSR Scribe ---")
    print("Type your text below. Type 'SAVE' on a blank line to save.")
    print("Type 'ABORT' on a blank line to exit without saving.")
    print("------------------")

    lines = []
    while True:
        try:
            line = input()
            if line == "SAVE":
                break
            elif line == "ABORT":
                print("Editing aborted.")
                return
            lines.append(line)
        except (KeyboardInterrupt, EOFError):
            print("\nEditing aborted.")
            return

    try:
        # Resolve the static path to the central Vault directory
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        vault_folder = os.path.join(base_dir, "Vault")
        os.makedirs(vault_folder, exist_ok=True)
        
        # Enforce the file save path into the Vault
        vault_path = os.path.join(vault_folder, os.path.basename(filename))

        with open(vault_path, "w", encoding="utf-8") as f:
            f.write("\n".join(lines))
        print(f"File saved successfully to Vault as '{os.path.basename(filename)}'.")
    except Exception as e:
        print(f"Error saving file to Vault: {e}")