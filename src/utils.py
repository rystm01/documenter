import os

CODE_EXTENSIONS = {
    # General programming languages
    '.c', '.cpp', '.cxx', '.cc', '.h', '.hpp', '.hxx', '.inl', '.tcc',  # C/C++ family
    '.java', '.class', '.jar',  # Java
    '.py',  # Python
    '.rb',  # Ruby
    '.js', '.jsx', '.mjs',  # JavaScript
    '.ts', '.tsx', '.d.ts',  # TypeScript
    '.go',  # Go
    '.php',  # PHP
    '.swift',  # Swift
    '.kt', '.kts',  # Kotlin
    '.r', '.rmd',  # R
    '.lua',  # Lua
    '.pl', '.pm',  # Perl
    '.sh', '.bash', '.zsh', '.fish',  # Shell scripts
    '.html', '.htm', '.xhtml',  # HTML
    '.css',  # CSS
    '.less', '.scss', '.sass',  # CSS preprocessors
    '.json',  # JSON
    '.xml',  # XML
    '.yml', '.yaml',  # YAML
    '.sql',  # SQL
    '.vhdl', '.vhd',  # VHDL
    '.asm', '.s', '.asm32',  # Assembly languages
    '.m', '.mm',  # Objective-C and Objective-C++
    '.scala',  # Scala
    '.clj', '.cljs',  # Clojure
    '.hs',  # Haskell
    '.elm',  # Elm
    '.nim',  # Nim
    '.d',  # D programming language
    '.vala',  # Vala
    '.racket',  # Racket (Scheme-based language)
    '.f90', '.f95', '.f03', '.f08',  # Fortran
    '.objc', '.objcpp',  # Objective-C++ and Objective-C
    '.tsv',  # Tab-separated values
    '.xsd',  # XML Schema Definition
    '.csv',  # Comma-separated values
    '.csv',  # Comma-separated values
    '.cabal',  # Haskell's Cabal build system
    '.el',  # Emacs Lisp
    '.sml',  # Standard ML
    '.coffee',  # CoffeeScript
    '.pug',  # Pug (formerly Jade)
    '.twig',  # Twig
    '.handlebars',  # Handlebars
    '.rpy',  # Ren'Py (Python-based)
    '.jl',  # Julia
    '.sh',  # Shell scripts
    '.awk',  # AWK script
    '.dart',  # Dart
    '.hbs',  # Handlebars template
    '.groovy',  # Groovy
    '.v',  # Verilog (hardware description language)
    '.fs', '.fsx',  # F# (F Sharp)
    '.gdb',  # GDB (Debugger scripts)
    '.ps1',  # PowerShell script
    '.scss',  # Sass (CSS preprocessor)
    '.ts',  # TypeScript
}


def find_files(path, tabs, hidden=False, all_=True, extensions=None):
  for filename in os.listdir(path):
    f = os.path.join(path, filename)

    is_dir = os.path.isdir(f)

    if(should_print(os.path.basename(f), hidden, all_, is_dir, extensions=extensions)):
      for _ in range(tabs):
        print("  ", end="")
      if(is_dir):
        print("d: ", end="")
      else:
        print("f: ", end="")

      print(os.path.basename(f))
      if(is_dir): 
        find_files(f, tabs+1, hidden, all_, extensions=extensions)

def is_code_file(filename, extensions):
  if os.path.splitext(filename)[-1] in extensions:
    return True
  return False

def should_print(filename, hidden, all_, is_dir, extensions):
    if is_dir and hidden:
        return True
    elif is_dir:
       return filename[0] != "."
    if not hidden and filename[0] == ".":
        return False

    if not all_:
        if is_code_file(filename, extensions):
            return True
        return False
    return True
  
