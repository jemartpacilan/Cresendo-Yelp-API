import time
from flask import Flask
import os
import requests
import json
from yelp.client import Client
# import fer
# import matplotlib.pyplot as plt
MY_API_KEY = os.getenv('API_KEY') #  Replace this with your real API key

client = Client(MY_API_KEY)
app = Flask(__name__)
faceplus = 'pk27jA_cLbl1vl-U-JN3hnkLZBmwk90B'
secret = 'W7ZjnDtspsmqACN-Qa4q-OT-PdqJeYNh'
url = 'https://api.yelp.com/v3/businesses'
faceplus_url = 'https://api-us.faceplusplus.com/facepp/v3/detect'
# API_KEY = xxxx
headers = {'Authorization': f"Bearer {MY_API_KEY}"}
# categories = ['french', 'chinese', 'japanese', 'italian', 'indian']

# for i, category in enumerate(categories):
# params = {'location': location, 'limit': 50, 'categories': category}
# resp = requests.get(url, headers=headers, params=params)
#!/usr/bin/env python3
# from luxand import luxand
# print(client.__dict__)
@app.route('/')
def hello():
    # print(client.get_business('yelp-san-francisco'))
    resp = requests.get(url + '/milwaukee-ale-house-milwaukee', headers=headers)
    # print(resp.json())
    # print(json.loads(resp.text))
    response = json.loads(resp.text)
    reviews = requests.get(url + '/milwaukee-ale-house-milwaukee/reviews', headers=headers)
    # print(json.loads(reviews.text))
    review_resp = json.loads(reviews.text)

    response["reviews"] = review_resp["reviews"]
    params = {
        'api_key': faceplus,
        'api_secret': secret,
        'image_url': 'https://s3-media4.fl.yelpcdn.com/photo/uMk8odkAx_MojVtkzsINGg/o.jpg',
        'return_attributes': 'emotion'
    }
    faceplus_response = requests.post(faceplus_url, params=params)
    face = faceplus_response.json()
    face_emotion = face['faces'][0]['attributes']['emotion']
    print(max(face_emotion, key=face_emotion.get), 'facessplsssusss')
    # client_luxand = luxand("87befaf8009d414d971cd95101cee6c4")

    # result = client_luxand.emotions(photo = "https://s3-media4.fl.yelpcdn.com/photo/uMk8odkAx_MojVtkzsINGg/o.jpg")

    # print(result)
    # return '<h1>jade batignawng</h1>'
    # business_response = client.get_business()
    # return business_response
    # print(client.__dict__)
    return face_emotion
