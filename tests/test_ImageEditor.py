from os import path, remove
import sys
sys.path.append('../src')
import src.ImageEditor

def test_redactImage():
    if path.exists("./redactedSSN.png"):
        remove("./redactedSSN.png")
    boxes = [{"top": 0.46082363, "left": 0.43226418, "bottom": 0.49924071, "right": 0.5754035}]
    src.ImageEditor.redactImage(boxes, "./tests/testSSN.jpg", "./redactedSSN.png")
    assert path.exists("./redactedSSN.png")
