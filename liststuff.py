def main():
    scores = get_scores()
    total = get_total(scores)
    lowest = min(scores)

    total = total - lowest
    average = total /(len(scores) - 1)


    print("average with lowest score dropped: ", average)

def get_scores():
    test_scores = []
    again = 'y'
    while again == 'y':
        value = float(input("Enter score"))
        test_scores.append(value)
        print("Do it again?")
        again = input("type y for yes or anything else for no: ")
        print()
    return test_scores

def get_total(value_list):
    total = 0.0
    for num in value_list:
        total = total + num
    return total

main()
