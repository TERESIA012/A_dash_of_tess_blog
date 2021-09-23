import urllib.request,json
from .models import Quote



def process_request(quote_list):
    """
    function process_request to fetch the API
    """
    quotes=[]
    for quote in quote_list:
        author= quote.get('author')
        quote= quote.get('quote')
        quotes.append(Quote(author, quote))
        return quotes
                          



