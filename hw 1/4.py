x=input("Input a letter of the alphabet: ")
if ord(x)==97 or ord(x)==101 or ord(x)==105 or ord(x)==111 or (x)==117 or ord(x)==121:
    print(x, end=" is a vowel")
else:
    print(x, end=" is a consonant")