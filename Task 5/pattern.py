def print_pattern():
    n = 5  # Number of rows for the upper half of the pattern
    for i in range(n):
        # Print the left half
        print("A", end="")
        if i > 0:
            print(" " * i + chr(65 + i), end="")
        
        # Print the middle spaces
        print(" " * (2 * (n - i - 1)), end="")
        
        # Print the right half
        if i > 0:
            print(chr(65 + i) + " " * i + "A", end="")
        else:
            print("A", end="")
        
        print()

    for i in range(n - 1, -1, -1):
        # Print the left half
        print("A", end="")
        if i > 0:
            print(" " * i + chr(65 + i), end="")
        
        # Print the middle spaces
        print(" " * (2 * (n - i - 1)), end="")
        
        # Print the right half
        if i > 0:
            print(chr(65 + i) + " " * i + "A", end="")
        else:
            print("A", end="")
        
        print()

print_pattern()
