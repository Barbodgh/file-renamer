"""
Script to rename files in a directory by replacing underscores with spaces.
Handles errors and provides clear feedback to the user.
"""

import pathlib
import os


def clear_screen() -> None:
    """Clears the terminal screen based on the operating system."""
    os.system('cls' if os.name == 'nt' else 'clear')


def rename_files(directory_path: str) -> None:
    """
    Renames files in the specified directory by replacing underscores with spaces.
    
    Args:
        directory_path (str): Path to the target directory.
    
    Handles:
        - Non-existent directories
        - Files/directories with underscores
        - Permission/OS errors
        - File existence checks
    """
    try:
        target_dir = pathlib.Path(directory_path)
        
        # Validate directory exists and is a directory
        if not target_dir.exists():
            raise FileNotFoundError(f"Directory not found: '{directory_path}'")
        if not target_dir.is_dir():
            raise NotADirectoryError(f"Path is not a directory: '{directory_path}'")

        # Get all items (files/dirs) with underscores in their names
        items_with_underscores = list(target_dir.glob("*_*"))
        
        if not items_with_underscores:
            print("No files with underscores found in the directory.")
            return

        for item_path in items_with_underscores:
            try:
                # Skip directories, only process files
                if not item_path.is_file():
                    print(f"Skipped directory: '{item_path.name}'")
                    continue

                # Generate new filename and path
                original_name = item_path.name
                new_name = original_name.replace("_", " ")
                new_file_path = item_path.with_name(new_name)
                
                # Prevent overwriting existing files
                if new_file_path.exists():
                    print(f"Conflict: '{new_name}' already exists. Skipping '{original_name}'.")
                    continue
                
                # Perform rename operation
                item_path.rename(new_file_path)
                print(f"Renamed: '{original_name}' → '{new_name}'")

            except PermissionError as e:
                print(f"Permission Error: Cannot rename '{original_name}'. Reason: {e}")
            except OSError as e:
                print(f"System Error: Failed to rename '{original_name}'. Reason: {e}")

    except (FileNotFoundError, NotADirectoryError) as e:
        print(f"Invalid Directory: {e}")
    except Exception as e:
        print(f"Unexpected Error: {str(e)}")


if __name__ == "__main__":
    # Get directory input and execute rename operation
    input_directory = input("Enter directory path: ")
    clear_screen()
    rename_files(input_directory)