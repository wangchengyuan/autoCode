from xml.dom import minidom

class configRead():

    #邮件配置
    def config_Read_Mail(self,tagName):
        #打开xml文档
        dom = minidom.parse("D:\\test3\\mailconfig.xml")
        #获取文档元素对象
        root=dom._get_documentElement()
        tagname=root.getElementsByTagName(tagName)
        return tagname[0].firstChild.data
