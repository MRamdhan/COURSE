from hello import hello

def main():
    test_default()
    test_argument()

def test_default():
    assert hello() == "Hello, World!"
    
def test_argument():
    for name in ["Rosa","Nadira"]:
        assert hello(name) == f"Hello, {name}"
    
if __name__ == '__main__':
    main()