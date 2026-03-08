from textblob import TextBlob
import matplotlib.pyplot as plt


stats = {"positive": 0, "negative": 0, "neutral": 0}
history = []

print("--- Welcome to the Sentiment Spy Chatbot! ---")
name = input("What is your name? ")
print(f"Nice to meet you, {name}. Type 'exit' to quit or 'report' to see stats.")

while True:
    user_input = input("\nEnter text for analysis: ")
    

    if user_input.lower() == 'exit':
        break
    elif user_input.lower() == 'report':
        print(f"\nSentiment Statistics: {stats}")
        continue
    elif user_input.lower() == 'reset':
        stats = {"positive": 0, "negative": 0, "neutral": 0}
        history = []
        print("Data reset.")
        continue

    analysis = TextBlob(user_input)
    if analysis.sentiment.polarity > 0:
        sentiment = "positive"
        print("That sounds like a positive sentiment!")
    elif analysis.sentiment.polarity < 0:
        sentiment = "negative"
        print("I detect some negativity there.")
    else:
        sentiment = "neutral"
        print("That seems neutral.")

    
    stats[sentiment] += 1
    history.append((user_input, sentiment))

print(f"\n--- Final Mission Report for {name} ---")
print(f"Total entries analyzed: {sum(stats.values())}")


labels = stats.keys()
values = stats.values()

plt.figure(figsize=(8, 5))
plt.bar(labels, values, color=['green', 'red', 'gray'])
plt.title(f"Sentiment Analysis Results for {name}")
plt.xlabel("Sentiment Category")
plt.ylabel("Number of Inputs")
plt.show()

print("Mission complete. Goodbye!")