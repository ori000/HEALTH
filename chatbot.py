def chatbot(text):
    from helper_api_functions import API_function
    from helper_api_functions import BadWordFunction
    from response_fetcher import response_fetcher

    import json
    import random

    if text.endswith("?"):
        text=text[:-1]
    text=text.lower()


    tag=""

    # check for bad words, for some reason it detects this as bad: "what types of appointments do you have?"
    if(BadWordFunction(text) and "appointments" not in text and "appointment" not in text and "type" not in text and "prices" not in text):
        return "Don't Discuss Sensitive Content"
    else:
    # check if text is only letters and spaces
        lst=text.split()
        only_letters=True
        for i in lst:
            only_letters= only_letters and i.isalpha();
        if(only_letters):
            # api didnt understand
            if API_function(text)["document"]["keyTopics"]==[]:

                tag="didn't_understand"
                return response_fetcher(tag)
        
            else:
              
                #if API_function(text)["document"]["keyTopics"][0]["words"][0]["token"]=="appointment":
                    #print("sure, you can book an appointment by clicking this link: LINK")
                    response=""
                    token=[topic["words"][0]["token"] for topic in API_function(text)["document"]["keyTopics"]]
                                    
                    if("price" in token or "prices" in token):
                        tag="price"
                        response+=response_fetcher(tag)+"\n"

                    if(("type" in token or "types" in token) and ("appointment" in token or "appointments" in token)):
                        tag="typesofappointments"
                        response+=response_fetcher(tag)+"\n"
                    if("appointment" in token):
                        tag="appointment"
                        response+=response_fetcher(tag)+"\n"
                    if("discount" in token or "discounts" in token):
                        tag="discount"
                        response+=response_fetcher(tag)+"\n"
                #return "I understood what you want but i dont know how to response"

                    return response
                
            

        else:
            tag="only_letters"
            return response_fetcher(tag)
        
        
