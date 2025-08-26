#get input from user
def ask_for_data():
    print("what is your name, age, purpose in this world, and your hobby?");
    user_input = input();
    return user_input.split(', ');

#gets the users personal information
while True:
    words = ask_for_data();
    if len(words) < 3:
        print("some one is witholding information try again");
        words = ask_for_data();
    else:
        break;


print(words);
