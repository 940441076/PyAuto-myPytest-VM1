# -*- coding: utf-8 -*-
# @Time ： 2023/6/14 10:50
# @Auth ： 醉在深海里的鱼🐟
# @Motto:  洗洗睡吧，梦里啥都有
from dingtalkchatbot.chatbot import DingtalkChatbot
def send_dingtalk():
    '''发送钉钉消息'''
    systemInfo = read_yaml('/extract.yaml')['systemInfo']
    try:
        webhook = 'https://oapi.dingtalk.com/robot/send?access_token=034ef99dce9cc9bcb08ce8ed887c8c06ce17a03989cee023098338a06957f419'
        secret = 'SECfc4c756e21efaf7ffdbef4fb2d732195f177d8d90847956274ea6c887287502c'
        ding = DingtalkChatbot(webhook, secret)
        try:
            window = WindowControl(searchDepth=1, Name='C:\Windows\py.exe')
            textContent = window.DocumentControl(searchDepth=1).GetTextPattern().DocumentRange.GetText()
            content = re.compile('at <(.*?)/>.', re.S)
            http_address = re.findall(content, textContent)[0]
        except:
            http_address = '地址错误'
        ding.send_text('{}自动化测试完成，\n测试报告临时链接(内网)：\n{}'.format(systemInfo['deviceType'],http_address))
        # ding.send_image(r'{}/pytest-VM1/result/report/result.jpg'.format(http_address))

    except Exception as e:
        print(e)
