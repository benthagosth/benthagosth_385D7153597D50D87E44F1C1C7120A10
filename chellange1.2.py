start_year = int(input("Please select a starting year: "))
num_of_years = int(input("Please select how many years you'd like to check: "))
end_year = start_year + num_of_years



for year in range(start_year-1, end_year):
    year += 1    
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        print ("{}: Is a leap year".format(year))
    else:
        print (year)
      