import urllib.request,json
from .models import Quote



def process_requests(quote_list):
    """
    function process_request to fetch the API
    """
    quotes=[]
    for quote in quote_list:
        author= quote.get('author')
        quote= quote.get('quote')
        quotes.append(Quote(author, quote))
        return quotes
    
    
def get_quote():
    """
    Fetches quotes from Api
    """   
    url = "http://quotes.stormconsultancy.co.uk/quotes/25"
    with urllib.request.urlopen(url) as response:
        quote_list= json.loads(response.read)
        return process_requests(quote_list)
    
    
    
    
    
    
    
        
        
                          



