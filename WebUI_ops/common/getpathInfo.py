import os

def getpathInfo():
    current_path = os.path.split(os.path.realpath(__file__))[0]
    root_path = os.path.dirname(current_path)
    return root_path



if __name__ == '__main__':
    path = getpathInfo()
    print(path)