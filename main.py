NEGATIVE = ["no", "nah", "nope", "not really"];
POSITIVE = ["yes", "yea", "ye", "sure", "i guess"];

#get input from user
def ask_for_data():
    print("what is your name, age, purpose in this world, and your hobby?");
    user_input = input();
    return user_input.lower().split(', ');

#gets the users personal information
while True:
    words = ask_for_data();
    if len(words) < 3:
        print("some one is witholding information try again");
        words = ask_for_data();
    else:
        break;

data = {
    'name':words[0],
    'age':words[1],
    'purpose':words[2],
    'hobby':words[3]
}

if int(data['age']) <= 10:
    print(format("yea i can see that"));
elif int(data['age']) >= 25:
    print("someone as old as you should act a bit more mature dont you think?")
else:
    print(format("so your{data['age']} hmmm is your humor terrible?"));
    i = input();
    if i.lower() in NEGATIVE:
        print("sure pal");
    elif i.lower() in POSITIVE:
        print("yea thats what i expected")
    else:
        print("what? ehh whatevere");