import http.client, json, nltk, pprint
from nltk.draw.tree import draw_trees

headers = {
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': 'd88ce6da475e45e382cebcaccd9abbd3',
}

# Returns you the list of analysers that can be used by the Linguistic Analyser
def getAnalyzers():
    try:
        conn = http.client.HTTPSConnection('api.projectoxford.ai')
        conn.request("GET", "/linguistics/v1.0/analyzers", "{}", headers)
        response = conn.getresponse()
        data = json.loads(response.read().decode())
        conn.close()
        #print(data)
        return data;
    except Exception as e:
        print(e)
        return False;

pprint.pprint(getAnalyzers())
