import urllib.request
import xml.dom.minidom

encodingKey = "{q6hOrIt1rP4rcR%2Fyz6vYxwaIPvj5QqJfDluLk%2BqmryiW9NmC6Q5tsW7Ymh2FJ0MZpFVgf8732NKCptcbVIaEMQ%3D%3D}"
decodingKey = "{q6hOrIt1rP4rcR/yz6vYxwaIPvj5QqJfDluLk+qmryiW9NmC6Q5tsW7Ymh2FJ0MZpFVgf8732NKCptcbVIaEMQ==}"

print("[START]")

# request url정의
url = "http://apis.data.go.kr/B553881/Parking/PrkOprInfo?ServiceKey=" + encodingKey + "&numOfRows=10&pageNo=1&format=2"
request = urllib.request.Request(url)

# request보내기
response = urllib.request.urlopen(request)

# 결과 코드 정의
rescode = response.getcode()

if(rescode==200):
    response_body = response.read()
    dom = xml.dom.minidom.parseString(response_body.decode('utf-8'))
    pretty_xml_as_string = dom.toprettyxml()
    print(pretty_xml_as_string)
else:
    print("Error Code:" + rescode)

print("[END]")