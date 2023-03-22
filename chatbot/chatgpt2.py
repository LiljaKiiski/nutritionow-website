from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import json
# from webdriver_manager.chrome import ChromeDriverManager
import undetected_chromedriver as uc
driver = uc.Chrome()

with open("intents2.json") as f:
    end = json.load(f)
with open("FoodQandA.json", 'r') as f:
    intents = json.load(f) 

# Set up the webdriver

# driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://chat.openai.com/chat")
input("Waiting for go signal --> ")
# Find the input field and enter a prompt
c = 1
for intent in intents['intents']:
    print(c)
    if c < 19:
        c += 1
        continue
    string = intent['patterns'][0]
    message = "Rewrite the question \"" + string + "\" 30 times with varying levels of conciseness and varying levels of generalization, don't number each question, separate each question with a comma"
    input_field = driver.find_element(By.CSS_SELECTOR, "#__next > div.overflow-hidden.w-full.h-full.relative > div.flex.h-full.flex-1.flex-col.md\:pl-\[260px\] > main > div.absolute.bottom-0.left-0.w-full.border-t.md\:border-t-0.dark\:border-white\/20.md\:border-transparent.md\:dark\:border-transparent.md\:bg-vert-light-gradient.bg-white.dark\:bg-gray-800.md\:\!bg-transparent.dark\:md\:bg-vert-dark-gradient.pt-2 > form > div > div.flex.flex-col.w-full.py-2.flex-grow.md\:py-3.md\:pl-4.relative.border.border-black\/10.bg-white.dark\:border-gray-900\/50.dark\:text-white.dark\:bg-gray-700.rounded-md.shadow-\[0_0_10px_rgba\(0\,0\,0\,0\.10\)\].dark\:shadow-\[0_0_15px_rgba\(0\,0\,0\,0\.10\)\] > textarea")
    # input_field = driver.find_element_by_css_selector("#__next > div.overflow-hidden.w-full.h-full.relative > div.flex.h-full.flex-1.flex-col.md\:pl-\[260px\] > main > div.absolute.bottom-0.left-0.w-full.border-t.md\:border-t-0.dark\:border-white\/20.md\:border-transparent.md\:dark\:border-transparent.md\:bg-vert-light-gradient.bg-white.dark\:bg-gray-800.md\:\!bg-transparent.dark\:md\:bg-vert-dark-gradient.pt-2 > form > div > div.flex.flex-col.w-full.py-2.flex-grow.md\:py-3.md\:pl-4.relative.border.border-black\/10.bg-white.dark\:border-gray-900\/50.dark\:text-white.dark\:bg-gray-700.rounded-md.shadow-\[0_0_10px_rgba\(0\,0\,0\,0\.10\)\].dark\:shadow-\[0_0_15px_rgba\(0\,0\,0\,0\.10\)\] > textarea")
    input_field.send_keys(message)
    
    # Submit the form
    submit_button = driver.find_element(By.CSS_SELECTOR, "#__next > div.overflow-hidden.w-full.h-full.relative > div.flex.h-full.flex-1.flex-col.md\:pl-\[260px\] > main > div.absolute.bottom-0.left-0.w-full.border-t.md\:border-t-0.dark\:border-white\/20.md\:border-transparent.md\:dark\:border-transparent.md\:bg-vert-light-gradient.bg-white.dark\:bg-gray-800.md\:\!bg-transparent.dark\:md\:bg-vert-dark-gradient.pt-2 > form > div > div.flex.flex-col.w-full.py-2.flex-grow.md\:py-3.md\:pl-4.relative.border.border-black\/10.bg-white.dark\:border-gray-900\/50.dark\:text-white.dark\:bg-gray-700.rounded-md.shadow-\[0_0_10px_rgba\(0\,0\,0\,0\.10\)\].dark\:shadow-\[0_0_15px_rgba\(0\,0\,0\,0\.10\)\] > button")
    # submit_button = driver.find_element_by_css_selector("#__next > div.overflow-hidden.w-full.h-full.relative > div.flex.h-full.flex-1.flex-col.md\:pl-\[260px\] > main > div.absolute.bottom-0.left-0.w-full.border-t.md\:border-t-0.dark\:border-white\/20.md\:border-transparent.md\:dark\:border-transparent.md\:bg-vert-light-gradient.bg-white.dark\:bg-gray-800.md\:\!bg-transparent.dark\:md\:bg-vert-dark-gradient.pt-2 > form > div > div.flex.flex-col.w-full.py-2.flex-grow.md\:py-3.md\:pl-4.relative.border.border-black\/10.bg-white.dark\:border-gray-900\/50.dark\:text-white.dark\:bg-gray-700.rounded-md.shadow-\[0_0_10px_rgba\(0\,0\,0\,0\.10\)\].dark\:shadow-\[0_0_15px_rgba\(0\,0\,0\,0\.10\)\] > button")
    submit_button.click()

    # Wait for the page to load
    input()
    
    # Get the page source
    page_source = driver.page_source

    # Use BeautifulSoup to parse the page source and extract the result
    soup = BeautifulSoup(page_source, "html.parser")
    print(soup)
    result = soup.findAll("div", {"class": "markdown prose w-full break-words dark:prose-invert dark"})

    # Print out the result
    print(result)

    # print(data)
    # ans.append(string)
    # if len(ans) < 25:
    #     print("help: " + str(c))
    # tmp = {}
    # tmp["tag"] = intent['tag']
    # # print(ans)
    # tmp["patterns"] = ans
    # # print(tmp["patterns"])
    # tmp["responses"] = [intent['responses']]
    # tmp["context_set"] = ""
    # end["intents"].append(tmp)
    # # print(end)
    # # break
    # c += 1
    # obj = json.dumps(end)
    # with open("intents2.json", "w") as f:
    #     f.write(obj)
    # time.sleep(10)



# Close the webdriver
driver.quit()
