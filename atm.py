'''
   CS5001
   Homework 1
   Spring 2024
   Kole Agava
'''
def main():
    '''
    ATM Program to Dispense Bills and Coins
    Test Cases

    Test Case 1
    Input: 137
    Expected Output:
    2 x $50 bills
    1 x $20 bills
    1 x $10 bills
    1 x $5 bills
    1 x $2 coins
    1 x $1 coins

    Test Case 2
    Input: 93
    Expected Output:
    1 x $50 bills
    2 x $20 bills
    1 x $2 coins
    1 x $1 coins

    Test Case 3
    Input: 17
    Expected Output:
    1 x $10 bills
    1 x $5 bills
    2 x $1 coins

    Additional Test Cases

    Test Case 4
    Input: 0
    Expected Output:
    (Enter a number greater than 0)

    Test Case 5
    Input: 57
    Expected Output:
    1 x $50 bills
    1 x $5 bills
    2 x $1 coins

    Test Case 6
    Input: 98
    Expected Output:
    1 x $50 bills
    2 x $20 bills
    1 x $5 bills
    3 x $1 coins
    '''

fifties = 0
twenties = 0
tens = 0
fives = 0
toonies = 0
loonies = 0

amount_to_withdraw = int(input("Enter your amount "))
if amount_to_withdraw >= 50:
    fifties = amount_to_withdraw // 50
    amount_to_withdraw %= 50
    print(f"{fifties} x $50 bills")
if amount_to_withdraw >= 20:
    twenties = amount_to_withdraw // 20
    amount_to_withdraw %= 20
    print(f"{twenties} x $20 bills")
if amount_to_withdraw >= 10:
    tens = amount_to_withdraw // 10
    amount_to_withdraw %= 10
    print(f"{tens} x $10 bills")
if amount_to_withdraw >= 5:
    fives = amount_to_withdraw // 5
    amount_to_withdraw %= 5
    print(f"{fives} x $5 bills")
if amount_to_withdraw >= 2:
    toonies = amount_to_withdraw // 2
    amount_to_withdraw %= 2
    print(f"{toonies} x $2 coins")
if amount_to_withdraw >= 1:
    loonies = amount_to_withdraw // 1
    amount_to_withdraw %= 1
    print(f"{loonies} x $1 coin")
else:
    print("Enter a number greater than 0")


if __name__ == "__main__":
    main()


    
    
