
miles = float(input("Please tell me how many miles you want converted to kilometers: "))    #input miles to convert
miles_to_kilometers = float(miles * 1.6)                                                    #convert miles to kilometers    
print (miles, "miles equals", miles_to_kilometers, "kilometers")                            #print number of miles as number in kilometers

fahrenheit_temperature = float(input("Please tell me the temperature in fahrenheit: "))     #input temp to convert
fahrenheit_to_celsius = float((fahrenheit_temperature - 32) * 5/9)                          #convert fahrenheit to celsius
print (fahrenheit_temperature, "Fahrenheit is", fahrenheit_to_celsius, "Celsius")           #print temp in farenheit as temp in celsius

gallons = float(input("Please tell me how many gallons you want converted to liters: "))    #input gallons to convert
gallons_to_liters = float(gallons * 3.9)                                                    #convert gallons to liters
print (gallons, "gallons equals", gallons_to_liters, "liters")                              #print amount in gallons as amount in liters

pounds = float(input("Please tell me how many pounds you want converted to kilograms: "))   #input pounds to convert
pounds_to_kilograms = float(pounds * .45)                                                   #convert pounds to kilograms
print (pounds, "pounds equals", pounds_to_kilograms, "kilograms")                           #print number of pounds as number of kilograms

inches = float(input("Please tell me how many inches you want converted to centimeters: ")) #input inches to convert
inches_to_centimeters = float(inches * 2.54)                                                #convert inches to centimeters
print (inches, "inches equals", inches_to_centimeters, "centimeters")                       #print number of inches as number of centimeters
