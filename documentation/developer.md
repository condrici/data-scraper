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

## Syntax Characteristics
- Python is a scripting, general-purpose, cross-platform, high-level and interpreted programming language
- Getters and setters are usually avoided, use instead class properties
- For method/properties access levels use __(private), _(protected) or none for public
- Import statements are relative to the main script entrypoint unless \_\_name__ is used
- \__init__ method is the Python equivalent of the C++ constructor in an object-oriented approach
- \__init__.py file turns a set of individual files into one library and then we can use one import line instead of many
- It is a common practice to use a file called requirements.txt where to add the project requirements
- Virtual environments give you the ability to isolate your Python development projects from your system installed Python and other Python environments

## Debugging and Unit Testing
- Only test concrete classes, not abstract classes
- Use Python's internal logger to output code while running unit tests
- Method type(class_name) can show you the exact instance of a given object
- Using @patch on a non-test method might give unexpected results when unit testing
- Use Python pbd for more debugging