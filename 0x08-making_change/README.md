# 0x08. Making Change

## Description

This project contains a Python function that determines the fewest number of coins needed to meet a given amount total, given a pile of coins of different values. This is a classic dynamic programming problem that tests understanding of algorithmic efficiency and problem-solving approaches.

## Installation

Install Python 3.8:

```bash
sudo apt update
sudo apt install python3.8
```

Ensure `pycodestyle` is installed:

```bash
sudo pip3 install pycodestyle==2.8.0
```

## Usage

Run the test script:

```bash
./0-main.py
```

Example output:

```bash
7
-1
```

## Requirements

### General
- Allowed editors: vi, vim, emacs
- All files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.4.3)
- All files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should use the PEP 8 style (version 1.7.x)
- All your files must be executable

### Task
**0. Change comes from within**

Given a pile of coins of different values, determine the fewest number of coins needed to meet a given amount total.

- Prototype: `def makeChange(coins, total)`
- Return: fewest number of coins needed to meet total
  - If total is 0 or less, return 0
  - If total cannot be met by any number of coins you have, return -1
- coins is a list of the values of the coins in your possession
- The value of a coin will always be an integer greater than 0
- You can assume you have an infinite number of each denomination of coin in the list
- Your solution's runtime will be evaluated in this task

## Concepts Covered

- Dynamic programming approaches
- Greedy algorithms (though they may not always work for this problem)
- Time and space complexity considerations
- Problem decomposition
- Edge case handling
 
## Mission Director

This project is part of the ALX Software Engineering Program.

## Developer

**Codename**: Achraf Sadeq

## Acknowledgments

This repository was developed by Holberton School, in collaboration with the ALX Software Engineering Program, to provide practical, hands-on learning experiences in a professional and real-world context. It aims to equip learners with the skills and knowledge necessary to tackle complex challenges in software engineering.



