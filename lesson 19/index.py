import requests
def get_random_joke():
    url = "https://official-joke-api.appspot.com/random_joke"
    response =requests.get(url)
    
    if response.status_code == 200:
        print(f"Full JSON Response :{response.json()}")
        joke_data = response.json()
        return f"\n{joke_data["setup"]} - {joke_data["punchline"]}"
    else:
        return " failed to get joke"
    
def main():
    print("welcome to the random joke generator!")

    while True:
        User_input = input("press enter to get a new joke, or type ,q/exit, to quit: ").strip().lower()
        if User_input in("q","exit"):
            print("goodbye")
            break
        joke =get_random_joke()
        print(joke)

if __name__ == "__main__":
    main()