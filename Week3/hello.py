def main():
    str = input("whats your name ? ")
    print(hello(str))
    
def hello(to="World!"):
    return f"Hello, {to}"

if __name__ == "__main__":
    main()