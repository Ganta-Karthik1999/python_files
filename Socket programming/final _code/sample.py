import csv

with open('final_data.csv','a+')as cs:
        kg=csv_writer(cs)
        kg.writerow(["karthik","yo","mama"])

cs.close()
