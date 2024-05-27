from fizzbuzz import fizzbuzz
from fizzbuzz import fizzbuzz_list

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
    
def test_return_fizzbuzz_list_accordingly():
    assert fizzbuzz_list([3, 5, 15, 8]) == ["Fizz", "Buzz", "FizzBuzz", 8]
    assert fizzbuzz_list([30, 4, 9, 10]) == ["FizzBuzz", 4, "Fizz", "Buzz"]
    

