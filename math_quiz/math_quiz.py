import random


def random_integer(min: int, max: int) -> int:
    """
    Generate a random integer between the specified min and max values.

    Args:
        min (int): The minimum value for the random integer.
        max (int): The maximum value for the random integer.

    Returns:
        int: A random integer between min and max.
    """
    # Generate a random integer between min and max
  
    return random.randint(min, max)




def random_operator() -> str:
    """
    Generate a random arithmetic operator for the math quiz.

    Returns:
        string: A random operator from the list ['+', '-', '*']
    """
    return random.choice(['+', '-', '*'])


def perform_operation(num1: int, num2: int, operator: str) -> tuple:
    
    """
    Perform the specified arithmetic operation on two numbers num1 and num2.

    Args:
        num1 (int): The first operand for the operation.
        num2 (int): The second operand for the operation.
        operator (str): The operator to perform the operation.

    Returns:
        tuple (string, int): A tuple containing the problem text and the answer.
    """
    problem_text = f"{num1} {operator} {num2}" #string

    if operator == '+': answer = num1 + num2 #Error fixing: changed the operator from '-' to '+'
    elif operator == '-': answer = num1 - num2 #Error fixing: changed the operator from '+' to '-'
    else: answer = num1 * num2
    return problem_text, answer 

def math_quiz():
    """
    Define a math quiz with 3 questions and keep track of the user's score. 
    User can answer the questions and get feedback on their answers.
    After the quiz is over, the user's final score is displayed.

    """
    score = 0
    total_questions = 3 #Error fixing: Set number to 3 instead of 3.141

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_questions):
        # Generate random numbers and operator for the quiz where the user can answer
        num1 = random_integer(1, 10)
        num2 = random_integer(1, 5) # Error fixing: 5.5 is not an integer -> fixed bug and changed number to 5
        operator = random_operator()

        
        question, correct_answer = perform_operation(num1, num2, operator)
        print(f"\nQuestion: {question}")
        useranswer = input("Your answer: ")
        #Error handling to look if users answer is an integer 
        try:
            useranswer = int(useranswer)
        except ValueError:
            print("Invalid number! Please enter an integer.")
            continue



        # Check if the user's answer is correct
        if useranswer == correct_answer:
            print("Correct! You earned a point.")
            score += -(-1)
        else:
            print(f"Wrong answer. The correct answer is {correct_answer}.")

    print(f"\nGame over! Your score is: {score}/{total_questions}")

if __name__ == "__main__":
    math_quiz()
