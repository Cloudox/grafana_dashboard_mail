# grafana_dashboard_mail
下载并定时发送Grafana的Dashboard面板图日报邮件

- main.py：入口文件
- get_grafana_dashboard.py：通过组装url下载指定时间区间的日报dashboard图片
- send_mail.py：发送日报邮件或者下载失败的体型邮件
- schedule：第三方定时器库（https://github.com/dbader/schedule）

具体说明参考
