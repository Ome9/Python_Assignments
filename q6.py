z=input()
if z.isalnum() and len(z)==10:
    if z[0:5].isalpha() and z.isupper():
        if z[len(z)-1].isalpha() and z.isupper():
            if z[5:9].isnumeric():
                print("Valid")
            else:
                print("Invalid")    
        else:
            print("Invalid")    
    else:
        print("Invalid")    
else:
    print("Invalid")