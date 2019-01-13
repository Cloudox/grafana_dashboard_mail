# coding: utf8

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.utils import parseaddr, formataddr
import time as Time

# 发送dashboard日报邮件
def send_mail(img_name):
    sender = 'xxxxxxxx@qq.com'
    to_address = ['xxxxxxxx@qq.com']
    username = 'xxxxxxxx@qq.com'
    password = 'faslkjflajflj' # SMTP授权码
    msgRoot = MIMEMultipart('related')
    msgRoot['Subject'] = '监控日报'
    msgRoot['From'] = sender
    msgRoot['To'] = ",".join( to_address ) # 发给多人

    content = MIMEText('<html><head><style>#string{text-align:center;font-size:25px;}</style><div id="string">检查数面板<div></head><body><img src="cid:image1" alt="image1"></body></html>','html','utf-8')
    msgRoot.attach(content)
    # 获取图片
    fp = open(img_name, 'rb')
    msgImage = MIMEImage(fp.read())
    fp.close()
    msgImage.add_header('Content-ID', 'image1') # 该id和html中的img src对应
    msgRoot.attach(msgImage)

    smtp = smtplib.SMTP_SSL('smtp.qq.com:465')
    smtp.login(username, password)
    smtp.sendmail(sender, to_address, msgRoot.as_string())
    smtp.quit()

# 发送失败提醒邮件
def send_failed_mail():
    sender = 'xxxxxxxx@qq.com'
    to_address = ['xxxxxxxx@qq.com']
    username = 'xxxxxxxx@qq.com'
    password = 'faslkjflajflj'
    msgRoot = MIMEMultipart('related')
    time_now = int(Time.time())
    time_local = Time.localtime(time_now)
    dt = Time.strftime("%Y%m%d",time_local)
    msgRoot['Subject'] = '监控日报图获取失败-' + dt
    msgRoot['From'] = sender
    msgRoot['To'] = ",".join( to_address ) # 发给多人

    content = MIMEText("Dashboard图片下载失败",'utf-8')
    msgRoot.attach(content)

    smtp = smtplib.SMTP_SSL('smtp.qq.com:465')
    smtp.login(username, password)
    smtp.sendmail(sender, to_address, msgRoot.as_string())
    smtp.quit()