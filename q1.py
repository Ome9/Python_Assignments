'''
Create a Python code that takes every object from the list and check if it has list object or not. If a list object is present in a list, it should be unpacked, and the overall count of the list should be conveyed. If list object is not present in the existing list, it should say “cannot unpack”

Note: The output "cannot unpack" should be in lower case and only one space between two words.

Sample Input: [[1,2],’a’,”Hello”] 

Sample output: 4
'''

#CODE#

z=input()
lst=[]
b=z.split("[")
i=0
if len(b)>2:
    c=z.split(",")
    print(len(c))
else:
    print("cannot unpack")
    
    