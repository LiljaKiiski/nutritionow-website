import json
from bs4 import BeautifulSoup
import pyperclip

with open("intents2.json") as f:
    end = json.load(f)
    
# end = {"intents": []}

with open("FoodQandA.json", 'r') as f:
    intents = json.load(f) 
c = 1
for intent in intents['intents']:
    print(c)
    if c < 34:
        c += 1
        continue
    string = intent['patterns'][0]
    message = "Rewrite the question \"" + string + "\" 30 times with varying levels of conciseness and varying levels of specificity and varying lengths, don't number each question, separate each question with a comma"
    pyperclip.copy(message)
    print("Copied!")
    input("Enter to parse -> ")
    soup = BeautifulSoup(pyperclip.paste(), "html.parser")
    ans = soup.get_text().replace("\n","").replace("?","?<3").split("<3")
    ans[-1] = string
    print(ans)
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
    input("Enter to continue -> ")
    with open("intents2.json", "w") as f:
        f.write(obj)

