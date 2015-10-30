def main():
    numbers = [2, 4, 6, 8, 10]
    print("The total is", get_total(numbers))

def get_total(values):
    total = 0
    for num in values:
        total = total + num
    return total

main()
