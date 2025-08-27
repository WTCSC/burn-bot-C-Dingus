NEGATIVE = ["no", "nah", "nope", "not really"];
POSITIVE = ["yes", "yea", "ye", "sure", "i guess"];

#get input from user
def ask_for_data():
    print("what is your name, age, and favourite sport?");
    user_input = input();
    return user_input.lower().split(', ');

#gets the users personal information and checks that age is a valid number
while True:
    words = ask_for_data();
    if len(words) < 2:
        print("some one is witholding information try again");
    else:
        try:
            int(words[1]);
            break;
        except:
            print("age is invalid number")
        



#converts data to dictionary
data = {
    'name':words[0],
    'age':words[1],
    'sport':words[2]
}


#checks if name has been read before
try:
    #try open file of user
    with open(f"{data['name']}.what", "r") as file:
        print(f"{data['name']}?");

        #read the file and compare to input data
        ud = file.read().split("'");
        if int(ud[7]) != int(data['age']):
            print(f"so your telling me you grew {int(data['age']) - int(ud[7])} years? sure guy");
            if ud[11] != data['sport']:
                print("well at least your sports prefrences have ... changed");
            else:
                print("and you still feel the same about sports? i see");
        else:
            if ud[11] != data['sport']:
                print("I see your sports prefrences have changed but your age hasn't");
            else:
                print("why are you back? you haven't grown at all")



except:
    #read and judge input data
    if int(data['age']) <= 10:
        print(f"{data['age']} yea i can see that");
    elif int(data['age']) >= 25:
        print(f"someone as old as {data['age']} should act a bit more mature dont you think?")
    else:
        print(f"so your {data['age']} wow i bet your humor is great");
        i = input();
        if i.lower() in NEGATIVE:
            print("yea thats what i thought");
        elif i.lower() in POSITIVE:
            print("sure pal");
        else:
            print("...");

    print("anyways as for you favourite sport");
    match data['sport']:
        case "golf":
            if int(data['age']) >= 50:
                print(f"wow golf; you really are {data['age']}");
            else:
                print(f"why golf you not 50 yet");
        case "soccer":
            print("soccer? good luck with that your going to need it if you call it soccer");
        case "football":
            print("american football or football football?");
            i = input();
            if i == "american" or i == "american football":
                print("why?")
            elif i == "real" or i == "football" or i == "football football":
                print("wow your so different your not like other americans you call soccer football");
        case "basketball":
            print("wow basketball hope you got good genetics to play that but i doubt that");
        case _ :
            print(f"{data['sport']}? ... ok sure")

#save data to file
with open(f"{data['name']}.what", "w") as file:
    file.write(f"{data}")

print("alright get out of here");
