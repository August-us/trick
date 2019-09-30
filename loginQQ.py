import os
import time
import win32gui
import win32api
import win32con
from pymouse import *
from pykeyboard import PyKeyboard
from ctypes import *


def QQ(qq, pwd):
    # 运行QQ
    os.system('"D:\Program Files (x86)\Tencent\TIM\Bin\QQScLauncher.exe"')
    time.sleep(5)
    # 获取QQ的窗口句柄
    # 参数1是类名,参数2是QQ软件的标题
    a = win32gui.FindWindow(None, "TIM")
    # 获取QQ登录窗口的位置
    loginid = win32gui.GetWindowPlacement(a)
    print(loginid)
    print(loginid[4][0])
    print(loginid[4][1])

    # 定义一个键盘对象
    k = PyKeyboard()

    # 把鼠标放置到登陆框的输入处
    windll.user32.SetCursorPos(loginid[4][0] + 192, loginid[4][1] + 282)

    # 按下鼠标再释放
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)  # press mouse
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)  # release mouse

    time.sleep(2)
    ###input username

    print(qq)
    # 输入用户名
    k.type_string(qq)
    time.sleep(0.2)
    ##tab
    # 按下tab，切换到输入密码的地方
    win32api.keybd_event(9, 0, 0, 0)
    win32api.keybd_event(9, 0, win32con.KEYEVENTF_KEYUP, 0)
    # 按下tab用下面两行也行
    # k.press_key(k.tab_key)
    # k.release_key(k.tab_key)
    # 按下tab用下面一行也行
    # k.tap_key(k.tab_key)

    # 输入密码
    k.type_string(pwd)

    # 按下回车
    win32api.keybd_event(13, 0, 0, 0)
    win32api.keybd_event(13, 0, win32con.KEYEVENTF_KEYUP, 0)

def QQZan(visitqq,myqq,mypas):
    from selenium import webdriver
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.get('https://user.qzone.qq.com/{}/main'.format(visitqq))
    browser.switch_to_frame('login_frame')
    #通过使用选择器选择到表单元素进行模拟输入和点击按钮提交
    # browser.find_element_by_id('switcher_plogin').click()
    # browser.find_element_by_id('u').clear()
    # browser.find_element_by_id('u').send_keys(myqq)
    # browser.find_element_by_id('p').clear()
    # browser.find_element_by_id('p').send_keys(mypas)
    # browser.find_element_by_id('login_button').click()
    # 使用TIM关联登录
    time.sleep(3)
    browser.find_element_by_id('nick_1289269253').click()
    time.sleep(3)
    browser.find_element_by_xpath('//*[@id="like"]/a[1]').click()
    browser.quit()

def qqmessage(Name):
    import os
    time.sleep(3)
    clientDict = {'17孙玮聪': '864110913','孙颢伊':'1640664598'}  # 人名 和对应的 qq号
    qq =clientDict[Name]
    os.system('start tencent://message/?uin=' +qq )
    import win32gui
    import win32con
    import win32clipboard as w



    def getText():
        """获取剪贴板文本"""
        w.OpenClipboard()
        d = w.GetClipboardData(win32con.CF_UNICODETEXT)
        w.CloseClipboard()
        return d

    def setText(aString):
        """设置剪贴板文本"""
        w.OpenClipboard()
        w.EmptyClipboard()
        w.SetClipboardData(win32con.CF_UNICODETEXT, aString)
        w.CloseClipboard()

    def send_qq(msg):
        """发送qq消息
        to_who：qq消息接收人
        msg：需要发送的消息
        """
        # 将消息写到剪贴板
        setText(msg)
        # 获取qq窗口句柄
        time.sleep(3)
        qq = win32gui.FindWindow(None, Name)
        print(qq)
        # 投递剪贴板消息到QQ窗体
        win32gui.SendMessage(qq, 258, 22, 2080193)
        win32gui.SendMessage(qq, 770, 0, 0)
        # 模拟按下回车键
        win32gui.SendMessage(qq, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)
        win32gui.SendMessage(qq, win32con.WM_KEYUP, win32con.VK_RETURN, 0)

    # 测试
    msg = '这是一条自动消息,防止忘记发消息'
    send_qq(msg)

# get the current handle
# print(win32gui.GetWindowText(win32gui.GetForegroundWindow()))
# print(win32gui.GetActiveWindow())

def lock():
    import win32gui, win32con, win32api
    from ctypes import windll
    import time

    user = windll.LoadLibrary('user32.dll')
    user.LockWorkStation()
    '''
    切换用户
    username = 'ADMINISTRATOR'
    password = ''
    domain = ''
    token = win32security.LogonUser (
        username,
        domain,
        password,
        win32con.LOGON32_LOGON_SERVICE,
        win32con.LOGON32_PROVIDER_DEFAULT
    )
    win32security.ImpersonateLoggedOnUser(token)
    '''
    time.sleep(3)
    win32api.keybd_event(13, 0, 0, 0)
    win32api.keybd_event(13, 0, win32con.KEYEVENTF_KEYUP, 0)

    handle = win32gui.GetForegroundWindow()
    print(win32gui.GetWindowText(win32gui.GetForegroundWindow()))
    win32api.SendMessage(handle, win32con.WM_KEYDOWN, ord('A'), 0)
    temp = win32api.PostMessage(handle, win32con.WM_CHAR, ord('A'), 0)
    win32api.SendMessage(handle, win32con.WM_KEYUP, ord('A'), 0)



    # win32api.keybd_event(68, 0, 0, 0)
    # win32api.keybd_event(67, 0, 0, 0)
    #
    # win32api.keybd_event(57, 0, 0, 0)
    # win32api.keybd_event(49, 0, 0, 0)
    # win32api.keybd_event(51, 0, 0, 0)
    # win32api.keybd_event(13, 0, 0, 0)
    # win32api.keybd_event(13, 0, win32con.KEYEVENTF_KEYUP, 0)


if __name__ == "__main__":
    # fn = "qq.txt"
    # F = open(fn, "r").readlines()
    sun='孙颢伊'
    swc='17孙玮聪'
    # for i in F:
    #     tx = i.split('----')
    #     print(tx[0])  # 打印用户名
    #     print(tx[1])  # 打印密码
    try:
        QQZan(1640664598,'1289269253', ' ')
    except:
        pass
    qqmessage(str(sun))