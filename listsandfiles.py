def main():
    cities = ["Chicago", "Boston", "Houston", "Dallas"]

    outfile = open('cities.txt', 'w')
    for item in cities:
        outfile.write(item + '\n')
    outfile.close()

main()
