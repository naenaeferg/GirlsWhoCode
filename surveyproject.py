import json
answers = {}
list = []
   
questions= ["what is your name?", "How old are you?", "what's your favorite food?",
            "favorite sport?", "favorite color?", "favorite school subject?"]

data = ['name', 'age', 'food', 'sport', "color", "subject"]
collection = "yes"

while collection == "yes":
    for i in range(len(questions)):
        answers[data[i]]=input(questions[i])


    print(answers)

    list.append(answers)

    collection = input("do you want to continue collecting?")

    # reads in from a json file, r for read

with open('data.json', 'r')as mydataFile:
    list2 = json.load(mydataFile)

with open('data.json', 'w')as mydataFile:
    print(list)
    # adds new survey to existing surveys stored in json file
    list2.extend(list) # only works if it is LIST of DICTIONARY
    # print(list)
    json.dump(list2, mydataFile)

with open('data.json', 'r')as mydataFile:
    list2 = json.load(mydataFile)
    

    count_of_people= len(list2)
    print("number of answers", count_of_people)
    print(list2 [0] ["age"])
total=0
for i in list2:
    if 
    total+= int(i["age"])
    
print (total/count_of_people)

    
    



