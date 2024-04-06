import requests
import re

target_url = 'https://jsy.dog/Help/Tutorial.html#ios-tab'
urls = []
html = requests.get(target_url).text
matches = re.findall(r'<object[^>]+data="(.*?)"[^>]*>', html, re.I)
for match in matches:
    urls.append(match)

res = []
for url in urls:
    html = requests.get(url).text
    result = re.findall(r'data-clipboard-text="(.*?)">复制', html, re.I)
    rrr = f"账号：{result[0]}\n密码：{result[1]}"
    res.append(rrr)
ppp = '\n\n'.join(res)
print(ppp)
