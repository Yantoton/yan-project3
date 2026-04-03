import requests
page ="https://www.google.com/search?q=give+me+all+python+file+i%2Fo+ducumentation+and+methods&oq=give+me+all+python+file+i%2Fo+ducumentation+and+methods+&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIJCAEQIRgKGKABMgkIAhAhGAoYoAEyCQgDECEYChigATIJCAQQIRgKGKABMgkIBRAhGAoYoAHSAQo2MzIxMmowajE1qAIIsAIB8QVlbyjY_Q-TPQ&sourceid=chrome&ie=UTF-8"
print(page)
response = requests.get(page)
print(response.text)
