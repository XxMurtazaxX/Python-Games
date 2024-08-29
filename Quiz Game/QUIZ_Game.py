print(
 "Welcome to QUIZ Game, you have to answer 5 different questions to win \"10 MILLION\". Every Question will be having a merit of 2 MILLION and any wrong answer will make you lose the game, however you get the money for previous correctly answered questions:-\n"
)

Q1 = "Q1) When compared to their body weight, which animal is the strongest?"
Q2 = "Q2) What is the Capital of Pakistan?"
Q3 = "Q3) What is the tallest peak in the world?"
Q4 = "Q4) Which animal is known as the ship of the desert?"
Q5 = "Q5) What is largest organ of the Human body?"

A1 = "A. Dung Beetle\nB. Elephant\nC. Ant\nD. Cow"
A2 = "A. New-Delhi\nB. Kabul\nC. Canberra\nD. Islamabad"
A3 = "A. K2\nB. Mount-Everest\nC. Mount-Kangchenjunga\nD. Lhotse"
A4 = "A. lizards\nB. Snakes\nC. Jackrabbits\nD. Camels"
A5 = "A. Liver\nB. Heart\nC. Skin\nD. Lungs "

Q_A = [(Q1,A1),(Q2,A2),(Q3,A3),(Q4,A4),(Q5,A5)]
correct_answers=["A","D","B","D","C"]
i = 0
reward = 0

for item in Q_A:

    print(item[0])
    print(item[1])

    x = (input("Choose the correct answer from above:")).upper()

    if (x == correct_answers[i]):

        reward += 2
        i += 1

        if(i == len(correct_answers)):
               print("\nWOW! you successfully gave all answers correctly:")
               print(f'You won a total reward of \"{reward} Million\"!\n')
        else:
               print(f"\nCorrect! you won {reward} Million as a reward!")
               print("You may proceed to the next question:\n")
   
    else:
        print(f"\nWrong answer!")
        print(f'You won a total reward of \"{reward} Million\"!\n')
        print("GAME OVER!")
        break