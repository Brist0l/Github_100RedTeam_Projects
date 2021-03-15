import string


def encrypt():
    sentence = input("Enter ur text:").upper()
    shift = 13
    letters = string.ascii_uppercase
    dictionary = dict(zip(range(26), letters))
    # print(dictionary)
    cipher = ""
    for words in sentence:
        try:
            if words == " ":
                cipher += " "
            else:
                a = letters.index(words)
                text = (a + shift) % 26
                x = dictionary[text]
                cipher += x
        except:
            print("error :(")
            break
    print(cipher.lower())


def decrypt():
    # def BruteForce():
    # sentence = input("Enter the text U want to decrypt:").upper()
    # letters = string.ascii_uppercase
    # dictionary = dict(zip(range(26), letters))
    # cipher = ""
    # for words in sentence:
    #     a = letters.index(words)
    #     for y in range(25):
    #         text = (a - y) % 26
    #         x = dictionary[text]
    #         cipher += x
    #     print(f"{cipher.lower()}\n")

    def shift():
        sentence = input("Enter the text U want to decrypt:").upper()
        shift = int(input("no. of shifts?:"))
        letters = string.ascii_uppercase
        dictionary = dict(zip(range(26), letters))
        cipher = ""
        for words in sentence:
            try:
                if words == " ":
                    cipher += " "
                else:
                    a = letters.index(words)
                    text = (a - shift) % 26
                    x = dictionary[text]
                    cipher += x
            except:
                print("error :(")
                break
        print(cipher.lower())

    choice = input("Do u know the no. of shifts of BRUTEFORCE(S,B)>")
    if choice == 's':
        shift()
    elif choice == 'b':
        #BruteForce()
        pass
    else:
        print("wrong option")


choice = input("Encrypt Or Decrypt A ROT13 Cipher(E,D)>")
choice = choice.upper()
if choice == 'E':
    encrypt()
elif choice == 'D':
    decrypt()
else:
    print("Not A Valid Command 'type 'E' or 'd' ' :( ")
