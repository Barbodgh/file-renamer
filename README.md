# Rename Files Script

This Python script renames files in a directory by replacing underscores (`_`) with spaces (` `). It handles errors gracefully and provides clear feedback to the user.

## Features  
- Validates if the provided path exists and is a directory.  
- Renames files with underscores in their names.  
- Skips directories and provides feedback.  
- Ensures no file is overwritten by checking for name conflicts.  
- Handles errors like invalid paths, permission issues, and OS errors.  

## Why This Program?
If you're someone who downloads movies, music, or other files from torrents, you've probably noticed that many of these files come with underscores (_) in their names. While this might be fine for some, it can look messy and unorganized.

If you're a neat and organized person who prefers clean filenames, this program is for you! Instead of manually renaming files one by one, you can use this script to rename all files in a directory in bulk. It replaces underscores with spaces in a matter of seconds, saving you time and effort while keeping your files tidy and readable.

## Requirements  
- Python 3.6 or higher.  

## Usage  
1. Clone the repository:  
   ```bash
   git clone https://github.com/Barbodgh/file-renamer.git  
   cd file-renamer
2. Run the script:
   ```bash
   python file-renamer.py
3. Enter the directory path when prompted.

## License
This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

## Contribution
Feel free to fork this repository and submit pull requests for improvements or new features!
