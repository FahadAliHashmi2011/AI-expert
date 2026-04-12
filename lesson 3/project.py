import random 
from colorama import Fore,init
init(autoreset=True)
destinations = {
    "beach" : ["bali","maldives","phuket"],
    "mountain" :["swiss alps","rocky mountains","himalayas"],
    "city" :["tokyo","paris","new york"]
}
print(Fore.CYAN+"hello ! i am travel bot")
name = input(Fore.YELLOW +"what is your name ?")
print(Fore.GREEN +"nice to meet you " + name)

while True :
    print(Fore.CYAN + "\nWhat do you want ?")
    print(Fore.GREEN + "1.travel suggestion")
    print(Fore.GREEN + "2.packing tips")
    print(Fore.GREEN + "3. joke")
    print(Fore.GREEN + "4. weather")
    print(Fore.GREEN + "5.time zones")
    print(Fore.GREEN + "6.exit")
   
    choice = input(Fore.YELLOW + "enter from 1,2,3 or 4")
    if choice == "1":
        place_type = input(Fore.YELLOW + "do like beack mountain or city ?").lower()
         
        if place_type in destinations:
            suggestion = random.choice(destinations[place_type])
            print(Fore.GREEN + "you can visit" + suggestion)
        else:
            print(Fore.RED +"sorry the only locationms i know are beach city and mountain")
    elif choice == "2":
        place= input(Fore.YELLOW + "where are you going ?" )
        days = input(Fore.YELLOW +"how many days will you stay ?")
        print(Fore.GREEN + "Packing tips for " + place + ":")
        print(Fore.GREEN + "- Pack enough clothes for " + days + " days")
        print(Fore.GREEN + "- Bring your charger")
        print(Fore.GREEN + "- Carry important documents")
    elif choice == "3" :
        jokes=[
            "why dont programmers like nature? too many bugs!",
            "why did the computer go the doctor ? because it had a virus",
            "why do travcelers always feel warm? because of theeir hotspots",
        ]
        print(Fore.MAGENTA +random.choice(jokes))
    
    elif choice == "4":
        weather_suggestion = [
                           "today is very hot so you shoud use sunscreen,sunglasses and an umbrella",
                           "today is quite cold so you should dress with warmer clothes and wear a hat",
                           "today the weather is clear so not much is neccessary just a light jacket ",
                          ]
        print(Fore.MAGENTA +random.choice(weather_suggestion))
    
    elif choice == "5":
        time_zones = [
                     "did you know tokyo is  around 8 - 9 hours ahead of us in the uk",
                     "uk is actually ahead of usa by around 5 - 8 hours depending  on the location        "
        ]
        print(Fore.MAGENTA +random.choice(time_zones))



    elif choice== "6":
        print(Fore.CYAN +"goobye and safe travels!")
    else:
        print(Fore.RED + " enterr valid option")