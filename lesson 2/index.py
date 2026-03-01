import colorama
from colorama import Fore, Style
from textblob import TextBlob
colorama.init()
print(Fore.CYAN + "welcome to sentiment spy" + Style.RESET_ALL)
name=input(Fore.MAGENTA + "what is your name" + Style.RESET_ALL)
if name == "":
    name = "agent"
print(Fore.CYAN +f"hello agent{name}" + Style.RESET_ALL)
print("type a sentence")
print("commands: history | reset | exit")
history = []
while True:
    user_text =input(Fore.GREEN + ">>" + Style.RESET_ALL)
    if user_text.lower() == "exit":
        print(Fore.BLUE + "Goodbye Agent" + Style.RESET_ALL)
        break
    elif user_text.lower() == "reset":
        history.clear()
        print(Fore.CYAN + "history reset" + Style.RESET_ALL)
        continue
    elif user_text == "history":
        if not history:
            print(Fore.YELLOW + "no history yet" + Style.RESET_ALL)
        else :
            for text, sentiment in history:
                print(text,"->",sentiment)
        continue
    polarity = TextBlob(user_text).sentiment.polarity
    if polarity> 0.25:
        sentiment=Fore.GREEN +"positive 😊"
    elif polarity < -0.25:
        sentiment = Fore.RED + "negative😔"
    else:
        sentiment = Fore.YELLOW +"neutral😑"
    history.append((user_text,sentiment))
    print("sentiment:",sentiment + Style.RESET_ALL)

