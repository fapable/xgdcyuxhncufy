def calc_temp_FtoC():                                           #start
    Fahrenheit = float(input("Insert Fahrenheit temperature"))  #input request
    Celsius = ( ( (Fahrenheit - 32) * 5 ) / 9)                  #formule F naar C
    print ( "%.2f" % Celsius)                                   #print
calc_temp_FtoC()                                                #end
