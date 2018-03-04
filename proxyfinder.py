import requests
from lxml import html as lh

headers = {'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:56.0) Gecko/20100101 Firefox/56.0'}

req = requests.get('http://www.gatherproxy.com/sockslist', headers=headers, timeout=23)
options = lh.fromstring(req.content)

ips = [op.lstrip().split("'")[-2] for op in options.xpath(".//*[@id='tblproxy']//script/text()")][::2]
portas = [op.lstrip().split("'")[-2] for op in options.xpath(".//*[@id='tblproxy']//script/text()")][1::2]
resp_time = [op for op in options.xpath(".//*[@id='tblproxy']//td[7]/text()")]
for ip, porta, rt in zip(ips, portas, resp_time):
    print(ip + " : " + porta + " : " + rt)
