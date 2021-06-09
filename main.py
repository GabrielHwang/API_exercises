from utils import *

if __name__ == '__main__':
    UserId=str(GetUUID())
    print('获取ID成功，id为'+UserId)
    infor=GetInfor(UserId)
    print("{}{}\n {}{}\n {}{}\n".format("用户id： ",infor['UUID'],"已关注: ",infor['following'],"被关注",infor['follower']))
