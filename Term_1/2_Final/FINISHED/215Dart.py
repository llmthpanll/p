"""Dart"""
def main():
    """Dart"""
    amount = int(input())
    count = 0
    for _ in range(amount):
        posi = input()
        posi = posi.split(" ")
        point_x = int(posi[0])
        point_y = int(posi[1])
        radius = ((point_x**2)+(point_y**2))**0.5
        if radius <= 2:
            count += 5
        elif radius <= 4:
            count += 4
        elif radius <= 6:
            count += 3
        elif radius <= 8:
            count += 2
        elif radius <= 10:
            count += 1
    print(count)
main()
