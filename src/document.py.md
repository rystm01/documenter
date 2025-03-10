# .\src\document.py

This file contains the `Documenter` class which handles generating documentation for code files using the Anthropic Claude API.

## Overview
The `Documenter` class provides functionality to:
- Read code files
- Generate markdown documentation using Claude
- Write documentation to markdown files
- Process files recursively through directories

## Dependencies
- `anthropic`: For accessing the Claude API
- `os`: For file system operations
- `re`: For regular expressions (though not actively used in code)
- `src.utils`: Custom utility functions for file filtering

## Class: Documenter

### Constructor Parameters
- `path`: Base path to process files from
- `api_key`: Optional Anthropic API key
- `filewise`: Boolean controlling if documentation is written per-file or combined

### Key Attributes
- `markdown`: Stores generated markdown content
- `num`: Counter for processed files
- `files`: Set tracking processed filenames
- `api_key`: Boolean indicating if API key was provided

### Methods

#### `_read_file(filename)`
Reads and returns the contents of a file.

#### `_document_file(filename)`
Generates markdown documentation for a single file using Claude:
- Reads file content
- Sends content to Claude API
- Writes response to markdown file

#### `document(path, tabs, hidden=False, all_=True, extensions=None)`
Recursively processes files in directories:
- Handles both files and subdirectories
- Applies filtering based on parameters
- Calls `_document_file()` for each valid file

#### `write_md(md, filename)`
Writes generated markdown to file:
- Supports single or per-file documentation
- Appends to existing files
- Tracks processed files

### Cleanup
The destructor removes the API key from environment variables if it was set during initialization.
