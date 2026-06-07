import requests
API_URL ="https://uselessfacts.jsph.pl/api/v2/facts/random?language=en"
def generate_facts():
    response = requests.get(API_URL)
    if response.status_code == 200:
        facts = response.json()
        print(f"\ndid you know ?\n{facts["text"]}")
    else:
        print("No data found")

def main():
    while True:
        user_input = input("Press enter to get a random fact or press q to quit: ").lower()
        if user_input == "q":
            print(f"\nGoodbye")
            break
        generate_facts()

if __name__ == "__main__":
    main()
