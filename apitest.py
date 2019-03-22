import requests
import json

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}
word = input('请输入你要翻译的中文：')
url = 'http://fanyi.youdao.com/translate?&doctype=json&type=AUTO&i={}'.format(word)
res = requests.get(url,headers=headers)
json_data = json.loads(res.text)

print(json_data)
print(json_data.get("translateResult")[0][0].get("tgt"))
