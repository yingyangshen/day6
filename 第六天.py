#作业
"""
实现random.sample
"""
import random
print 'N must >K else error'
n=int(input("n="))
k=int(input("k="))
result=[]
x=range(n)
for i in range(k):
    t=random.randint(i,n-1)
    temp=x[i]
    x[i]=x[t]
    x[t]=temp
    result.append(x[i])
print(result )
input('Inpuy AnyKey to exit')

"""
实现max函数

"""
def biggest(a,b,c):
    # 先比较a和b
    if a>b:
        maxnum = a
    else:
        maxnum = b
    # 再比较maxnum和c
    if c>maxnum:
        maxnum=c
    return maxnum
a1=float(input("请输入一个数"))
a2=float(input("请输入一个数"))
a3=a1=float(input("请输入一个数"))
maxnum = biggest(a1,a2,a3)
print(maxnum)

"""
实现判断两个字符串是否相等的方法
"""
def comparison(a,b):
    ib=0
    for ia in range(len(a)):
        if ord(a[ia:ia+1])-ord(b[ib:ib+1])==0:
            ib=ib+1
            if ib==len(b):
                print('a and b are equall')
        else:
            print('a and b are not equall')
            break
m = input("请你输入第一个字符串：")
n = input("请你输入第二个字符串：")
comparison(m,n)




"""
函数参数总结
1.位置匹配 func(name)
2.关键字匹配 func(key=value)
3.收集匹配
　　1.元组收集 func(name,arg1,arg2)
　　2.字典收集 func(name,key1=value1,key1=value2)
4.参数顺序
 
1.位置匹配 func(name)
def func(arg1,arg2,arg3):
    return arg1,arg2,arg3

print func(1,2,3)

(1, 2, 3)
 
2.关键字匹配 func(key=value)
和顺序无关，可以有默认值。

def func1(k1='',k2=None,k3=''):
    return k1,k2,k3

print (func1(k3=5,k1=4,k2=3))
print (func1(k1=1,k3=2))
(4, 3, 5)
(1, None, 2)

3.收集匹配
　　1.元组收集 func(name,arg1,arg2)
　　2.字典收集 func(name,key1=value1,key1=value2)

def func2(a,d,b=4,*kargs,**kwargs):
    return kargs
print (func2(2,3,4,5,6,7,9,[1,2,3,4],{1:2,3:4}))

def func2(*kargs,**kwargs):
    return kargs
print (func2(2,3,4,5,6,7,9,[1,2,3,4],{1:2,3:4}))

def func2(*kargs,**kwargs):
    return kargs
print (func2(2,3,4,{1:2,3:4},[1,2,3,4],5,6,7,9))


(5, 6, 7, 9, [1, 2, 3, 4], {1: 2, 3: 4})
(2, 3, 4, 5, 6, 7, 9, [1, 2, 3, 4], {1: 2, 3: 4})
(2, 3, 4, {1: 2, 3: 4}, [1, 2, 3, 4], 5, 6, 7, 9)

4.参数顺序
1.先是位置匹配的参数    a, d
2.再是关键字匹配的参数  b=4
3.收集匹配的元组参数     *kargs  一个星号是元祖
4.收集匹配的关键字参数  **kwargs 两个星号是字典
 
5. 一些习题
'''
1.定义一个func(name)，该函数效果如下。
assert func("lilei") = "Lilei"
assert func("hanmeimei") = "Hanmeimei"
assert func("Hanmeimei") = "Hanmeimei"
'''
1 def capstr(name):
2     return name.capitalize()

"""
"""2.定义一个func(name,callback=None),效果如下。
assert func("lilei") == "Lilei"
assert func("LILEI",callback=string.lower) == "lilei"
assert func("lilei",callback=string.upper) == "LILEI"

3.定义一个func(*kargs),效果如下。
l = func(1,2,3,4,5)
for i in l:
print i,
#输出 1 2 3 4 5
l = func(5,3,4,5,6)
for i in l:
print i
#输出 5 3 4 5 6
"""
def getitem(*kargs):
    return kargs

"""
4.定义一个func(*kargs)，该函数效果如下。
assert func(222,1111,'xixi','hahahah') == "xixi"
assert func(7,'name','dasere') == 'name'
assert func(1,2,3,4) == None
"""

def shortstr(*kargs):
    '''
    shortstr(*kargs) -> str or None
    return the shortest str in the kargs, or return None if no str in it.
    '''
    #过滤非字符串
    lis = filter(lambda x:isinstance(x,str),kargs)
    #收集长度
    len_lis = [len(x) for x in lis]

    if len_lis:
            min_index = min(len_lis)
            return lis[len_lis.index(min_index)]         #这两部绝对精华呢！
    return None

