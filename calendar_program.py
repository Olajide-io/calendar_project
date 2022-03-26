import calendar
calendar.setfirstweekday(calendar.SUNDAY)
year = 2005
month = 7
calen = calendar.monthcalendar(year, month)

# Creating an header for the calendar
print('|------ %s-%s ----|' % ("Aug", year))
print('|Su Mo Tu We Th Fr Sa|')
print('|--------------------|')

border = '|'
for week in calen:
    line = border

      
    for day in week:
        if day == 0: 
      # Creating 3 spaces for the empty days       
            line += '   ' 
        elif len(str(day)) == 1:
            line += ' %d ' % day
        else:
         line += '%d ' % day
    # Making sure spaces in the last column are removed
    line = line[0:len(line) - 1]  
    line += border
    print(line)

