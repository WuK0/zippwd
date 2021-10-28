import zipfile
import itertools


dictionaries = ['1', '2', '3', '4','5','6','7','8','9','0',
                'a','b','c','d','e','f','g','h','i','j','k',
                'l','m','n','o','p','q','r','s','t','u','v',
                'w','x','y','z']         #组成破解字典的关键字符（可以按照自己需求添加）


def allkeyword():            #排列出字符所有4个字符的组合
    allkey1 = itertools.product(dictionaries,repeat=4)
    allkey2 = (''.join(i) for i in allkey1)
    return allkey2


def trypassword (password):
    try:
        ZIPFILE = zipfile.ZipFile(r'./test.zip')   #定义对象，相当于定义一个压缩文件1.zip
        ZIPFILE.extractall(path=r'./',pwd=password.encode('utf-8')) 
        print(f"解压成功,正确密码为：{password}")
        return True
    except:
        print(f"解压失败,尝试密码为：{password}")
        return False

#用trypassword函数返回的True或者Flase来判定程序是否终止。
for pwd in allkeyword() :   
    if trypassword(pwd):
        break
