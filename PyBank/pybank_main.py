import csv
import os
file_load = "raw_data.csv"
file_output = "pybank_analysis.txt"

# initial parameters
tmonths = 0
total = 0
row_used = 0
maxinc = 0 
maxdec = 0
#empty list
month_change = []

# read the csv &convert 
with open(file_load) as profitdata:
    reader = csv.DictReader(profitdata)
    for row in reader: #loop through rows to calculate # months and total
        # track total
        tmonths += 1 
        total = total + int(row["Profit/Losses"])
        if tmonths > 1: #determines change in profit and if its greater than the inc/dec of new to find max
            change = int(row["Profit/Losses"])-row_used
            month_change.append(change)
            
            if change > maxinc:#finds max inc
                maxinc = change
                maxinc_month = row["Date"]
            if change < maxdec:#finds max dec
                maxdec = change
                maxdec_month = row["Date"]
        row_used = int(row["Profit/Losses"])#cycles through rows

# Calculate the average
sums = sum(month_change)
length  = len(month_change)+ 0.0
avg = round(sums/length,2)

#output = ('Financial Analysis'+ '\n'+'.........................'+ '\n'  +'Total Months: ' + str(tmonths) + '\n' +'Total: ' + ' $'+ str(total) + '\n' +'Average Change:' + ' $' + str(avg ) + '\n' +'The Greatest Increase in Profits: ' + maxinc_month + ' $' + str(maxinc) + '\n' +'The Greatest Decrease in Profits: ' + maxdec_month + ' $' + str(maxdec) + '\n')

print('Financial Analysis'+ '\n'+'.........................'+ '\n'  +'Total Months: ' + str(tmonths) + '\n' +'Total: ' + ' $'+ str(total) + '\n' +'Average Change:' + ' $' + str(avg ) + '\n' +'The Greatest Increase in Profits: ' + maxinc_month + ' $' + str(maxinc) + '\n' +'The Greatest Decrease in Profits: ' + maxdec_month + ' $' + str(maxdec) + '\n')

with open(file_output, 'w') as fileoutput:#writing file
    fileoutput.write('Financial Analysis'+ '\n'+'.........................'+ '\n'  +'Total Months: ' + str(tmonths) + '\n' +'Total: ' + ' $'+ str(total) + '\n' +'Average Change:' + ' $' + str(avg ) + '\n' +'The Greatest Increase in Profits: ' + maxinc_month + ' $' + str(maxinc) + '\n' +'The Greatest Decrease in Profits: ' + maxdec_month + ' $' + str(maxdec) + '\n')
