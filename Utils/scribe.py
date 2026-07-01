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
        with open(filename, "w", encoding="utf-8") as f:
            f.write("\n".join(lines))
        print(f"File '{filename}' saved successfully.")
    except Exception as e:
        print(f"Error saving file: {e}")