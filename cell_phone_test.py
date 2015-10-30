import cellphone

def main():
    man = input("Enter the manufacturer: ")
    mod = input("enter the model number: ")
    retail = float(input("Enter the retail price: "))

    phone = cellphone.CellPhone(man, mod, retail)

    print("Here is the data you entered: ")
    print('Manufacturer:', phone.get_manufact())
    print('Model number:', phone.get_model())
    print('Retail price $', format(phone.get_retail_price(), ',.2f'), sep ='')

main()
