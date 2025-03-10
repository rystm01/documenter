# .\src\utils.py

This utility module provides functionality for file system operations and code file identification.

## Constants

### `CODE_EXTENSIONS`
A set containing file extensions for various programming languages and development-related files. Includes extensions for:
- C/C++ family
- Java
- Python
- Web technologies (JavaScript, HTML, CSS)
- Shell scripts
- Various other programming languages and file formats

## Functions

### `find_files(path, tabs, hidden=False, all_=True, extensions=None)`
Recursively lists files and directories in a given path with hierarchical formatting.

Parameters:
- `path`: String path to search
- `tabs`: Integer number of tabs for indentation
- `hidden`: Boolean to include hidden files (Default: False)
- `all_`: Boolean to show all files vs only code files (Default: True)
- `extensions`: Set of file extensions to filter by (Default: None)

### `is_code_file(filename, extensions)`
Determines if a file is a code file based on its extension.

Parameters:
- `filename`: String name of the file to check
- `extensions`: Set of valid code file extensions

Returns:
- Boolean indicating if the file is a code file

### `should_print(filename, hidden, all_, is_dir, extensions)`
Determines if a file or directory should be included in the output.

Parameters:
- `filename`: String name of the file to check
- `hidden`: Boolean to include hidden files
- `all_`: Boolean to show all files vs only code files
- `is_dir`: Boolean indicating if the item is a directory
- `extensions`: Set of file extensions to filter by

Returns:
- Boolean indicating if the file should be printed
