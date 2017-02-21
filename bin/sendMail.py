import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
from bin.configRead import configRead

class sendMail():

    def send_mail(self):
        config=configRead()
        #设置发送服务器
        sendserver=config.config_Read_Mail('sendserver')
        #用户名和密码
        username=config.config_Read_Mail('username')
        password=config.config_Read_Mail('password')
        #发送方
        sender=config.config_Read_Mail('sender')
        #接收方
        recevier=config.config_Read_Mail('recevier')
        #发送邮件主题
        subject=config.config_Read_Mail('subject')
        #发送内容
        msg=MIMEText(config.config_Read_Mail('msg'))
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