# Developer Notes

Developer notes

## PEP 8 Style Guide Observations

- 4 spaces (no tabs) per indentation level 
- 79 characters line length (to have multiple files open next to one another, useful when unit testing as well) 
- UTF-8 file encoding
- Use trailing commas only when it is expected to extend the list 
- Function and variable names should be lowercase with underscores 
- Constant names should be uppercase with underscores, usually at module level 
- Docstring comments for public modules, functions, classes and methods (not private) 
- Surround top-level function and class definitions with two blank lines 
- Imports should usually be on separate lines 
- Order of imports: Standard library, Related third party, Local application/library specific
- You should put a blank line between each group of imports
- Absolute imports are recommended, as they are usually more readable
- Wildcard imports (from \<module> import *) should be avoided
- Module level “dunders” such as __all__, __author__, should be placed after the module docstring but before any import statements
- Use either single quotes or double quotes but keep consistency in your code

## How does the Python Interpreter work?
1) Before executing code, Python interpreter reads source file and define few special variables/global variables
2) If the python interpreter is running that module (the source file) as the main program, it sets the special \__name__ variable to have a value “\__main__”
3) If this file is being imported from another module, \__name__ will be set to the module’s name. Module’s name is available as value to \__name__ global variable

## Syntax Characteristics
- Python is a scripting, general-purpose, cross-platform, high-level and interpreted programming language
- Getters and setters are usually avoided, use instead class properties
- For method/properties access levels use __(private), _(protected) or none for public
- Import statements are relative to the main script entrypoint unless \_\_name__ is used
- \__init__ method is the Python equivalent of the C++ constructor in an object-oriented approach
- \__init__.py is a special Python file that is used to indicate that the directory it is present in is a Python package
- \__init__.py can contain initialisation code for the package or it can be an empty file
- packages are a way to structure Python's module namespace by using "dotted module names"
- It is a common practice to use a file called requirements.txt where to add the project requirements
- Virtual environments give you the ability to isolate your Python development projects from your system installed Python and other Python environments
- Data types: str, int, float, complex, list, tuple, range, dict, set, frozenset, bool, bytes, bytearray, memoryview, NoneType

## Debugging and Unit Testing
- Most common testing tools and debugging: pytest, unittest, coverage.py, pbd
- Only test concrete classes, not abstract classes
- Use Python's internal logger to output code while running unit tests
- Use print statements like type(class_name) which can show the exact data type
- Using @patch on a non-test method might give unexpected results when unit testing
- Right click in swagger files in pyCharm - show context actions - sort fields alphabetically

## Legal Considerations
- Web scraping is legal as long as you scrape public information available on the internet
- Scraping personal data or intellectual property is not legal