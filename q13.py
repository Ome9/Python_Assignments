'''
Suppose you’re working as data analyst in a healthcare department where you need to analyze the patient’s
data. Assume you’d received a dataset comprises diabetic details. Design a python program to read diabetes.
csv and print total number of lines present in the file. Also find out the how many null values exist in the
file. Finally print all the information in a new output file.

Note: First download the sample dataset from the given link 
https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database
'''

#CODE

import csv

# Open CSV file and read data into a list
with open("D:\diabetes.csv", "r") as diabetes_file:
  diabetes_data = list(csv.reader(diabetes_file))

# Print total number of lines in the file
print("Total number of lines:", len(diabetes_data))

# Count number of null values
null_count = 0
for row in diabetes_data:
  for value in row:
    if value == "":
      null_count += 1
print("Number of null values:", null_count)

# Write data to new output file
with open("diabetes_output.csv", "w", newline="") as output_file:
  writer = csv.writer(output_file)
  writer.writerows(diabetes_data)