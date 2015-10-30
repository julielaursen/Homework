import pickle
import cellphone

FILENAME = 'cellphones.dat'

def main():
    again = 'y'

    output_file = open(FILENAME, 'wb')
    while again.lower == 'y'
        man = input("Enter the manufacturer ")
        mod = input("Enter the model number: ")
        retail = float(input("Enter the retail price ")

        phone = cellphone.Cellphone(man, mod, retail)

        #pickle the object and write it to a file
        pickle.dump(phone, output_file)

        again = input("Enter more phone data? y/n: ")

    output_file.close()

main()

                       
