import os
import sys

utils_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Utils")
if utils_path not in sys.path:
    sys.path.append(utils_path)
#import the utils!
from stripper import run_stripper
from scribe import run_scribe
from scribel import run_scribel
from viewfile import run_view
from discarder import run_discard

#Main Shell Func
def main_shell():
    print("===============================================================")
    print("Welcome to PSR! Written by McafeeHater!")
    print("Python Shells are Resurrected. Type 'exit' to close your session.")
    print("===============================================================\n")
    #Trash Folder
    trash_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".TRASH.CAN")
    
    while True:
        try:
            current_dir = os.getcwd()
            command_input = input(f"PSR // {current_dir} >>>>> ").strip()
            #Commands
            if not command_input:
                continue
                
            parts = command_input.split(maxsplit=1)
            command = parts[0].lower()
            args = parts[1] if len(parts) > 1 else ""
            
            if command == "exit":
                print("\nGoodbye! Hope you enjoyed your session!")
                sys.exit()
                
            elif command == "locate":
                print(os.getcwd())
                
            elif command == "peek":
                files = os.listdir(".")
                for item in files:
                    if os.path.isdir(item):
                        print(f"[DIR] {item}")
                    else:
                        print(f"[FILE] {item}")
                        
            elif command == "shift":
                if not args:
                    print("Error: Where do you want to shift to? Provide a path.")
                else:
                    target_dir = args.strip('\'"')
                    try:
                        os.chdir(target_dir)
                    except FileNotFoundError:
                        print(f"Error: Destination '{target_dir}' does not exist.")
                    except NotADirectoryError:
                        print(f"Error: '{target_dir}' is a file, not a folder.")
                    except PermissionError:
                        print(f"Error: Access denied to '{target_dir}'.")

            elif command == "discard":
                run_discard(args, os.path.dirname(os.path.abspath(__file__)))

            elif command == "cleanse":
                run_stripper()

            elif command == "scribe":
                run_scribe()
                
            elif command == "scribel":
                run_scribel()

            elif command == "view":
                run_view()
                
            elif command == "help":
                print("\n--- PSR COMMAND MENU ---")
                print("locate   -> View your current folder path")
                print("peek     -> See what files are inside this folder")
                print("view     -> Read and view a file's contents directly")
                print("shift    -> Move to a different directory")
                print("cleanse  -> Strip target characters out of a file")
                print("scribe   -> Create and edit text files")
                print("scribel  -> Launch a minimal GUI canvas drawing tool")
                print("help     -> Show this menu")
                print("exit     -> Close PSR\n")
                #Help Menu
            else:
                print(f"PSR Error: '{command}' is not a recognized PSR function.")
                #Exit
        except (KeyboardInterrupt, EOFError):
            print("\nGoodbye! Hope you enjoyed your session!")
            sys.exit()

if __name__ == "__main__":
    main_shell()
