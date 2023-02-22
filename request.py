import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'Distance':25.40, 'Pressure':1.0, 'HRV':101.396, 'Sugar level':61.080, 'Sp02':87.770})

print(r.json())