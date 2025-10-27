def get_weekly_report(temperatures):
    # temperatures = list of 28 numbers (4 weeks)
    weekly_averages = []

    # TODO: slice the list into weeks

    first_week = temperatures[:7] # starts and ends (not including at) 7
    second_week = temperatures[7:14]  # starts at index 7 and stops at 14
    third_week = temperatures[14:21] # starts at 14, stops at 21
    fourth_week = temperatures[21:28] 

 
    totalOfWeekOne = sum(first_week) # get the sum of the 1st week
    aveOfWeekOne = totalOfWeekOne / 7 # divide by 7 to get the average
    weekly_averages.append(aveOfWeekOne) # add the average to the list

    totalOfWeekTwo = sum(second_week) 
    aveOfWeekTwo = totalOfWeekTwo / 7
    weekly_averages.append(aveOfWeekTwo)

    totalOfWeekThree = sum(third_week) 
    aveOfWeekThree = totalOfWeekThree / 7
    weekly_averages.append(aveOfWeekThree)

    totalOfWeekFour = sum(fourth_week) 
    aveOfWeekFour = totalOfWeekFour / 7
    weekly_averages.append(aveOfWeekFour)

    # cleaner version
    '''for i in range(0, len(temperatures), 7):
    print("i is:", i)
    print("week is:", temperatures[i:i+7])'''


    return weekly_averages


# Example data:
temps = [30, 31, 29, 28, 32, 31, 30, 33, 32, 31, 30, 29, 30, 31,
         28, 27, 29, 30, 31, 29, 30, 28, 27, 26, 29, 30, 28, 27]

result = get_weekly_report(temps)
print(result)
