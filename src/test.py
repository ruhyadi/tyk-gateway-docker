import requests

url = "http://localhost:8080/sample/sample"
# url = "http://localhost:8114/sample/"
# url = "http://localhost:8001/alfabeta/"

payload={}
headers = {
  'Authorization': 'foo',
  'X-Tyk-Authorization': 'foo'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
