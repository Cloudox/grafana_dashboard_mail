# coding: utf8

import os,stat
import urllib.request
from datetime import datetime, date, time, timedelta
import time as Time

# 获取七日前0点与今日0点的时间戳
def last_seven_day():
    midnight = datetime.combine(date.today(), time.min)
    yesterday_mid = midnight - timedelta(days=7) # 想要此前几天的，就改这个参数
    epoch = datetime.utcfromtimestamp(0)
    midnight = midnight - timedelta(seconds=1)
    midnight = int((midnight - epoch).total_seconds() * 1000.0)
    yesterday_mid = int((yesterday_mid - epoch).total_seconds() * 1000.0)
    return str(yesterday_mid), str(midnight)

# 下载指定的dashboard
def download_db():
    # 组装url，跑代码之前现在浏览器试试
    dbuid = "xxxxxxx"
    grafana_server = "http://your-grafana-server-url"
    url = (grafana_server + '/render/d/' +
               dbuid + '?from=' +
               last_seven_day()[0] + '&to=' + last_seven_day()[1] +
               '&var-datasource=xxx&width=1500&height=700&tz=UTC%2B08%3A00'
               )
    header = {"Authorization": "Bearer YourAdminApiKeyToken"} # 用管理员去Grafana生成API Key
    request = urllib.request.Request(url,headers=header)
    try:
        # 访问并下载面板图
        response = urllib.request.urlopen(request)
        time_now = int(Time.time())
        time_local = Time.localtime(time_now)
        dt = Time.strftime("%Y-%m-%d",time_local)
        img_name = "img"+dt+".png"
        filename = 'E:\\Github\\grafana_dashboard_mail\\db_img\\' + img_name
        # print(response.getcode())
        if (int(response.getcode()) == 200):
            with open(filename, "wb") as f:
                f.write(response.read())
            return filename
        else:
            return "failed"
    except:
        return "failed"
    
 
