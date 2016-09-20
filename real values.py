def absolute_values():   #start
    Value = float(input("Insert value here."))   #request value     float zodat geen problemen met strings
    if (Value >= 0):            
        print (Value)
    else:
        Value =( Value * -1)   #real value maken
        print (Value)  #print
absolute_values()  #end
