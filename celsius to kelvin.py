def calc_temp_CtoK():                                       #start
    Celsius = float(input("Insert Celcius temperature."))   #input request
    if Celsius >= -273.15:                                  #checken op rare taferelen
        Kelvin = (Celsius + 273.15)                         #formule celsius naar kelvin
        print ( "%.2f" % Kelvin)                            #print kelvin
    else:                                                   #in het geval van rare taferelen
        print ("Kelvin cannot go below 0.")                 #commentaar op de rare taferelen
calc_temp_CtoK()                                            #end
