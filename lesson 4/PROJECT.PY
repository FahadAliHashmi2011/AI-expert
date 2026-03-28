import random

def get_ai_move(history):
    """
    Basic Strategy: Frequency Analysis.
    The AI tracks how many times you've played each move and 
    chooses the counter to your most frequent choice.
    """
    if not history:
        return random.choice(['rock', 'paper', 'scissors'])

    
    counts = {
        'rock': history.count('rock'),
        'paper': history.count('paper'),
        'scissors': history.count('scissors')
    }
    
    
    prediction = max(counts, key=counts.get)
    
    
    strategy_map = {
        'rock': 'paper',
        'paper': 'scissors',
        'scissors': 'rock'
    }
    
    return strategy_map[prediction]

def play_game():
    moves = ['rock', 'paper', 'scissors']
    player_history = []
    scores = {"player": 0, "ai": 0}
    
    print("--- Rock Paper Scissors: Strategy Edition ---")
    print("Type 'quit' to exit.")

    while True:
        user_input = input("\nEnter Rock, Paper, or Scissors: ").lower()
        
        if user_input == 'quit':
            break
        if user_input not in moves:
            print("Invalid choice. Try again!")
            continue

        ai_move = get_ai_move(player_history)
        player_history.append(user_input)

        print(f"AI chose: {ai_move}")

    
        if user_input == ai_move:
            print("It's a tie!")
        elif (user_input == 'rock' and ai_move == 'scissors') or \
             (user_input == 'paper' and ai_move == 'rock') or \
             (user_input == 'scissors' and ai_move == 'paper'):
            print("You win this round!")
            scores["player"] += 1
        else:
            print("AI wins this round!")
            scores["ai"] += 1

        print(f"Score -> You: {scores['player']} | AI: {scores['ai']}")

if __name__ == "__main__":
    play_game()