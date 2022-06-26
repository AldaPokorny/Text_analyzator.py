"""
Text_analyzator.py: první projekt do Engeto Online Python Akademie
author: Aleš Pokorný
email: ales.po@seznam.cz
discord: Aleš P.#1775
"""


# vytvoření proměných
registered_users = {"bob": "123", "ann": "pass123", "mike": "password123", "liz": "pass123"}
separator = "-" * 45

# zadané texty
text_1 = """
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley.
"""

text_2 = """
At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.
"""

text_3 = """
The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.
"""

texts = [text_1, text_2, text_3]

# vyžádání údajů od uživatele
username = input("Enter user name: ")
password = input("Enter user password: ")

# zjištění správností údajů
if password == registered_users.get(username):
    print(separator)
    print(f"""Welcome to the app, {username}
We have 3 texts to be analyzed.""")
    print(separator)
else:
    print("Unregistered user, terminating the program!")
    quit()

# výběr textu od uživatele
choose_text = input("Enter a number between 1 and 3 to select: ")
if choose_text.isalpha():
    print("Input is not inteeger!")
    quit()
elif int(choose_text) < 1 or int(choose_text) > 3:
    print("Number is out of range!")
    quit()
else:
    print(separator)

selected_text = texts[int(choose_text)-1]

# vyčištění textu pro následné zpracování
clear_words = []
count = 0
for words in selected_text.split():
    clear_words.append(words.strip(",.()"))
    count = count + 1
print("There are", count, "words in the selected text.")

# statistika slov pro vybraný text
titlecase_words = []
lowercase_words = []
uppercase_words = []
alpha_words = []

for words in clear_words:
    if words.istitle():
        titlecase_words.append(words)
    elif words.isupper():
        uppercase_words.append(words)
    elif words.islower():
        lowercase_words.append(words)
    else:
        words.isdigit()
        alpha_words.append(words)


print("There are", len(titlecase_words), " titlecase words.")
print("There are", len(lowercase_words), " lowercase words.")
print("There are", len(uppercase_words), " uppercase words.")
print("There are", len(alpha_words), " numeric strings.")

# výpočet sumy čísel v textu
summary = 0
for i in range(0, len(alpha_words)):
    alpha_words[i] = int(alpha_words[i])
    summary = summary + alpha_words[i]

print("The sum of all the numbers: ", summary)
print(separator)


# graf výskytů slov v závisloti na jejich délce
occurences = []
for idx, elements in enumerate(clear_words):
    occurences.append(len(elements))

print("LEN", "|", "OCCURENCES".center(max(occurences)+(len("occurences")-2)),
    "| ", "NR.")
print(separator)

for i in range(1, max(occurences) + 1):
    if i < 10:
        print(" ", i, "| ", "*" * occurences.count(i),
              " " * ((max(occurences) + 5) - occurences.count(i)),
              " |", occurences.count(i))
    else:
        print("", i, "| ", "*" * occurences.count(i),
              " " * ((max(occurences) + 5) - occurences.count(i)),
              " |", occurences.count(i))
