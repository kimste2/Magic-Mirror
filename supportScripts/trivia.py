import json
import requests
import html
from bs4 import BeautifulSoup

def getTrivia():
    url = "https://opentdb.com/api.php?amount=10&type=multiple"
    response = requests.get(url)
    if response.status_code == 200:
        jsonString = json.loads(response.text)
    else:
        print("Error with trivial url " + str(response.status_code))


    response_code = jsonString['response_code']
    if response_code != 0:
        print("Error with trivial url, got non zero reponse code " + str(response_code))
    else:
        l = jsonString['results'][0]
        newline = "\n"
        string  = ""
        question = l['question']
        string += question + newline
        correct_answer = l['correct_answer']
        string += correct_answer + newline 
        incorrect_answers = l['incorrect_answers']
        for i in incorrect_answers:
            string += i + newline
            
        cleanText = BeautifulSoup(html.unescape(string), 'lxml')
        return cleanText.text
#getTrivia()
