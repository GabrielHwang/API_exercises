import urllib.request
import json
import re
import urllib.request
import hashlib
import os,sys
#basic idea:
#1. input correct website link
#2. regex right uid from input information
#3. find a right API which can get a json file
#4. deal with the json information.
#5. JSON format tool:https://www.bejson.com/
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
    cid=VideoInfoJson['data']['cid']
    info={'aid':aid,'bivd':biv,'pubdate':pubdate,'name':name,'mid':mid,'cid':cid}
    return info

def GetIP(Bvid):
    IPAPI="http://api.bilibili.com/x/web-interface/zone"
    IPJson=json.loads(urllib.request.urlopen(IPAPI).read())
    addr=IPJson['data']['addr']
    country=IPJson['data']['country']
    province=IPJson['data']['province']
    isp=IPJson['data']['isp']
    IPInfo={'addr':addr,'country':country,'province':province,'isp':isp}
    return IPInfo
    
    
def GetURL(Bvid,CID):
    URL_API="http://api.bilibili.com/x/player/playurl?bvid="+ Bvid+"&cid="+str(CID)+"&fnval=1"
    URL_JSON=json.loads(urllib.request.urlopen(URL_API).read())
    URL=URL_JSON['data']['durl'][0]['backup_url'][0]
    return URL

