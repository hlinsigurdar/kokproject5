from sample import fizzbuzz

def test_fizzbuzz():
    assert fizzbuzz(15) == "FizzBuzz"


def test_buzz():
    assert fizzbuzz(5) == "Buzz"
