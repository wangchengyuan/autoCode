import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart

class sendMail():

    def send_mail(self):
        #设置发送服务器
        sendserver="smtp.163.com"
        #用户名和密码
        username="tianyasisi11@163.com"
        password="tianya1124"
        #发送方
        sender="tianyasisi11@163.com"
        #接收方
        recevier="784444045@qq.com"
        #发送邮件主题
        subject="Python test"
        #发送内容
        msg=MIMEText("HELLO")
        msg['Subject']=Header(subject,"utf-8")

        #连接发送邮件
        smtp=smtplib.SMTP()
        smtp.connect(sendserver)
        smtp.login(username,password)
        smtp.sendmail(sender, recevier, msg.as_string())
        smtp.quit()

    def send_mail_att(self):

        #设置发送服务器
        sendserver="smtp.qq.com"
        #用户名和密码
        username="7844045@qq.com"
        password="tianyalieren"
        #发送方
        sender="78444045@qq.com"
        #接收方
        recevier="917515308@qq.com"
        #发送邮件主题
        subject="Python test"
        #发送附件
        sendfile=open('D:\\test\\test.txt','rb').read()

        att=MIMEText(sendfile,'base64','utf-8')
        att["Content-Type"]='application/octet-stream'
        att["Content-Disposition"]='attachment;filename=log.txt'

        msgRoot=MIMEMultipart('related')
        msgRoot['Subject']=subject
        msgRoot.attach(att)

        # 连接发送邮件
        smtp = smtplib.SMTP()
        smtp.connect(sendserver)
        smtp.login(username, password)
        smtp.sendmail(sender, recevier, msgRoot.as_string())
        smtp.quit()