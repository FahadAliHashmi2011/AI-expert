print("Welcome to the basic chat bot!")
name = input("what is your name? ")
print("Nice to meet you",name)
feeling = input ("how are you feeling today? ").lower()
if "good" in feeling:
    print("thats great to hear")
elif "bad" in feeling:
    print("i hope your day gets better")
else:
    print("Thats alright ,sometimes we dont have words to define how we feel")
hobby = input("what is your favorite hobby? ")
print(hobby,"sounds fun!")
print(f"it was nice chating with you {name}")