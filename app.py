import time
import os
import requests
import json
from flask import Flask, request
from yelp.client import Client


app = Flask(__name__)

YELP_REQUEST_URL = 'https://api.yelp.com/v3/businesses/'
YELP_REQUEST_HEADERS = {'Authorization': f"Bearer {os.getenv('YELP_API_KEY')}"}
FACEPLUS_REQUEST_URL = 'https://api-us.faceplusplus.com/facepp/v3/detect'

@app.route('/yelp-data', methods=['POST', 'GET'])
def yelp_data():
    """
        Endpoint for retrieving the business/restaurant details and reviews using the YELP API
    """
    # Get query string params
    business_id = request.args.get('business_id')

    try:
        # Get business/restaurant data
        business_data_response = requests.get(YELP_REQUEST_URL + business_id, headers=YELP_REQUEST_HEADERS)
        business_data = json.loads(business_data_response.text)
    except requests.exceptions.RequestException as e:
        return 'Failed to get business data'
    
    try:
        # Get reviews of the restaurant/business
        reviews_response = requests.get(YELP_REQUEST_URL + business_id + '/reviews', headers=YELP_REQUEST_HEADERS)
        business_reviews = json.loads(reviews_response.text)
    except requests.exceptions.RequestException as e:
        return 'Failed to get business reviews data'

    for review in business_reviews['reviews']:
        params = {
            'api_key': os.getenv('FACEPLUS_KEY'),
            'api_secret': os.getenv('FACEPLUS_SECRET'),
            'image_url': review['user']['image_url'],
            'return_attributes': 'emotion'
        }
        try:
            # Identify emotion of the reviewer based on the thumbnail
            faceplus_response = requests.post(FACEPLUS_REQUEST_URL, params=params)
            face = faceplus_response.json()
            face_emotion = face['faces'][0]['attributes']['emotion']
            review['user']['emotion'] = max(face_emotion, key=face_emotion.get)
        except requests.exceptions.RequestException as e:
            return 'Failed to process the emotion of the image'

    business_data["reviews"] = business_reviews["reviews"]

    with open(business_id + '.json', 'w') as f:
        json.dump(business_data, f, ensure_ascii=False)

    return business_data
