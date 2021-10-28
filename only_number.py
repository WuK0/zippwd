#此代码适合于破解密码为0-999999的密码，数字区间可以自己设置
import time
import zipfile
from tqdm import tqdm
def zipcrackl(start,end):
    a = time.time()
    zfile = zipfile.ZipFile('./1.zip')#把要破解的zip的文件名替换ZipFile里面的参数
    for i in tqdm(range(start,end)):
        try:
            zfile.extractall(path='./',pwd=str(i).encode('ascii'))
            print(u'密码是：'+str(i))
            print(u'破解时间是：'+str(time.time()-a)+'s')#破解时间减去开始那个时刻的时间，得到的就是破解这个压缩文件的时间
            break 
        except Exception as e:
            #print(e)
            pass 
if __name__ == '__main__':
    zipcrackl(0,999999)
