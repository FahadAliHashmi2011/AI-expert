import pandas as pd
from textblob import TextBlob
from colorama import init,Fore
init(autoreset=True)
movies = pd.read_csv("lesson 6/imdb_top_1000.csv")
print(Fore.CYAN + "welcome to the ai movie recommender !")
name = input(Fore.YELLOW + " what is your name ? ")
print(Fore.GREEN + f"\nhello {name} lets find a movie for you \n")
genre = input(" enter a movie genre, for example(drama , comedy , action): ")
mood =  input("how are you feeling today ?")
mood_score = TextBlob(mood).sentiment.polarity
if mood_score > 0:
    mood_type =  "positive"
elif mood_score < 0:
    mood_type = "negative"
else:
    mood_type = "neutral"
print(f"\nYour mood type is looking {mood_type}\n")
filtered_movies =movies[movies["Genre"].str.contains(genre, case=False, na=False)]
if filtered_movies.empty :
    print("sorry no movies for that genre")
else:
    print(" finding good movie recommendations for you ...")
    reccomendations = []
    for index, row in filtered_movies.iterrows():
        overview= row["Overview"]
        if pd.isna(overview):
            continue
        overview_score = TextBlob(overview).sentiment.polarity
        if mood_score > 0:
            if overview_score > 0 :
                reccomendations.append(row["Series_Title"])
        else:
            reccomendations.append(row["Series_Title"])
        if len(reccomendations)==5:
            break
if len(reccomendations) > 0:
    print(Fore.YELLOW + f"🍿 Recommended movies for {name}:\n")
    for i, movie in enumerate(reccomendations, 1):
        print(Fore.CYAN + f"{i}. {movie}")
else:
    print(Fore.RED + "Sorry! No suitable movies were found.")   

    

