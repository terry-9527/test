#读配置文件server.conf
import configparser,os,pymysql,pandas,requests
def read_server_conf(): #读本轮测试要用的服务器的具体信息
    which_sever=read_entry()[0]
    #1、导入模块，一般放到文件最前面
    #2、创建配置对象
    confile=configparser.ConfigParser()
    #3、读文件内容到对象
    confile.read('server.conf',encoding='utf-8')
    #4、取对象中的数据
    ip=confile.get(which_sever,'ip') #取formal节点的ip键的值
    port=confile.get(which_sever,'port')
    #5、组装数据为要求的格式
    host='http://'+ip+':'+port+'/'
    return host #返回字符串

def read_db_conf(): #读本轮测试要用的数据库信息
    which_db=read_entry()[1]
    #创建对象->将文件数据读入到内存对象->获得对象中存储的键的值->组装数据
    confile=configparser.ConfigParser()
    confile.read('db.conf',encoding='utf-8')
    host=confile.get(which_db,'host')
    user=confile.get(which_db,'user')
    password=confile.get(which_db,'password')
    db=confile.get(which_db,'db')
    dbinfo={'host':host, 'user':user, 'password':password, 'db':db}
    return dbinfo #返回字典

def read_entry(): #读入口名
    confile=configparser.ConfigParser()
    confile.read('entry.ini', encoding='utf-8')
    which_server=confile.get('entry', 'which_server')
    which_db=confile.get('entry', 'which_db')
    return which_server, which_db #返回元组

def read_sqls(sqlfiles=[]): #读sql文件中的sql命令到列表
    if len(sqlfiles)==0: #没给参数，或者给的空列表
        fold_files=os.listdir()
        for f in fold_files:
            if f.endswith('.txt'):
                sqlfiles.append(f)
    # print(sqlfiles)
    #执行到此处，sqlfiles中存着1个或多个txt文件名
    sqls=[] #存sql语句
    for txtfile in sqlfiles: #txtfile代表每一个txt文件
        for row in open(txtfile,'r',encoding='utf-8'): #row表示文件中的一行
            if not row.startswith('--') and len(row.strip())>0:
                sqls.append(row.strip())
    # print(sqls)
    return sqls

def conn_db(): #连接数据库
    #导入模块->调用connect
    dbinfo=read_db_conf() #{'host':'192...', 'user':'root', ...}
    conn=pymysql.connect(**dbinfo) #dbinfo是字典，**可以把字典拆成host=，user=这种形式
    # print(conn.open) #open如果是True，表示连接成功，否则抛出异常
    return conn

def init_db(sqlfiles=[]): #初始化数据库提供sql的文件名，文件名不处理给read_sqls函数处理
    #连接数据库->创建游标->指定sql语句->执行sql语句->提交数据->关闭数据库连接
    conn=conn_db() #连接数据库，直接调用前面的连接数据库函数
    cursor=conn.cursor()
    sqls=read_sqls(sqlfiles) #sql语句列表，读sql文件中的sql语句
    for sql in sqls: #循环执行
        cursor.execute(sql)
    conn.commit()
    conn.close()

def read_cases(xlsfile, columns=[]): #读excel测试用例文件，后面加中括号表示列表形式
    #前面导入pandas模块
    if len(columns)==0: #没给columns参数，或者给的空列表[]
        data=pandas.read_excel(xlsfile)#excel文件名
    else:  #返回字典
        data=pandas.read_excel(xlsfile, usecols=columns) #要写俩个分支
        #usecols=columns和columns=[]不能同时出现，空列表说明没给列名返回none是不合适的
    cases = data.values.tolist() #转换为二维列表
    # print(cases)
    for case in cases: #i表示下标
        for i in range(len(case)): #len(case)表示一条用例case中的列数
            if str(case[i]).startswith('{') and str(case[i]).endswith('}'):
                case[i]=eval(case[i])
    return cases

