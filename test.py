import itertools

value={0:[],1:[],2:['a','b','c'],3:['d','e','f'],4:['g','h','i'],5:['j','k','l'],6:['m','n','o'],7:['p','q','r','s'],8:['t','u','v'],9:['w','x','y','z']}
# print(value[2])
class cartesian(object):
    def __init__(self):
        self._data_list = []

    def add_data(self, data=[]):  # 添加生成数据列表
        self._data_list.append(data)

    def build(self):  # 计算
        for item in itertools.product(*self._data_list):
            print(''.join(item))

def Inp():
    num=input('请输入用逗号隔开的数字(0-99)：')
    num=num.split(',')
    car = cartesian()
    for i in num:
        car.add_data(value[int(i)])
    car.build()

if __name__ == "__main__":
    Inp()
