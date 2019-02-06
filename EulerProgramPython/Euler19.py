# want a set of tuples of the form (dayofweek,dayofmonth,month of year,year), 
#the day of week be NumberOfDaysAfter( 1 jan 1900 )%7 where 0 represents Monday, can even display said day.
#year shall represent the year, I will make a tuple of length 12 representing the number of days in the respective months
# if year == leapyear then MonthTuple = (31,29,31,30,31,30,31,31,30,31,30,31);
# else MonthTuple = (31,28,31,30,31,30,31,31,30,31,30,31)
#
def IsLeapYearBool(year):
#    return (year%400 == 0 or (year%100 != 0 and year%4 == 0))
    if year%400 == 0:
        return True
    elif year%100 == 0:
        return False
    elif year%4 == 0:
        return True
    else:
        return False
    
def Monthtuple(Year):
    #This function takes in a year, and spits out the number of days each month in that year has in the form (jan,feb,mar...)
    if IsLeapYearBool(Year):
        return (31,29,31,30,31,30,31,31,30,31,30,31)
    else:
        return (31,28,31,30,31,30,31,31,30,31,30,31)
    
def DayOfYear(DayOfMonth,MonthOfYear,Year):
    MonthLengths = Monthtuple(Year)
    assert DayOfMonth > 0 and DayOfMonth <= MonthLengths[MonthOfYear - 1]
    assert MonthOfYear > 0 and MonthOfYear <= 12
    MonthCounter = 1
    DaysSinceJanFirst = 0
    while MonthCounter < MonthOfYear:
        DaysSinceJanFirst = DaysSinceJanFirst + MonthLengths[MonthCounter-1]
        MonthCounter = MonthCounter + 1
    return DaysSinceJanFirst + DayOfMonth

def DayOfYearInverse(DayOfYear,Year):
    MonthIn = 1
    DaysLeftOver = DayOfYear
    while DaysLeftOver > Monthtuple(Year)[MonthIn-1]:
        DaysLeftOver = DaysLeftOver - Monthtuple(Year)[MonthIn-1]
        MonthIn = MonthIn + 1
    return (DaysLeftOver,MonthIn)    

def DayOfWeekConvertFromNumber(Day):
    if Day%7 == 0:
        return "Monday"
    elif Day%7 == 1:
        return "Tuesday"
    elif Day%7 == 2:
        return "Wednesday"
    elif Day%7 == 3:
        return "Thursday"
    elif Day%7 == 4:
        return "Friday"
    elif Day%7 == 5:
        return "Saturday"
    else:
        return "Sunday"

def DaysBetweenDatesInSameYear(DayOfMonth1,MonthOfYear1,DayOfMonth2,MonthOfYear2,Year):
    return DayOfYear(DayOfMonth2,MonthOfYear2,Year) - DayOfYear(DayOfMonth1,MonthOfYear1,Year)

def DaysBetweenDates(DayOfMonth1,MonthOfYear1,Year1,DayOfMonth2,MonthOfYear2,Year2):
    Days = 0
    Counter = Year1
    assert Year2 - Year1 >= 0
    while Counter < Year2:
        Days = Days + DayOfYear(31,12,Counter)
        Counter = Counter + 1
        
    Input1 = DayOfYearInverse(DayOfYear(DayOfMonth1,MonthOfYear1,Year1),Year2)
    Input2 = DayOfYearInverse(DayOfYear(DayOfMonth2,MonthOfYear2,Year2),Year2)
    
    return Days + DaysBetweenDatesInSameYear(Input1[0], Input1[1],Input2[0],Input2[1],Year2)
SundayCount = 0
for Year in range(1901,2001):
    for Month in range(1,13):
        for Day in range(1,Monthtuple(Year)[Month-1]+1):
#            print((DayOfWeekConvertFromNumber(DaysBetweenDates(1,1,1900,Day,Month,Year))),Day,Month,Year)
            if Day == 1 and DayOfWeekConvertFromNumber(DaysBetweenDates(1,1,1900,Day,Month,Year)) == "Sunday":
                SundayCount = SundayCount + 1
#print(DaysBetweenDates(29,8,2017,31,12,2017))              
print(SundayCount)
#print(DaysBetweenDates(1,1,1900,31,12,2000))
#Input1 = DayOfYearInverse(DayOfYear(DayOfMonth1,MonthOfYear1,Year1),Year2)
#Input2 = DayOfYearInverse(DayOfYear(DayOfMonth2,MonthOfYear2,Year2),Year2)
#print(DayOfYearInverse(100,1999))     
#print(DaysBetweenDatesInSameYear(1,1,1,1,2000))
#print(DayOfWeekConvertFromNumber(-2))   
#print(DayOfYear(31,12,2016))