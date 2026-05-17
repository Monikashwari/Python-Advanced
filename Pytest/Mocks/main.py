import requests

def api_call(url):
    res = requests.get(url)
    return {"Data" : res.json()}