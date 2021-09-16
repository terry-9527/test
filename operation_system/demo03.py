import unittest
from ddt import ddt,unpack,data
import pandas,json
import requests
def pandas_excel():
    excelfile = pandas.read_excel("testcase1.xlsx",usecols=['params','expect'])
    cases = excelfile.values.tolist()
    # print(cases)
    for case in cases:
        # print(case[2])
        for i in range(len(case)):
            if case[i].startswith('{') and case[i].endswith('}'):
                case[i] =eval(case[i])
    return cases
@ddt
class Demo02(unittest.TestCase):

    @data(*pandas_excel())
    @unpack
    def test_001(self,params,expect):
        url = "https://opstest.arsyun.com/api/v1/auth/login"
        # argument = json.dumps(args[2])
        # print(argument)
        res = requests.post(url=url,data=json.dumps(params))
        print(res.json())
        self.assertIn(expect,res.text)

if __name__ == '__main__':
    pandas_excel()