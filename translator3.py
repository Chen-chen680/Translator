import requests
import re
url = 'https://www.dreye.com.cn/trans/'
header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
          'Host':'www.dreye.com.cn',
          'Origin':'https://www.dreye.com.cn',
          'Referer':'https://www.dreye.com.cn/trans/',
          'Connection':'keep-alive',
          'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'}
data = {}
i=1

while i == 1:
    xuanze = input('1、英译汉，2、汉译英（默认英译汉）：')
    data['t_value']=input('输入你你要翻译的内容：')
    if xuanze == '1':    
        data['from']='en'  #zh-CHS
        data['to']='zh-CHS'  #en
    elif xuanze == '2':
        data['from']='zh=CHS'  #zh-CHS
        data['to']='en' #en
    else:
        data['from']='en'  #zh-CHS
        data['to']='zh-CHS'  #en
    data['sbt']='翻译'
    data['t_r'] = ''
    response = requests.post(url=url,data=data,headers=header)
    response_text = response.text
    response_reg = r'<textarea name="t_r" id="t_r_id" class="transtext">﻿(.*?)</textarea><br />'
    response_reg = re.compile(response_reg)
    text = re.findall(response_reg,response_text)
    print(text)
