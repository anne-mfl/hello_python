from fizzbuzz import fizzbuzz

def test_return_fizz_if_3():
    assert fizzbuzz(3) == "Fizz"
    assert fizzbuzz(6) == "Fizz"
    
def test_return_buzz_if_5():
    assert fizzbuzz(5) == "Buzz"
    assert fizzbuzz(10) == "Buzz"
    
def test_return_fizzbuzz_if_3and5():
    assert fizzbuzz(15) == "FizzBuzz"
    assert fizzbuzz(30) == "FizzBuzz"
    
def test_return_number_in_other_case():
    assert fizzbuzz(2) == 2
    assert fizzbuzz(8) == 8