# 0x08-making_change

This project is the ninth of many to test readiness for technical interviews.

## File Descriptions
### Mandatory
1. [0-making_change.py](./0-making_change.py) - a script that given a pile of coins of different values, determines the fewest number of coins needed to meet a given amount `total`
   - Prototype: `def makeChange(coins, total)`
   - Return: fewest number of coins needed to meet `total`
	- If `total` is `0` or less, return `0`
	- If `total` cannot be met by any number of coins you have, return `-1`
	- `coins` is a list of the values of the coins in your possession
	- The value of a coin will always be an integer greater than `0`
	- You can assume you have an infinite number of each denomination of coin in the list

   **Execution Example**
   ```
   Niyi@ubuntu$ ~/0x08-making_change$ cat 0-main.py
   #!/usr/bin/python3
   """
   Main file for testing
   """

   makeChange = __import__('0-making_change').makeChange

   print(makeChange([1, 2, 25], 37))

   print(makeChange([1256, 54, 48, 16, 102], 1453))

   Niyi@ubuntu:~/0x08-making_change$
   ```
