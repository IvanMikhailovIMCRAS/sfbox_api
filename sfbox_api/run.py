import os

def run(word: str) -> int:
    with open(os.path.join(os.getcwd(),"data/test.in"), 'w') as f:
        f.write(word)
    with open("./data/test.in", 'r') as f:
        s = f.read()
    return len(s)