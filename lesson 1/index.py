while True:
    print("\n--- Welcome to the basic chat bot! ---")
    name = input("What is your name? ")
    print("Nice to meet you,", name)
    
    feeling = input("How are you feeling today? ").lower()
    if "good" or "great" or "awesome" in feeling:
        print("That's great to hear!")
    elif "bad" in feeling:
        print("I hope your day gets better.")
    else:
        print("That's alright, sometimes we don't have words to define how we feel.")
    
    hobby = input("What is your favorite hobby? ")
    print(hobby, "sounds fun!")
    print(f"It was nice chatting with you, {name}.")

    
    repeat = input("\nWould you like to start over? (yes/no): ").lower()
    if repeat != "yes":
        print("Goodbye!")
        break 