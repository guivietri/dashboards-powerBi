import datetime

# replace tab to comma
'''
with open('country_latitude_longitude.csv') as fileIn, open('country_latitude_longitude_new.csv', 'w') as fileOut:
    for line in fileIn:
        fileOut.write(line.replace('\t', ','))

'''
# remove /SP from nome_cidade/SP

'''
with open('processed_SP.csv', encoding="utf-8") as fileIn, open('new_vacc.csv', 'w', encoding="utf-8") as fileOut:
    for line in fileIn:
        if "/SP" in line:
            fileOut.write(line.replace('/SP', ''))
        else:
            fileOut.write(line)
'''

# edit date, change name to number, dd/mm/yyyy to mm/dd/yyyy

'''
with open('Dados-covid-19-estadoSP.csv') as fileIn, open('new.csv', 'w') as fileOut:
    for line in fileIn:
        if 'jan' in line:
            line = line.replace('jan', '01')
            date = line[:10]
            rest = line[10:]
            date = datetime.datetime.strptime(date, '%d/%m/%Y').strftime('%m/%d/%y')
            fileOut.write(date + rest)
        elif 'fev' in line:
            line = line.replace('fev', '02')
            date = line[:10]
            rest = line[10:]
            date = datetime.datetime.strptime(date, '%d/%m/%Y').strftime('%m/%d/%y')
            fileOut.write(date + rest)
        elif 'mar' in line:
            line = line.replace('mar', '03')
            date = line[:10]
            rest = line[10:]
            date = datetime.datetime.strptime(date, '%d/%m/%Y').strftime('%m/%d/%y')
            fileOut.write(date + rest)
        elif 'abr' in line:
            line = line.replace('abr', '04')
            date = line[:10]
            rest = line[10:]
            date = datetime.datetime.strptime(date, '%d/%m/%Y').strftime('%m/%d/%y')
            fileOut.write(date + rest)
        elif 'mai' in line:
            line = line.replace('mai', '05')
            date = line[:10]
            rest = line[10:]
            date = datetime.datetime.strptime(date, '%d/%m/%Y').strftime('%m/%d/%y')
            fileOut.write(date + rest)
        elif 'jun' in line:
            line = line.replace('jun', '06')
            date = line[:10]
            rest = line[10:]
            date = datetime.datetime.strptime(date, '%d/%m/%Y').strftime('%m/%d/%y')
            fileOut.write(date + rest)
        elif 'jul' in line:
            line = line.replace('jul', '07')
            date = line[:10]
            rest = line[10:]
            date = datetime.datetime.strptime(date, '%d/%m/%Y').strftime('%m/%d/%y')
            fileOut.write(date + rest)
        elif 'ago' in line:
            line = line.replace('ago', '08')
            date = line[:10]
            rest = line[10:]
            date = datetime.datetime.strptime(date, '%d/%m/%Y').strftime('%m/%d/%y')
            fileOut.write(date + rest)
        elif 'set' in line:
            line = line.replace('set', '09')
            date = line[:10]
            rest = line[10:]
            date = datetime.datetime.strptime(date, '%d/%m/%Y').strftime('%m/%d/%y')
            fileOut.write(date + rest)
        elif 'out' in line:
            line = line.replace('out', '10')
            date = line[:10]
            rest = line[10:]
            date = datetime.datetime.strptime(date, '%d/%m/%Y').strftime('%m/%d/%y')
            fileOut.write(date + rest)
        elif 'nov' in line:
            line = line.replace('nov', '11')
            date = line[:10]
            rest = line[10:]
            date = datetime.datetime.strptime(date, '%d/%m/%Y').strftime('%m/%d/%y')
            fileOut.write(date + rest)
        elif 'dez' in line:
            line = line.replace('dez', '12')
            date = line[:10]
            rest = line[10:]
            date = datetime.datetime.strptime(date, '%d/%m/%Y').strftime('%m/%d/%y')
            fileOut.write(date + rest)
        elif 'Data' in line:
            fileOut.write(line)
        else:
            date = line[:10]
            rest = line[10:]
            date = datetime.datetime.strptime(date, '%d/%m/%Y').strftime('%m/%d/%y')
            fileOut.write(date + rest)
'''