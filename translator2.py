# 2020.6
import requests
data= {}
data['f']='auto'
data['t']='auto'
i = 1
while i == 1:
    try:
        data['w']= input('输入待翻译的文本：')
        url = 'http://fy.iciba.com/ajax.php?a=fy'
        header = {'User-Agent':'ozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
                  'X-Requested-With':'XMLHttpRequest',
                  'referer':'http://fy.iciba.com/',
                  'origin':'http://fy.iciba.com'}
        response = requests.post(url=url,data=data,headers=header)
        response_text = response.text
        #pprint(eval(response_text))
        print('翻译结果：'+eval(response_text)['content']['out'])
    except KeyError:
        
        continue