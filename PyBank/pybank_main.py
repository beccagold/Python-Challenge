import csv

#loads and outputs a new file(s)
files_load = "raw_data.csv"
files_output = "PyBankAnalysis.txt"

#parameters to track
tmonths = 0
tamount = 0
previousvalue = 0
monthschange = []
profitchange = []
maxincrease = 0
maxdecrease = 0

#read csv and convert into a list
with open(files_load) as profitdata:
    reader = csv.DictReader(profitdata)

    for row in reader:
        tmonths = tmonths+1
        tamount = tamount + int(row["Profit/Losses"])

        if tmonths > 1:
            change = int(row["Profit/Losses"])-previousvalue
            monthschange.append(change)
            
            if change > maxincrease:
                maxincrease = change
                maxincrease_month = row["Date"]
            if change < maxdecrease:
                maxdecrease = change
                maxdecrease_month = row["Date"]
        previous =  int(row["Profit/Losses"])

avgprofitchange = round(sum(monthschange)/(len(monthschange)+0.0),2)

analysisoutput = ('\n\n\n\nFinancial Analysis'+ '\n'+
          '----------------------------'+ '\n'  +
          'Total Months: ' + str(tmonths) + '\n' +
          'Total: ' + ' $'+ str(tamount) + '\n' +
          'Average Change:' + ' $' + str(avgprofitchange) + '\n' +
          'The Greatest Increase in Profits: ' + maxincrease_month + ' $' + str(maxincrease) + '\n' +
          'The Greatest Decrease in Profits: ' + maxdecrease_month + ' $' + str(maxdecrease) + '\n\n\n')

print(analysisoutput)

with open(files_output, 'w') as outputfile:
    outputfile.write(analysisoutput)