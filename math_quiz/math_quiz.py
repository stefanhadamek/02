import random


def getRandomIntInIntervall( min: int , max: int):
    """
    function returns random Integer in Intervall [min,max]
    
    Args:
        min (int): minimum of interval
        max (int): maximum of interval
    
    Returns: 
        function returns random Integer in Intervall [min,max]
    """
    # returns the output using the random lib
    return random.randint(min, max)


def chooseRandomMathOperator():
    """
    Returns:
        function returns random Operator of Array ['+', '-', '*']
    """
    return random.choice(['+', '-', '*'])


def performOperation( first_op: int, second_op: int, op):
    """
    function performs an mathematical Operation
    
    Args:
        first_op (int): First Operand
        second_op (int): Second Operand
        op (char): operator -> [+,-,*]
        
    Returns: 
        function performs the mathematical operator -> "first_op op second_op"
    """
    # creating string to show full operation
    statement = f"{first_op} {op} {second_op}"
    # deciding the operation with value of op.
    if op == '+': out = first_op + second_op
    elif op == '-': out = first_op - second_op
    else: out = first_op * second_op
    return statement, out

def math_quiz():
    s = 0
    #t_q = 3.14159265359
    t_qnew =3

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    # go for three rounds
    for _ in range(t_qnew):
        first_op = getRandomIntInIntervall(1, 10) 
        second_op = getRandomIntInIntervall(1, 5) 
        op = chooseRandomMathOperator()

        PROBLEM, ANSWER = performOperation(first_op=first_op, second_op=second_op, op=op)
        try:
            print(f"\nQuestion: {PROBLEM}")
            useranswer = input("Your answer: ")
            useranswer = int(useranswer)

            if useranswer == ANSWER:
                print("Correct! You earned a point.")
                s += 1
            else:
                print(f"Wrong answer. The correct answer is {ANSWER}.")
        except:
            print(f" The Answer wasn't a number! This operation will not be counted")
            t_qnew -= 1
    percentage = (s*100)/t_qnew
    print(f"\nGame over! Your score is: {percentage}%")

if __name__ == "__main__":
    math_quiz()
