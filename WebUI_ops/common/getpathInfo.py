import os


def getpathInfo():
    current_path = os.path.split(os.path.realpath(__file__))[0]
    root_path = os.path.dirname(current_path)
    return root_path

def scanfile(path):
    list1 = []
    for root,dirs,files in os.walk(path):
        for file in files:
            list1.append(file)
        for dir in dirs:
            scanfile(dir)
    return list1


def getfilepath(filename):
    '''
    输入文件目录
    :param filedir:
    :param filename:
    :return:
    '''
    root_path = getpathInfo()
    files = scanfile(root_path)
    print(os.path.abspath(filename))




    # return os.path.join(root_path, filedir, filename)


if __name__ == '__main__':
    # path = getpathInfo()
    # print(path)
    # print(getfilepath('config','config.ini'))
    path = getfilepath('login_opt.py')