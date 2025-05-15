# 0x04. UTF-8 Validation

## Description
This project contains a Python function that determines if a given dataset represents a valid UTF-8 encoding. UTF-8 is a variable-width character encoding capable of representing all possible Unicode code points. The function checks whether a list of integers (each representing a byte) follows the UTF-8 encoding rules.

## Requirements
### General
- Allowed editors: `vi`, `vim`, `emacs`
- All files will be interpreted/compiled on Ubuntu 20.04 LTS using `python3` (version 3.4.3)
- All files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should be documented
- Your code should use the PEP 8 style (version 1.7.x)
- All your files must be executable

## Task
### 0. UTF-8 Validation
**mandatory**

Write a function that determines if a given dataset represents a valid UTF-8 encoding.

- Prototype: `def validUTF8(data)`
- Return: `True` if data is a valid UTF-8 encoding, else return `False`
- A character in UTF-8 can be 1 to 4 bytes long
- The dataset can contain multiple characters
- The data will be represented by a list of integers
- Each integer represents 1 byte of data, therefore you only need to handle the 8 least significant bits of each integer

 
## **Developer**

**Codename**: Achraf Sadeq  

## **Acknowledgments**

This project was developed for educational purposes by Holberton School, in collaboration with the ALX Software Engineering Program.
