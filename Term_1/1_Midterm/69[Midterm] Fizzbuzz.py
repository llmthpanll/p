"""[Midterm] Fizzbuzz"""
def main():
    """[Midterm] Fizzbuzz"""
    num = int(input())
    for i in range(1, num+1):
        if i%3 == 0 and i%5 == 0:
            print("FizzBuzz")
        elif i%5 == 0:
            print("Buzz")
        elif i%3 == 0:
            print("Fizz")
        else:
            print(i)
main()
