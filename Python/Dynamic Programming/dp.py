import sys

# brute force approach
def fib_brute(n):
    if n <= 1:
        return n
    return fib_brute(n - 1) + fib_brute(n - 2)

#region Memoization (top down)
def fibRec(n, memo):
  
    # Base case
    if n <= 1:
        return n

    # To check if output already exists
    if memo[n] != -1:
        return memo[n]

    # Calculate and save output for future use
    memo[n] = fibRec(n - 1, memo) + \
              fibRec(n - 2, memo)
    return memo[n]

def fib_mem(n):
    memo = [-1] * (n + 1)
    return fibRec(n, memo)
#endregion

# Tabulation (bottom up)
def fib_tab(n):
    dp = [0] * (n + 1)

    # Storing the independent values in dp
    dp[0] = 0
    dp[1] = 1

    # Using the bottom-up approach
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    
    return dp[n]

# fibonacci number using space optimised.
def fib_opt(n):
    prevPrev, prev, curr = 0, 1, 1

    # Using the bottom-up approach
    for i in range(2, n + 1):
        curr = prev + prevPrev
        prevPrev = prev
        prev = curr

    return curr

def menu():
    print("Select which algorithm you want to use")
    print("1. Brute force")
    print("2. Memoization")
    print("3. Tabulation")
    print("4. Optimized")
    print("5. Exit")


def get_n(func):
    while True:
        num = input("Enter the Nth term you want to use: ")
        try:
            n = int(num)
            print(func(n), '\n')
            return
        except ValueError:
            print(f"The input '{num}' is not a valid integer.")

def main():
    while True:
        menu()
        choice = input("Enter your choice: ")
        match choice:
            case '1':
                get_n(fib_brute)
            case '2':
                get_n(fib_mem)
            case '3':
                get_n(fib_tab)
            case '4':
                get_n(fib_opt)
            case '5':
                print("Goodbye!")
                sys.exit()
            case _:
                print("Invalid option. Please try again.")

main()