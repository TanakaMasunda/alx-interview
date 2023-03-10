#!/usr/bin/python3
"""Module to check locked boxes can be opened sequencially"""


def canUnlockAll(boxes):
    """method to open the boxes"""

    unlocked = [0]
    for box_id, box in enumerate(boxes):
        if not box:
            continue
        for key in box:
            if key < len(boxes) and key not in unlocked and key != box_id:
                unlocked.append(key)
    if len(unlocked) == len(boxes):
        return True
    return False
