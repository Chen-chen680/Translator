import requests
import hashlib
import time
# 加密算法
# "fanyideskweb" + e + i + "n%A-rKaT5fb[Gy?;N5@Tj"

def md5_jm(md5_str):
    md5 = hashlib.md5()
    md5.update(md5_str.encode())
    return md5.hexdigest()

def youdao(url, word):
    # 15692080356573
    # 15692088624641
    # 1569208035657
    time_new = time.time()

    salt = int(time_new * 10000)
    ts = int(time_new * 1000)
    # client = 'fanyideskweb'
    md5_str = 'fanyideskweb' + word + str(salt) + "n%A-rKaT5fb[Gy?;N5@Tj"
    md5 = md5_jm(md5_str)
    #print(md5)

    proxies = {
        'https': 'https://114.99.27.97:8010'
    }

    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Content-Length': str(233 + len(word)),
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Cookie': 'OUTFOX_SEARCH_USER_ID=1944855340@221.219.225.40; OUTFOX_SEARCH_USER_ID_NCOO=1997242050.3906953; _ga=GA1.2.1551638093.1565616359; P_INFO=m18232003371_1@163.com|1566282170|0|other|00&99|null&null&null#bej&null#10#0#0|182371&1||18232003371@163.com; _ntes_nnid=377e77d2405afe0816cdd59ade547e7a,1567385119737; JSESSIONID=aaax0pdnMSVmHbJbYRB1w; ___rl__test__cookies=1569207897066',
        'Host': 'fanyi.youdao.com',
        'Origin': 'http://fanyi.youdao.com',
        'Referer': 'http://fanyi.youdao.com/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'
    }
    data = {
        'i': word,
        'from': 'AUTO',
        'to': 'AUTO',
        'smartresult': 'dict',
        'client': 'fanyideskweb',
        'salt': salt,
        'sign': md5,
        'ts': ts,
        'bv': '6ba427a653365049d202e4d218cbb811',
        'doctype': 'json',
        'version': '2.1',
        'keyfrom': 'fanyi.web',
        'action': 'FY_BY_REALTlME'
    }
    response = requests.post(url, headers=headers, data=data, proxies=proxies)
    data = response.text
    # 返回的是json数据，自行获取翻译
    print(data)
    #print('翻译结果：'+eval(data)['translateResult'][0][0]['tgt'])

url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'

while True:
    woed = input('输入待翻译的内容：')
    youdao(url,woed)
