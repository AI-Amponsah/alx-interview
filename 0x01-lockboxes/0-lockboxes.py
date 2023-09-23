#!/usr/bin/python3
""" This Module contains a function `canUnlockAll` """


def canUnlockAll(boxes):
    """Determines if all the boxes can be opened"""

    if type(boxes) != list:
        return False

    boxesLength = len(boxes)
    boxestoOpen = [0]
    openedBoxes = set()

    while boxestoOpen:
        boxIndex = boxestoOpen.pop()
        openedBoxes.add(boxIndex)

        if type(boxes[boxIndex]) != list:
            return False

        for key in boxes[boxIndex]:
            if (key < boxesLength) and (key not in boxestoOpen) and\
                    (key not in openedBoxes):
                boxestoOpen.append(key)

    return len(openedBoxes) == len(boxes)
