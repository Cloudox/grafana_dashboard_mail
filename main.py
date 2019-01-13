# coding: utf8

import schedule
import time
import get_grafana_dashboard
import send_mail

# 获取面板图并发邮件
def do_report():
    print("start to report")
    img_name = get_grafana_dashboard.download_db()
    if (img_name == "failed"): # 下载失败，邮件提醒
        send_mail.send_failed_mail()
    else: # 成功则发日报邮件
        send_mail.send_mail(img_name)
    print("report end")

# 定时每日8点发送
schedule.every().day.at("08:00").do(do_report)

while True:
    schedule.run_pending()
    time.sleep(1)