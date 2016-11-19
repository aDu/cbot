import http.client, json, api_key

headers = {
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': api_key.TEXT_ANALYSIS,
}

# Returns sentiment between 0 and 1, 1 indicating a positive sentence, 0 indicating negative
def getSentiment(message):
    body = {
      "documents": [
        {
          "language": "en",
          "id": "0",
          "text": message
        }
      ]
    };

    try:
        conn = http.client.HTTPSConnection('westus.api.cognitive.microsoft.com')
        conn.request("POST", "/text/analytics/v2.0/sentiment", json.dumps(body), headers)
        response = conn.getresponse()
        data = json.loads(response.read().decode())
        score = data['documents'][0]['score'];
        conn.close()
        return score;
    except Exception as e: #Error occurred, just assume 0.5 sentiment
        print(e)
        return 0.5;

getSentiment("I hate you")