import random


def generate_random_number(min_value, max_value):
    """
    Get a Random integer between min_value and max_value
    """
    return random.randint(min_value, int(max_value))



def choose_random_operator():
    """
    Choose an operator randomly.
    """
    return random.choice(['+', '-', '*','/'])

def calculate(operand1, operand2, operator):
    """
    Calculate the result of operand1 and operand2 using the operator.

    Parameters:
    operand1 (float/int): The first operand for the arithmetic operation.
    operand2 (float/int): The second operand for the arithmetic operation.
    operator (str): The arithmetic operator, one of ['+', '-', '*', '/'].

    Returns:
    tuple: A tuple containing a string representation of the operation and its result.
           Returns an error message and None if an exception occurs.
    """

    try:
        operation_description = f"{operand1} {operator} {operand2}"
        if operator == '-':
            result = operand1 - operand2
        elif operator == '+':
            result = operand1 + operand2
        elif operator == '*':
            result = operand1 * operand2
        elif operator == '/':
            if operand2 == 0:
                raise ValueError("Cannot divide by zero")
            result = operand1 / operand2
        else:
            raise ValueError("Invalid operator. Use '+', '-', '*', or '/'.")

        return operation_description, result

    except ValueError as calculateError:
        return str(calculateError), None
    except Exception as calculateException:
        return f"An unexpected error occurred: {str(calculateException)}", None


def math_quiz():
    """
    Conduct a math quiz game where the user answers a set of arithmetic problems.
    The quiz consists of a fixed number of randomly generated arithmetic problems.
    The user's score is calculated based on the number of correct answers.
    """
    score = 0
    total_questions = 4  # Set to an integer value

    # Print welcome message
    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    # Iterate through each question
    for _ in range(total_questions):
        # Generate random numbers
        operand1 = generate_random_number(1, 10)
        operand2 = generate_random_number(1, 5.5)
        operator = choose_random_operator()

        # Calculate the question and answer
        problem, answer = calculate(operand1, operand2, operator)
        print(f"\nQuestion: {problem}")

        # Ask user for answer
        try:
            user_answer = float(input("Your answer: "))
            # Check if answer is correct
            if round(user_answer, 2) == round(answer, 2):
                print("Correct! You earned a point.")
                score += 1
            else:
                print(f"Wrong answer. The correct answer is {answer}.")

        except ValueError:
            print("Invalid input. Please enter a valid number.")

    # Print score
    print(f"\nGame over! Your score is: {score}/{total_questions}")

if __name__ == "__main__":
    """
    Run the game
    """
    math_quiz()

