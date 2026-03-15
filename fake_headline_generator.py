#1- import the random module
import random

#2-create subjects
subjects=[
    "Shahrukh khan",
    "Virat kohli",
    "Nirmala Sitaraman",
    "A Mumbai Cat",
    "A Group of Monkeys",
    "Prime Minister MOdi",
"Auto Rickshaw Driver from Delhi"
]

actions=[
    "launches",
    "cancels",
    "dances with",
    "eats",
    "declares war on ",
    "orders",
    "celebrates"

]

places_or_things=[
    "at Red Fort",
    "in MUmbai Local Train",
    "a plate of Samosa",
    "inside parliament",
    "at Ganga Ghat",
    "during IPL match",
    "at India Gate"
]

#3- Start the headline generation loop
while True:
    subject=random.choice(subjects)
    action = random.choice(actions)
    place_or_thing = random.choice(places_or_things)

    headline=f" BREAKING NEWS: {subject} {action} {place_or_thing}"
    print("\n" + headline)

    user_input=input("\n Do you want another headline? (yes/no)").strip().lower()
    if user_input== "no":
        break
#print goodbye message
print("\n Thanks for using the Fake News Headline Generator . Have a fun day ")    
