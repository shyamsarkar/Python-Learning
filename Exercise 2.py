"""

1. create ID and password for first time, write it to a .dat file
2. first encrypt that password and write to the file
3. login to your account, allows to enter login ID and password
4. encrypt the ID password
5. then compare with your database and, either allow or deny access
"""

# Encrypt all 26 alphabets


# Encrypt all special characters
'''


'''


list_2 = []
dict_cypher = \
{
    '1': 'klrahul',
    '2': 'Dui',
    '3': 'teen',
    '4': 'char',
    '5': 'aronfinch',
    '6': 'chhoy',
    '7': 'kartikermaadhoni',
    '8': 'ravindrajadeja',
    '9': 'noy',
    '0': 'sachintendulkar',
    'a': 'aarea' ,
    'b': 'ollab',
    'c': 'nic',
    'd': 'minded',
    'e': 'walle',
    'f': 'faf',
    'g': 'bing',
    'h': 'booyah',
    'i': 'mini',
    'j': 'georj',
    'k': 'walk',
    'l': 'mill',
    'm': 'gham',
    'n': 'goon',
    'o': 'bolo',
    'p': 'priya',
    'q': 'kwarq',
    'r': 'bimar',
    's': 'minus',
    't': 'amit',
    'u': 'damru',
    'v': 'yadav',
    'w': 'allow',
    'x': 'rolax',
    'y': 'colony',
    'z': 'miraz'
}

def id_enter():
    enter_email_id = input("Enter your Email ID: ")
    email_id = enter_email_id + ".dat"
    return email_id

def pass_enter():
    pass_word = input("Enter your password: ")
    return pass_word

def pass_conform():
    new_pass = input("Confirm password again: ")
    return new_pass



def ac_login():
    check_id = id_enter()
    check_pass = pass_enter()
    check_pass_encrypt = encrypted(check_pass)
    list_5 = []
    for element in check_pass_encrypt:
        for text in element:
            list_5.append(text)
    send_result = False
    try:
        file = open(check_id, "r")
        list_3 = []
        for element2 in file:
            for text2 in element2:
                if text2 != " ":
                    list_3.append(text2)
                else:
                    continue
        file.close()
        if list_5 == list_3:
            send_result = True
        return send_result
    except:
        print("Entered account does not exist.")
        return send_result

def encrypted(original_pass):
    for word1 in original_pass:
        encrypting = dict_cypher[word1]
        list_2.append(encrypting)
    return list_2


def writing_pass():
    file_created = open(id_enter(), "w")
    while True:
        old_pass = pass_enter()
        new_pass = pass_conform()
        if old_pass == new_pass:
            encrypted_pass = encrypted(new_pass)
            for word in encrypted_pass:
                file_created.write(word)
                file_created.write(" ")
            break
        elif old_pass == 'quit' or old_pass == 'exit':
            break
        else:
            print("Password did not match!. If you want to quit then type quit")
    file_created.close()



primary_question = input("Login(L),Create account(C),Change password(R),Q to quit.")
if primary_question == 'l' or primary_question == 'L':
    login = ac_login()
    if login:
        print("Login Successful.")

    else:
        print("Incorrect Password.")
elif primary_question == 'c' or primary_question == 'C':
    print("Enter quit or exit to quit ")
    writing_pass()
elif primary_question == 'r' or primary_question == 'R':
    re_check = input("Do you want to continue? (Y or N) : ")
    if re_check == 'y' or re_check == 'Y':
        login = ac_login()
        if login:
            print("login successful. now you can change password.")
            writing_pass()
        else:
            print("please, login first!")

elif primary_question == 'q' or primary_question == 'Q':
    exit(0)
else:
    print("Wrong input!. Please enter a valid input.")