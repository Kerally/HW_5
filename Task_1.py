import requests
import pprint


URL = 'https://script.google.com/macros/s/AKfycbzJxqVchgHcGpkv9L6FwSEKERUZ2ECi19vh-RkvcizwobfF6j57RHiRtn8TYInB_NgIcA/exec'

def get_data(URL):
    response = requests.get(URL)
    data = response.json() 
    return data


pprint.pprint(get_data(URL))