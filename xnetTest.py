import requests,time,cv2

def isConnected():
    proxies = { "https": "http://127.0.0.1:8086", }
    try:
        html = requests.get("https://www.google.com.hk/", proxies=proxies,timeout=60)
        print(html)
    except:
        return False
    return True

while True:
    print(time.asctime(time.localtime(time.time())))
    if isConnected():
        from loginQQ import qqmessage
        qqmessage('17孙玮聪')
        img=cv2.imread(r'C:\Users\Administrator\Desktop\Live2D-master\5aeb1057bb167.jpg')
        cv2.imshow('',img)
        cv2.waitKey()
        break
    time.sleep(540)


