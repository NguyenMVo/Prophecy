import requests, uuid, json, os
from dotenv import load_dotenv

def translate(sentence):
    load_dotenv()
    # Add your subscription key and endpoint
    subscription_key = os.getenv('TRANSLATE_KEY')
    endpoint = os.getenv('TRANSLATE_ENDPOINT')

    # Add your location, also known as region. The default is global.
    # This is required if using a Cognitive Services resource.
    location = os.getenv('REGION')

    path = '/translate'
    constructed_url = endpoint + path

    params = {
        'api-version': '3.0',
        'to': ['vi']
    }
    constructed_url = endpoint + path

    headers = {
        'Ocp-Apim-Subscription-Key': os.getenv('TRANSLATE_KEY'),
        'Ocp-Apim-Subscription-Region': os.getenv('REGION'),
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
    }

    # You can pass more than one object in body.
    body = [{
        'text': sentence
    }]

    request = requests.post(constructed_url, params=params, headers=headers, json=body)
    response = request.json()

    tmp = (json.dumps(response, sort_keys=True, ensure_ascii=False, indent=4, separators=(',', ': ')))
    result = json.loads(tmp)
    #print(result[0]['translations'][-1]['text'],result[0]['translations'][-1]['to'], result[0]['detectedLanguage']['language'])
    return result[0]['translations'][-1]['text']