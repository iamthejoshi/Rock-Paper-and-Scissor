from flask import Flask, request, jsonify
import random

app = Flask(__name__)

# Define the moves
moves = ['rock', 'paper', 'scissors']

@app.route('/play', methods=['GET'])
def play():
    user_choice = request.args.get('choice', '')
    computer_choice = random.choice(moves)
    
    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        result = f"You win! {user_choice.capitalize()} beats {computer_choice}."
    else:
        result = f"You lose! {computer_choice.capitalize()} beats {user_choice}."

    return jsonify(message=result)

if __name__ == '__main__':
    app.run(debug=True)
