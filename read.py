from aip import AipSpeech

APP_ID = "15808152"
API_KEY = "xVf65zq0A6oKvxa4Xc97ooyf"
SECRET_KEY = "znKwPhd1tuuHdQxoRnxoZyBdKSFLwHf6"

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)


def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()


result = client.synthesis(get_file_content('凡人修仙之仙界篇/仙界篇外传一.txt'), 'zh', 1, {
    'vol': 8, # 音量
    'spd': 6, # 语速
    'pit': 7, # 语调
    'per': 4, # 音色
})

with open("仙界篇外传一.mp3", "wb") as f:
    f.write(result)
