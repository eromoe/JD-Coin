# import pytesseract
# from PIL import Image
# import baidu

# token = baidu.getToken()
# print(token)

# # image.show()
# #需要配置下载文件
# result = pytesseract.image_to_string(image, lang="chi_sim")
# print(result)

from aip import AipOcr
from PIL import Image
import base64
from io import BytesIO

""" 你的 APPID AK SK  图2的内容"""

APP_ID = "18037773"
API_KEY = "opPSLkjXliSrYXfrKizsFGiC"
SECRET_KEY = "tfXgvzAcGXoasQmnoRvElWBPRsleOFbg"
client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

options = {}
options["language_type"] = "CHN_ENG"
options["detect_direction"] = "true"
options["detect_language"] = "true"
options["probability"] = "true"


def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()


image_path = 'weread/image/test.jpeg'
image = Image.open(image_path)
buffered = BytesIO()
image.save(buffered, format="jpeg")

""" 带参数调用通用文字识别, 图片参数为本地图片 """
result = client.basicGeneral(buffered.getvalue(), options)
print(result)
