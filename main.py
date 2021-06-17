from urllib.request import URLopener
from utils import *
import time
if __name__ == '__main__':
    UserId=str(GetUUID())
    print('获取ID成功，id为'+UserId)
    infor=GetInfor(UserId)
    print("{}{}\n {}{}\n {}{}\n".format("用户id： ",infor['UUID'],"已关注: ",infor['following'],"被关注",infor['follower']))

    Bvid=str(GetBvid())
    print('BV号为: '+Bvid)
    BvInfo=GetVideoInfo(Bvid)
    dateTime=BvInfo['pubdate']
    time_local=time.localtime(dateTime)
    time_pub= time.strftime("%Y-%m-%d %H:%M:%S",time_local)
   # print("https://space.bilibili.com/"+str(BvInfo['mid']))
    print("{}{}\n{}{}\n{}{}\n{}{}\n{}{}\n" \
        .format("用户名： " ,BvInfo['name'],"av: ",BvInfo['aid'],"主页","https://space.bilibili.com/"+str(BvInfo['mid']),"发布时间： ",time_pub,"cv: ",BvInfo['cid']))
    
    IP_Information=GetIP(Bvid)
    print("---获取IP地址中---")
    print("{}{}\n{}{}\n{}{}\n"\
        .format('addr: ',IP_Information['addr'],\
            'country: ',IP_Information['country'],\
                'isp: ',IP_Information['isp']))
    CID=BvInfo['cid']
    URL_addr=GetURL(Bvid,CID)
    print("---当前视频流为---")
    print(URL_addr)

    dailyPost = GetDailyPost()
    for item in dailyPost:
        pass
        