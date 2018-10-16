import json

# myDictionary = {"name": "Anne"}
#
# with open("allanswers.json", "w") as outfile:
#     json.dump(myDictionary, outfile)

survey = ["What is your name? ", "What is your programming language? "]

keys = ["name", "language"]

listOfAnswers = []

done = "No"

while done == "No":
    answers = {}

    for x in range(len(survey)):
        response = input(survey[x] + " ")
        answers[keys[x]] = response

        listOfAnswers.append(answers)
        done = input("Are you done with the survey? Yes or No?")

#Open file with all the past results and append them to the current list
f = open("allAnswers.json", "r")
oldData = json.load(f)
listOfAnswers.extend(oldData)
f.close

f = open("allAnswers.json", "w")
f.write("[\n")
index = 0

for j in listOfAnswers:
    if (index < len(listOfAnswers)-1):
        json.dump(j, f)
        f.write("\n")
    else:
        json.dump(j, f)
        f.write("\n")
    index +=1

    f.write("]")
    f.close()
