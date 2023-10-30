import os

def run(word: str) -> int:
    current_directory = os.path.dirname(os.path.realpath(__file__))
    parent_directory = os.path.split(current_directory)[0]
    with open(os.path.join(parent_directory,"data/test.in"), 'w') as f:
        f.write(word)
    with open(os.path.join(parent_directory,"data/test.in"), 'r') as f:
        s = f.read()
    return len(s)