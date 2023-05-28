import base64
import json
import cohere
import requests
import os


def gen_image():
    r = requests.post(
        "https://api.deepai.org/api/text2img",
        data={
            'text': "show me a cat",
            'grid_size': 1
        },
        headers={
            'api-key': 'quickstart-QUdJIGlzIGNvbWluZy4uLi4K'}
    )
    # image_url = r.json()#['output_url']
    response = f"<Response><Message><Media>{image_url}</Media></Message></Response>"

    print(response)
    return {
        'statusCode': 200,
        'headers': {'Content-Type': 'text/xml'},
        'body': response
    }


print(gen_image())