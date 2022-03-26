# Importing the calendar module
import calendar

# Creating the object my_calendar from the calendar module 
my_calendar = calendar.TextCalendar(calendar.SUNDAY)
# Making sure the start of the month is Sunday
august_2005_calandar = my_calendar.formatmonth(2005, 8)
print(august_2005_calandar)