import requests



    
    
def get_quote():
    """
    Fetches quotes from Api
    """   
    response =requests.get("http://quotes.stormconsultancy.co.uk/random.json")
    if response.status_code==200:
        quote=response.json()
        return quote
        
    
    
    
    
    
    
    
        
        
                          



