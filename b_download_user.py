import requests
import time 
def get_star(url):
    html = requests.get(url).json()['data']
    # follower = html['follower']
    # following = html['following']
    #print("粉丝数：{}，关注数：{}".format(follower,following))
    #print("-"*20)

def download_face(face_url,name):
    image = requests.get(face_url).content
    with open("./{}.jpg".format(name),'wb') as f:
        f.write(image)

def get_userdata(url):
    jsondata = requests.get(url).json()['data']
    # name = jsondata['name']
    # sex = jsondata['sex']
    # level = jsondata['level']
    # birthday = jsondata['birthday']
    # coins = jsondata['coins']
    #print("名字是：{}  性别是：{}  等级是：{}  生日是：{}  硬币数目：{}".format(name,sex,level,birthday,coins))
    # face_url = jsondata['face']
    #print("正在下载头像……")
    #download_face(face_url,name)

def main():
    
    
    for i in range(1000, 1010):
        url = "https://api.bilibili.com/x/space/acc/info?mid={}&jsonp=jsonp".format(i)
        get_userdata(url)
        url2 = "https://api.bilibili.com/x/relation/stat?vmid={}&jsonp=jsonp".format(i)
        get_star(url2)

if __name__ == '__main__':
    time_start = time.time()
    main()
    time_end = time.time()    #结束计时
    time_c= time_end - time_start   #运行所花时间
    print('time cost', time_c, 's')
