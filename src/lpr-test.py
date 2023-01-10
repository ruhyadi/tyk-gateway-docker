import requests

headers = {
    'accept': 'application/json',
    'Authorization': 'Basic YWxmYWJldGE6YWxmYWJldGExMjM=',
    'X-Tyk-Authorization': 'foo'
    # requests won't add a boundary if this header is set when you pass files=
    # 'Content-Type': 'multipart/form-data',
}

files = {
    'image': open('src/license_plate.jpg', 'rb'),
    'ipCameraAddress': (None, '1'),
    'engineExternalId': (None, ''),
}

# response = requests.post('http://localhost:8114/lpr-capture', headers=headers, files=files)
response = requests.post('http://localhost:8080/sample/lpr-capture', headers=headers, files=files)

print(response.text)