def response_fetcher(tag):
    import json
    import random

    with open('intents.json', 'r') as json_data:
        intents = json.load(json_data)
    
    response=""
    for intent in intents['intents']:
        if tag==intent["tag"]:
            response+=random.choice(intent["responses"])

    # this means that there is a missing entry in the intents.json file
    if not response:
        return "no response"
    else:
        return response
