from kalkulator import squared

def main():
    test_positive()
    test_negative()
    test_netral()

def test_positive():
    assert squared(2) == 4
    assert squared(5) == 25
    
def test_negative():
    assert squared(-2) == 4
    assert squared(-5) == 25
    
def test_netral():
    assert squared(0) == 0

if __name__ == "__main__":
    main()
