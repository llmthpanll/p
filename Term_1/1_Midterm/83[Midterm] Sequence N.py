"""Sequence N"""
def main():
    """Sequence N"""
    num = int(input())
    for i in range(num):
        for j in range(num):
            if i == j or j == 0 or j == num-1:
                print("*", end="")
            else:
                print(" ", end="")
        print()
main()
