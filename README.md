# CRESENDO - YELP API

## Description

A simple Flask application which provides an endpoint that retrieves the details and reviews of a specified business/restaurant using the YELP API

## Requirements

To run this application you must install the following:

-   Docker
-   Python 3

## Installation (Project Setup)

First, you need to acquire a YELP API KEY for the yelp api requests to work and Faceplusplus API key and secret from the [Faceplusplus site](https://www.faceplusplus.com/) to be able to identify the emotion of the reviewer's thumbnail.
Furthermore, you need to add the API keys and secret as one of the environment variables of the project in the .env file.

Before running the commands for installation, you need to create a .env file at the root of the project to set the environment variables of the application.

Here's a sample of the .env file for this project

```
YELP_API_KEY=B_k-TmkXiqKop6z-W393dJgbbne7YfNBbKTuqXXcGgSeHH53y0g5qrBi_iupYz5ixRTfI0QnAxFvG0CrXJdgVkG5U2vZg80EbCzcO_vucLg9fdHiu09zF4AMiF6KYHYx
FACEPLUS_KEY=pk27jA_cLbl1vl-U-JN3hnkLZBmwk90B
FACEPLUS_SECRET=W7ZjnDtspsmqACN-Qa4q-OT-PdqJeYNh
```

Alternatively, you can just rename the .env.dev file (found at the root of the project) to .env

### Docker command to set up/build the project:

Build and run the application using:

```
docker-compose up
```

## API Endpoints (sample)

| HTTP verb | Path                                                 |
| --------- | ---------------------------------------------------- |
| GET, POST | /yelp-data?business_id=milwaukee-ale-house-milwaukee |
