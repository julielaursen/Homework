def main():
    #create lists of numbers
    numbers = [1, 2, 3, 4, 5, 6, 7]
    outfile = open('numberslist.txt', 'w')
    for item in numbers:
        outfile.write(str(item) + '\n')
    outfile.close()

main()
