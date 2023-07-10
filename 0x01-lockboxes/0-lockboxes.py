#!/usr/bin/python3
'''Given n number of locked boxes (except the first one, which is unlocked),
    where each box is numbered sequentially from 0 to (n - 1) and may only
    contain keys to other boxes, write a function that determines if all the
    boxes can be opened.

    A key with the same number as a box opens the box
    Assume all keys are positive integers
    Some keys may not have boxes
    The first box `boxes[0]` is already open
'''


def canUnlockAll(boxes):
    '''Args: boxes is a list of lists, where each list represents a box
       Return: True if all boxes can be opened, False otherwise
    '''
    open_boxes = [0]  # the first box is always open

    for box_id, box in enumerate(boxes):
        if not box:
            continue
        for key in box:
            # a key that can open a box must be between 0 and `len(boxes)`
            # Do not repeat a key, since the box has already been opened
            # A key cannot open itself, i.e. key != box_id
            if key < len(boxes) and (key not in open_boxes) and key != box_id:
                open_boxes.append(key)

    # all boxes are open if len(open_boxes) is equal to len(boxes)
    if len(open_boxes) == len(boxes):
        return True
    return False
