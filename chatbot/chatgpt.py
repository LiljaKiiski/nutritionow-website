import http.client
import json
import time

conn = http.client.HTTPSConnection("chatgpt-api.shn.hk")
headers = { 'Content-Type': "application/json" }
with open("intents2.json") as f:
    end = json.load(f)
    
# end = {"intents": []}

with open("FoodQandA.json", 'r') as f:
    intents = json.load(f) 
c = 1
for intent in intents['intents']:
    print(c)
    if c < 19:
        c += 1
        continue
    string = intent['patterns'][0]
    message = "Rewrite the question " + string + " 30 times with varying levels of conciseness and varying levels of generalization, don't number each question, separate each question with a comma"
    payload = "{\"model\": \"gpt-3.5-turbo\",\"messages\": [{\"role\": \"user\", \"content\": \"" + message + "\"}]}"
    conn.request("POST", "/v1/", payload, headers)
    res = conn.getresponse()
    data = json.loads(res.read())
    # print(data)
    ans = data['choices'][0]['message']['content'].replace("\n\n","").replace("\n","$<3$").split("$<3$")
    ans.append(string)
    if len(ans) < 25:
        print("help: " + str(c))
    tmp = {}
    tmp["tag"] = intent['tag']
    # print(ans)
    tmp["patterns"] = ans
    # print(tmp["patterns"])
    tmp["responses"] = [intent['responses']]
    tmp["context_set"] = ""
    end["intents"].append(tmp)
    # print(end)
    # break
    c += 1
    obj = json.dumps(end)
    with open("intents2.json", "w") as f:
        f.write(obj)
    time.sleep(10)



# {'id': 'chatcmpl-6uQZcJbIXh89i6dgjxWZGmw4t0iJ7', 'object': 'chat.completion', 'created': 1678906536, 'model': 'gpt-3.5-turbo-0301', 'usage': {'prompt_tokens': 35, 'completion_tokens': 132, 'total_tokens': 167}, 'choices': [{'message': {'role': 'assistant', 'content': "\n\nWhat is the suggested daily caloric intake for a typical adult? \nWhat's the standard calorie recommendation for an average adult? \nWhat's the advised calorie intake for a regular adult? \nHow much calories are recommended on a daily basis for the average adult? \nFor an average adult, what's the daily advised calorie intake? \nWhat quantity of daily calories are recommended for an ordinary adult? \nWhat's the typical caloric recommendation for a regular adult? \nWhat's the everyday adult's advised daily calorie intake? \nWhat's the standard every day caloric intake for an average adult? \nWhat is a regular adult's suggested daily calorie intake?"}, 'finish_reason': 'stop', 'index': 0}]}