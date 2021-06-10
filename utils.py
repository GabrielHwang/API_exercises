import urllib.request
import json
import re
import urllib.request
import hashlib

#
def GetUUID():
    s = input("---请粘贴Bilibili主页的网址：---\n（形如 https://space.bilibili.com/******\n")
    nums = re.findall(r'\d+', s)
    return nums[0]

def GetInfor(UserId):
    InforAPI = "https://api.bilibili.com/x/relation/stat?vmid="+UserId+"&jsonp=jsonp"
    InforJson=json.loads(urllib.request.urlopen(InforAPI).read())
    following=InforJson['data']['following']
    follower= InforJson['data']['follower']
    user={'UUID':UserId,'following':following,'follower':follower}
    
    return user

def GetBvid():
    I = input("---请粘贴Bilibili视频的网址（web端）---\n 形如 https://www.bilibili.com/video/*****\n")
    BvidNum=re.findall(r"[^/]+(?!.*/)",I) #正则到最后反斜杠后的str
    return BvidNum[0]
    
def GetVideoInfo(Bvid):
    
    VideoInfoAPI="http://api.bilibili.com/x/web-interface/view?bvid="+Bvid
    VideoInfoJson=json.loads(urllib.request.urlopen(VideoInfoAPI).read())
    biv=VideoInfoJson['data']['bvid']
    aid=VideoInfoJson['data']['aid']
    pubdate=VideoInfoJson['data']['pubdate']
    name=VideoInfoJson['data']['owner']['name']
    mid=VideoInfoJson['data']['owner']['mid']
    info={'aid':aid,'bivd':biv,'pubdate':pubdate,'name':name,'mid':mid}
    return info
    
