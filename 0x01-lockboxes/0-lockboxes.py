#!/usr/bin/python3

"""Lockboxe problem"""


def canUnlockAll(boxes):
    """determines if all the boxes can be opened"""

    # len(boxes) # initialize all box as unlocked
    unlocked = [False] * len(boxes)
    unlocked[0] = True  # first box is always unlocked
    locked_index = []  # track of all index of boxes with no known keys yet
    keys = set(boxes[0][:])  # get already known keys from box[0]

    for index, box in enumerate(boxes[1:]):
        if (index + 1) in keys:
            unlocked[index + 1] = True
            keys.update(box)

            if locked_index and locked_index[0] in keys:
                unlocked[locked_index[0]] = True
                keys.update(boxes[locked_index[0]])
                locked_index.pop()
        else:
            locked_index.append(index + 1)

    return all(unlocked)
