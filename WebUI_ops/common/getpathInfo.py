import os


def getpathInfo():
    current_path = os.path.split(os.path.realpath(__file__))[0]
    root_path = os.path.dirname(current_path)
    return root_path


def scanfile(path):
    list1 = []
    for root, dirs, files in os.walk(os.path.join(getpathInfo(),path)):
        for file in files:
            if not file.startswith('__'):
                list1.append(os.path.join(root,file))
        # for dir in dirs:
        #     print(dir)
        #     # scanfile(dir)
    return list1


def getfilepath(filename):
    '''
    返回一个文件的绝对路径
    :param filedir: 文件所在目录
    :param filename: 文件名
    :return: 返回文件的绝对路径
    '''
    root_dir = getpathInfo()
    files = scanfile(root_dir)
    n =0
    for file in files:
        if filename == os.path.split(file)[1]:
            n+=1
            return file

    if n == 0:
        return "no such file"



if __name__ == '__main__':
    # path = getpathInfo()
    # print(path)
    # print(getfilepath('config','config.ini'))
    # path = getfilepath('page_location\login_location','login_lct.py')
    # print(path)
    # scanfile('common')
    g = getfilepath('login_opt.py')
    print(g)