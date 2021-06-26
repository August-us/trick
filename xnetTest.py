import requests,time,cv2

def isConnected():
<<<<<<< HEAD
    # proxies = { "https": "http://127.0.0.1:8086", }
    proxies = { "https": "http://127.0.0.1:1080", }

    try:
        html = requests.get("https://www.google.com.hk/", proxies=proxies,timeout=60)
        print(html)
=======
    proxies = { "https": "http://127.0.0.1:8086", }
    try:
        html = requests.get("https://www.google.com.hk/", proxies=proxies,timeout=5)
>>>>>>> 71c653ad5f149159b6bd60ac46828dd17c5d4c82
    except:
        return False
    return True

while True:
    print(time.asctime(time.localtime(time.time())))
    if isConnected():
        from loginQQ import qqmessage
<<<<<<< HEAD
        # qqmessage('17孙玮聪')
=======
        qqmessage('17孙玮聪')
>>>>>>> 71c653ad5f149159b6bd60ac46828dd17c5d4c82
        img=cv2.imread(r'C:\Users\Administrator\Desktop\Live2D-master\5aeb1057bb167.jpg')
        cv2.imshow('',img)
        cv2.waitKey()
        break
<<<<<<< HEAD
    # time.sleep(540)
=======
    time.sleep(595)
>>>>>>> 71c653ad5f149159b6bd60ac46828dd17c5d4c82