"""
5.定义一个func(name=None,**kargs),该函数效果如下。
assert func(“lilei”) == "lilei"
assert func("lilei",years=4) == "lilei,years:4"
assert func("lilei",years=10,body_weight=20) == "lilei,years:4,body_weight:20"
"""

def detail(name=None,**kargs):   #方法一
    '''
    detail(name=None,**kargs) -> str
    name is a str.return a str like'name,key1:value1,key2:value2'    这个函数特定的功能
    '''
    data = []
    for x,y in kargs.items():
        data.extend([',', str(x), ':', str(y)])

    info = ''.join(data)
    return '%s%s'%(name,info)

def func(name=None,**kargs):    #方法二
    lis = ["%s:%s"%(k,v) for k,v in kargs.items()]
    lis.insert(0,name)
    return ','.join(lis)



#coding =utf-8
#Lesson: 进阶篇3-函数第二节

'''
1  定义一个方法get_num(num)，num参数是列表类型，判断列表里面的元素为数字类型。
   其它类型则报错，并且返回一个偶数列表：（列表里面的元素为偶数）
'''
"""def get_num(num_list):
    '判断列表里面的元素为数字类型'

    num_list_k = []

    if not isinstance(num_list,list):        # 
isinstance
(object, classinfo) object的类型
return '请输入以list为类型的参数。'

    else:
        for i in num_list:
            if not isinstance(i,int):
                return '列表里面的元素必须为数字类型。'
            elif i % 2 == 0:
                num_list_k.append(i)
    return num_list_k

print (get_num([1,2,5,6,8,20]))

assert get_num([1,2,5,6,8,20])== [2,6,8,20],'断言得到的结果。'
assert get_num((1,2,5,7,9,3))=='请输入以list为类型的参数。'
assert get_num([1,'abcd',5,6,8,20])=='列表里面的元素必须为数字类型。'

print(get_num.__doc__)           # 属性__doc__可以输出文档字符串的内容  
##################################################################################################
'''
2 定义一个方法get_page(url),url参数是需要获取网页内容的网址，
  返回网页的内容。 提示（可以了解python的urllib模块）。
'''
# 方法一
from urllib.request import urlopen

def get_page(url):
    '返回网页的内容'

    if not isinstance(url,str):
        return '输入的网址类型不对。'
    elif url.startswith('http://'):
        url_info = urlopen(url).read()
        return url_info

    else:
        return '请检查您输入的网址格式，网址要以 http:// 开始。'

print (get_page('http://www.baidu.com'))

assert get_page('www.baidu.com') =='请检查您输入的网址格式，网址要以 http:// 开始。'
assert get_page(123) == '输入的网址类型不对。'
###################################################################################################
# 方法二
def get_page(url):
    if not isinstance(url,str):
        return '输入的数据类型不对。'
    if not ur.startswith('http://') and not url.startswith('http://'):
        return "error url_format"

    try:
        url_info = urlopen(url).read()
    except Exception as e:
        logging.debug(e)
    else:
        return url_info
assert get_page('www.baidu.com') == '请检查您输入的网址格式，网址要以 http:// 开始。'
assert get_page(123) == '输入的网址类型不对。'
###################################################################################################

'''
3 定义一个方法 func, 该func引入任意多的列表参数，返回所有列表中最大的那个元素。
'''

def func(*l_args):
    all_list = []
    for i in l_args:
        if isinstance(i,list):
            all_list.extend(i)
        else:
            return '请输入正确的列表参数。'
    all_list.sort()

    return all_list[-1]
print (func([1,845,10000,7,8,9,]),[8888800,3345,111],[1,2,3]))
assert func([4,5,7,19],[3,5,7],[1,2,3]) == 19,'断言结果为最大的数19'
assert func([4,5,7,19],'abc',[1,2,3]) == '请输入正确的列表参数。'
#######################################################################################################
'''
4 定义一个方法get_dir(f), f参数为任意一个磁盘路径，该函数返回路径下的所有文件夹组成的列表，
  如果没有文件夹则返回“not dir”
'''

import os

def get_dir(f):

    l_dir = []

    if not os.path.isdir(f):
        return '输入的磁盘路劲的参数不正确。'

    else:
        for i in os.listdir(f):
            l_dir.append(i)

        if l_dir == []:            #  if l_dir:       后面的代码更好看
            return 'Not dir'     #     return l_dir
        else:                      #  else：
            return l_dir           #     return 'Not dir'
print (get_dir('test/'))
assert type(get_dir('test/'))== list,'is list'
assert get_dir('123') == '输入的磁盘路径的参数不正确

"""
"""