import requests

url = 'https://translate.alibaba.com/trans/TranslateTextAddAlignment.do'

header = {}
# header[':authority']='translate.alibaba.com'
# header[':method']='POST'
# header[':path']='/trans/TranslateTextAddAlignment.do'
# header[':scheme']='https'
header['accept']='application/json, text/plain, */*'
header['accept-encoding']='gzip, deflate, br'
header['accept-language']='zh-CN,zh;q=0.9'
header['content-length']='98'
header['content-type']='application/x-www-form-urlencoded'
header['cookie']='_samesite_flag_=true; cookie2=108024e07cd09c9f4c1192d48c0ab3e8; t=e9e487ca2c3cd09dff5c976f339b5e88; _tb_token_=f399d333ee9eb; ali_apache_id=11.9.13.76.1593922541452.372024.6; cna=QyFJF0bYrRsCAavcoNM9bNpv; x5sec=7b227472616e736c6174696f6e6f70656e7365766963653b32223a2235623330333332333930346235353465616564316431326561306164333730314349756f6866674645504c55357179377438616b7977453d227d; isg=BD4-RBjw7eiQqznMS1qnBn7Kj1SAfwL5w4-1FehFcwF8i9hlUA8LCYgqA1dHs_oR; l=eBgf5n17OQ10IybOBO5Znurza77TaQRfhsPzaNbMiInca6QF9FNLvNQqG86WWdtjgtfbTetrb3kJjRIrh34dgPjPtZZY-2L27YJe-'
header['origin']='https://www.aliyun.com'
header['referer']='https://www.aliyun.com/product/ai/base_alimt?spm=5176.14040702.h2v3icoap.219.2cb671d9zUVsbd'
header['sec-fetch-dest']='empty'
header['sec-fetch-mode']='cors'
header['sec-fetch-site']='cross-site'
header['user-agent']='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'

header1 = {}
header1['accept']='application/json, text/plain, */*'
header1['accept-encoding']='gzip, deflate, br'
header1['accept-language']='zh-CN,zh;q=0.9'
header1['content-length']='82'
header1['content-type']='application/x-www-form-urlencoded'
header1['cookie']='_samesite_flag_=true; cookie2=108024e07cd09c9f4c1192d48c0ab3e8; t=e9e487ca2c3cd09dff5c976f339b5e88; _tb_token_=f399d333ee9eb; ali_apache_id=11.9.13.76.1593922541452.372024.6; cna=QyFJF0bYrRsCAavcoNM9bNpv; x5sec=7b227472616e736c6174696f6e6f70656e7365766963653b32223a2235623330333332333930346235353465616564316431326561306164333730314349756f6866674645504c55357179377438616b7977453d227d; isg=BD4-RBjw7eiQqznMS1qnBn7Kj1SAfwL5w4-1FehFcwF8i9hlUA8LCYgqA1dHs_oR; l=eBgf5n17OQ10IybOBO5Znurza77TaQRfhsPzaNbMiInca6QF9FNLvNQqG86WWdtjgtfbTetrb3kJjRIrh34dgPjPtZZY-2L27YJe-'
header1['origin']='https://www.aliyun.com'
header1['referer']='https://www.aliyun.com/product/ai/base_alimt?spm=5176.14040702.h2v3icoap.219.2cb671d9zUVsbd'
header1['sec-fetch-dest']='empty'
header1['sec-fetch-mode']='cors'
header1['sec-fetch-site']='cross-site'
header1['user-agent']='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'


data = {}
data['bizType']='general'
data['source']='aliyun'
data['srcText']='I really hate you'
data['srcLanguage']='zh'
data['tgtLanguage']='en'
true = 'true'
false = 'false'

data1 = {}
data1['srcLanguage']='en'
data1['tgtLanguage']='zh'
data1['srcText']='I really hate you'
data1['bizType']='general'
data1['source']='aliyun'
while True:
    leixing = input('输入类型：1、英译汉，2、汉译英：')
    if eval(leixing) == 2:
        data['srcText'] = input('输入待翻译内容（不超过200字）：')
        html = requests.post(url=url, headers=header, data=data).text
    elif eval(leixing) == 1:
        data1['srcText'] = input('输入待翻译内容（不超过200字）：')
        html = requests.post(url=url, headers=header1, data=data1).text
    else:
        print('输入错误，重新输入')
        continue
    #print(html)
    xx = eval(html)

    #print(xx)
    print('翻译结果：'+xx['listTargetText'][0]+'\n')