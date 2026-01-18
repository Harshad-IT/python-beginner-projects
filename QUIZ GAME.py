# PYTHON QUIZ GAME

print("=" * 80)
print("✨PYTHON QUIZ GAME✨".center(80))
print("=" * 80)

questions = ("1. What is the capital of Australia?:",
             "2. Who is known as the 'Father of the indian constitution'?:",
             "3. Which planet is called the red planet?:",
             "4. Which is the largest ocean in the world?:",
             "5. Which is the national animal of india?:",
             "6. Who invented the telephone?:",
             "7. Which gas do plants absorb from  the atmosphere?:",
             "8. Which country is known as the land of Rising Sun?:",
             "9. How many continents are there in the world?:",
             "10. Which is the longest river in the world?:")

options = (("A. Sydney", "B. Melbourne", "C. Canberra", "D. Perth"),
           ("A. Mahatma Gandhi", "B. Jawaharlal Nehru", "C. Dr. B. R. Ambedkar", "D. Sardar Patel"),
           ("A. Venus", "B. Mars", "C. Jupiter", "D. Saturn"),
           ("A. Atlantic Ocean", "B. Indian Ocean", "C. Arctic Ocean", "D. Pacific Ocean"),
           ("A. Lion", "B. Elephant", "C. Tiger", "D. Leopard"),
           ("A. Thomas Edison", "B. Alexander Graham Bell", "C. Nikola Tesla", "D. James Watt"),
           ("A. Oxygen", "B. Nitrogen", "C. Carbon Dioxide", "D. Hydrogen"),
           ("A. China", "B. Japan", "C. Thailand", "D. South korea"),
           ("A. 5", "B. 6", "C. 7", "D. 8"),
           ("A. Amazon", "B. Ganga", "C. Yangtze", "D. Nile"))

answers = ("C", "C", "B", "D", "C", "B", "C", "B", "C", "D")
guesses = []
score = 0
question_num = 0

for question in questions:
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[question_num]} is  the correct answer")
    print("-" * 80)
    question_num += 1
text = "RESULTS"
a = text.center(80)
print("=d"
      "d" * 80)
print(a)
print("=" * 80)

print("Answers: ", end=" ")
for answer in answers:
    print(answer, end=" ")
print()

print("Guesses: ", end=" ")
for guess in guesses:
    print(guess, end=" ")
print()

print("=" * 70)


score = score / len(questions) * 100
print(f"Your score is: {score:.2f}%")
if score >= 80:
    print("🔥 Excellent performance!")
elif score >= 50:
    print("👍 Good job! Keep practicing.")
else:
    print("📘 Needs improvement. Try again!")

print("\n👋 Thank you for playing the Quiz Game!")
print("=" * 70)