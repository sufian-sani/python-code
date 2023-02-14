import csv
reader=csv.reader(open("employees.csv"))

no_line=len(list(reader))

print(no_line)