def check_db(case_info,data,check_sql,db_expect_rows): #落库检查
    #连接数据库->创建游标->指定sql->执行sql->获得数据库实际结果->关闭数据库连接->结果比对
    conn=conn_db() #直接调用函数
    cursor=conn.cursor()
    cursor.execute(check_sql)#前面指定过了
    result=cursor.fetchone() #取一行(元组)
    db_actual_rows=result[0] #取一列
    if db_expect_rows==db_actual_rows:
        print(case_info+'==落库检查通过')
    else:
        print(case_info+'==落库检查失败==要检查的数据：'+str(data)+'==预期行数：'
              +str(db_expect_rows)+'==实际行数：'+str(db_actual_rows))

def post(case_info,address,argument,expect): #发送请求、比对响应结果
    res=requests.post(address,argument) #res获得响应结果
    # print(res.headers['content-type'])
    #在查看响应类型之前先检查下响应类型
    if 'text' in res.headers['Content-Type']:
        actual=res.text
        if expect in actual:
            print(case_info+'==响应结果比对通过')
        else:
            print(case_info+'==响应结果比对失败==预期结果：'+str(expect)+'==实际结果：'+str(actual))
    elif 'json' in res.headers['Content-Type']:
        actual=res.json() #获得实际结果对比测试
        if expect==actual:
            print(case_info + '==响应结果比对通过')
        else:
            print(case_info + '==响应结果比对失败==预期结果：' + str(expect) + ''
                            '==实际结果：' + str(actual))
    else:
        print('暂不处理text和json之外的其他响应类型')

def test_login(): #测试登录接口
    #初始化数据库->读用例->发送请求、比对响应结果
    init_db(['login.txt']) #登录时候初始化login文件，一定是列表形式的实参
    cases=read_cases('login.xlsx') #case_id 0、case_name 1、data 2、expect 3
                                   #文件后面不指定哪些列的话，默认是所有列
    # address=read_server_conf()+'exam/login/'
    #地址需要调用函数read_server_conf函数需要一个参数，which_server
    which_server=read_entry()[0] #需要哪一个服务器名称
    address=read_server_conf()+'exam/login/' #读出服务器信息，然后去进组装
    #因为 read_server_conf返回值是http://host:port/所以加上接口名称
    for case in cases: #case是一条数据
        case_info=case[0]+':'+case[1]
        argument=case[2]
        expect=case[3]
        post(case_info,address,argument,expect) #发送给post请求

def test_signup(): #测试注册接口
    #初始化数据库->读用例->发送请求、比对响应结果->落库检查
    init_db(['signup.txt'])
    # case_id 0、case_name 1、data 2、expect 3、check_sql 4、db_expect_rows 5
    cases=read_cases('signup.xlsx')
    address=read_server_conf()+'exam/signup/'
    for case in cases:
        case_info=case[0]+':'+case[1]
        argument=case[2]
        expect=case[3]
        post(case_info,address,argument,expect)
        check_sql=case[4] #落库检查
        db_expect_rows=case[5]
        check_db(case_info,argument,check_sql,db_expect_rows) #调用check_db函数把参数传进来

#调试
if __name__=='__main__':
    # print(read_entry())
    # print(read_server_conf())
    # print(read_db_conf())
    # print(read_sqls())
    # print(read_sqls([]))
    # print(read_sqls(['login.txt']))
    # print(read_sqls(['login.txt','signup.txt']))
    # print(read_sqls('login.txt')) #报错：实参必须是列表
    # print(conn_db().open) #open属性是不是True
    # init_db()
    # init_db([])
    # init_db(['signup.txt'])
    # print(read_cases('login.xlsx'))
    # print(read_cases('signup.xlsx',[]))
    # print(read_cases('login.xlsx',['data','expect']))
    # check_db('用例信息',{'line':'all'},'select count(*) from user',4)
    # post('用例信息','http://192.168.66.69/exam/login/',{'username':'admi','password':'123456'},'登录成功')
    # post('用例信息', 'http://192.168.66.69/exam/signup/', {'username': 'admin', 'password': '123456','confirm':'123456'}, {'Status': 1004, 'Result': 'Username admin is taken', 'Message': '用户名已被占用'})
    test_login()
    test_signup()