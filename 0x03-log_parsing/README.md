 # 0x03-log_parsing

## Description
This project contains a Python script that reads stdin line by line, parses log data, and computes metrics including total file size and status code statistics. The script prints statistics after every 10 lines and/or when interrupted by CTRL+C.

## Requirements
### General
- Allowed editors: vi, vim, emacs
- All files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.4.3)
- All files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should be documented
- Your code should use the PEP 8 style (version 1.7.x)
- All your files must be executable

## Task
### 0. Log parsing
**mandatory**

Write a script that reads stdin line by line and computes metrics:

- Input format: `<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>`
  (if the format is not this one, the line must be skipped)
- After every 10 lines and/or a keyboard interruption (CTRL + C), print these statistics:
  - Total file size: `File size: <total size>`
    where `<total size>` is the sum of all previous `<file size>`
  - Number of lines by status code:
    - possible status codes: 200, 301, 400, 401, 403, 404, 405 and 500
    - if a status code doesn't appear or is not an integer, don't print anything for it
    - format: `<status code>: <number>`
    - status codes should be printed in ascending order

**Example:**
```bash
$ ./0-generator.py | ./0-stats.py
File size: 5213
200: 2
401: 1
403: 2
404: 1
405: 1
500: 3
File size: 11320
200: 3
301: 2
400: 1
401: 2
403: 3
404: 4
405: 2
500: 3
File size: 16305
200: 3
301: 3
400: 4
401: 2
403: 5
404: 5
405: 4
500: 4
^CFile size: 17146
200: 4
301: 3
400: 4
401: 2
403: 6
404: 6
405: 4
500: 4
```
## **Developer**

**Codename**: Achraf Sadeq  

## **Acknowledgments**

This project was developed for educational purposes by Holberton School, in collaboration with the ALX Software Engineering Program.

