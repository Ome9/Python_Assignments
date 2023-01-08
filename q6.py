'''
An institution mandated all its employees to submit their PAN card through the google form. There are some mischievous employees who purposefully submitting random number as PAN card number instead of PAN card number format. You design a python code to check whether the data entered by the employee is the valid PAN card number or not. If it is a valid PAN card format, print “Valid” otherwise print “Invalid”. 

The rule for PAN Card number is as follows: 

In total, it should be an alphanumeric string of length 10
The first half of the PAN is alphabets only
The last character should be an alphabet.
The remaining characters are numbers only.
No special Characters are allowed.
Only Upper-case characters are allowed
'''
#CODE

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