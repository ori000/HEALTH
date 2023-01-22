
# returns if theres bad words in the input_text
def BadWordFunction(input_text):

    from MagnetAPIClient import MagnetAPIClient
    import json


    ENDPOINT ='https://nlp.klangoo.com/Service.svc'
    CALK ='1a815cf2-3e45-4de4-a879-b437660d88d8'
    SECRET_KEY ='jtxCz6M0jnqJkvCbhFcuZgyBbzBqga2nVqn2v1qS'

    client = MagnetAPIClient(ENDPOINT, CALK, SECRET_KEY)

    text = input_text

    request = { 'text' : text, 'lang' : 'en', 'format' : 'json' }



    rsp = client.callwebmethod('ProcessSensitiveContent', request, 'POST')

    
    return any([i["name"]!="Others" and i["name"]!="Politics" for i in json.loads(rsp)["categories"]])

# api processes the text
def API_function(input_text):
    from MagnetAPIClient import MagnetAPIClient
    import json




    ENDPOINT ='https://nlp.klangoo.com/Service.svc'
    CALK ='1a815cf2-3e45-4de4-a879-b437660d88d8'
    SECRET_KEY ='jtxCz6M0jnqJkvCbhFcuZgyBbzBqga2nVqn2v1qS'

    client = MagnetAPIClient(ENDPOINT, CALK, SECRET_KEY)

    text = input_text

    request = { 'text' : text, 'lang' : 'en', 'format' : 'json' }



    rsp = client.callwebmethod('ProcessDocument', request, 'POST')

    
    return json.loads(rsp)
