def main():
    number = int(input("What's the number? "))
    print(f"Squared of {number} is", squared(number))

def squared(n):
    return n * n

if __name__ == "__main__":
    main()
