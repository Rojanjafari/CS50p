months = {"January":1, "February":2, "March":3, "April":4, "May":5, "June":6, "July":7,
          "August":8, "September":9, "October":10, "November":11, "December":12}
while True:
    try:
        user_date = input('Enter the date: ').strip()
        if user_date.find('/') != -1:
            month, day, year = user_date.split('/')
        else:
            month_let, day, year = user_date.split(' ')

            if month_let.isalpha() == False:
                 raise ValueError
            if day.find(',') == -1:
                 raise ValueError

            day = day.replace(',' , '')
            month = str(months[month_let])

        if int(month) not in months.values():
                raise ValueError
        if int(day) not in range(1, 31):
            raise ValueError

        if len(day) == 1:
                day = '0' + day
        if len(month) == 1:
            month = '0' + month

        print(f"{year}-{month}-{day}")
        break

    except ValueError:
        pass