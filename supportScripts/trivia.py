import json
import requests
import html
from bs4 import BeautifulSoup
import random

l = ""
string = ""
url = "https://opentdb.com/api.php?amount=10&type=multiple"
response = requests.get(url)

if response.status_code == 200:
    jsonString = json.loads(response.text)
else:
    print("Error with trivia url " + str(response.status_code) + " exit(1)")
    exit(1)

response_code = jsonString['response_code']

if response_code != 0:
    print("Error with trivial url, got non zero reponse code " + str(response_code))
    exit(1)
else:
    l = jsonString['results'][0]
    
     
    question = l['question']
    cleanText = BeautifulSoup(html.unescape(question), 'lxml')
    cleanQuestion = cleanText.text.strip()

    possible_Answers = []  
    correctAnswer = l['correct_answer']
    possible_Answers.append(correctAnswer.strip())
    
    for i in l['incorrect_answers']:
    	possible_Answers.append(i.strip())
        
    

    string = ""
    for p in possible_Answers:
         string += str(p) + ","
            
    cleanText = BeautifulSoup(html.unescape(string), 'lxml')
    cleanAnswers = cleanText.text.rstrip()
    cleanAnswers.strip()
    lst = cleanAnswers.split(",", 3);
    random.shuffle(lst)
    dct = {}
    
    emptyString = ""
    for l in lst:
        if l == correctAnswer:
            dct['correct'] = l.replace(',','').rstrip()
        else:
            dct['incorrect' + str(lst.index(l))] = l.replace(',','').rstrip()
             
def getQuestion():        
    return cleanQuestion
 
def getAnswers():
    return dct
