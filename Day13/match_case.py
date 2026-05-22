# Example: Math operations using match-case
num = 2

match num:
    case 1:
        print("Square:", num ** 2)
    case 2:
        print("Cube:", num ** 3)
    case 3:
        print("Square Root:", num ** 0.5)
    case _:
        print("Invalid choice")
