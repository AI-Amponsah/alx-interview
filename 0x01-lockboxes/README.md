# 0x01. Lockboxes

This project is the second of many to test readiness for technical interviews.

## File Descriptions
### Mandatory

1. [0-lockboxes.py](./0-lockboxes.py) - A method that checks if all locked boxes numbered sequentially from 0 to n - 1 contains keys to the other boxes and all boxes can be opened.
	- Prototype: def `canUnlockAll(boxes)`
	- `boxes` is a list of lists
	- A key with the same number as a box opens that box
	- You can assume all keys will be positive integers
		- There can be keys that do not have boxes
	- The first box `boxes[0]` is unlocked
	- Return `True` if all boxes can be opened, else return `False`
	
	**Execution Example**:
	```
	niyi@ubuntu:~/0x01-lockboxes$ cat main_0.py
	#!/usr/bin/python3

	canUnlockAll = __import__('0-lockboxes').canUnlockAll

	boxes = [[1], [2], [3], [4], []]
	print(canUnlockAll(boxes))

	boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
	print(canUnlockAll(boxes))

	boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
	print(canUnlockAll(boxes))

	niyi@ubuntu:~/0x01-lockboxes$
	```

	```
	niyi@ubuntu:~/0x01-lockboxes$ ./main_0.py
	True
	True
	False
	niyi@ubuntu:~/0x01-lockboxes$
	```
