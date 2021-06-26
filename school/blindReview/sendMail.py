import configparser
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
import smtplib
from email.utils import formataddr
from email.mime.image import MIMEImage

MIMEImage()

def get_mail_message(content, sender, subject='盲审结果'):
    msg = MIMEMultipart('related')
    text = MIMEText(content, 'html', 'utf-8')  # 在content变量中传入准备好的hhtml代码
    msg.attach(text)
    msg['Subject'] = Header(subject, 'utf-8')  # 设置邮件的主题，放入subject变量中
    msg['From'] = formataddr(["何林", sender])

    return(msg)


def send_mail(receiver):
    # smtpserver = 'smtp.qq.com'                                       # 定义发件邮箱所用的服务器类型
    smtpserver = 'smtp.163.com'
    config = configparser.ConfigParser()  # 定义一个ConfigParser对象
    config.read("./config.ini")  # 使用该对象读取class.ini配置文件
    email = config.get("get_user", "user_mail")  # 获取section下的key值
    psswd = config.get("get_user", "user_pwd")  # 获取section下的key值
    smtp = smtplib.SMTP()                                            # 定义一个SMTP对象
    smtp.connect(smtpserver)                                         # 连接邮件服务器
    smtp.login(email, psswd)                                   # 使用邮箱和授权码登陆


    for i in receiver:
        msg = get_mail_message('盲审结果', email)
        attach = MIMEApplication(open("__init__.py", 'r', encoding='utf-8').read())
        attach.add_header('Content-Disposition', 'attachment', filename='盲审结果.word')
        msg.attach(attach)
        print('The current receiver is',i)
        smtp.sendmail(email, i, msg.as_string())                    # 循环发送邮件
    smtp.quit()                                                      # 退出登陆

send_mail([ '1289269253@qq.com'])