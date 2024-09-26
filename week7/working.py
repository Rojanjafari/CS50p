import re

def main():
    print(convert(input("Hours: ")))

def convert(s):
    AM = {'12':'00', '1':'01', '2':'02', '3':'03', '4':'04', '5':'05', '6':'06', '7':'07', '8':'08', '9':'09', '10':'10', '11':'11'}
    PM = {'12':'12', '1':'13', '2':'14', '3':'15', '4':'16', '5':'17', '6':'18', '7':'19', '8':'20', '9':'21', '10':'22', '11':'23'}

    match = re.search(r"^(\d+)(\:)?(\d\d)? ([A,P]?)M to (\d+)(\:)?(\d\d)? ([A,P]?)M$", s)

    if match:
        start_hour = match.group(1)
        if int(start_hour) > 12:
            raise ValueError
        
        if match.group(3) != None:
            start_min = match.group(3)
            if int(start_min) > 59:
                raise ValueError
        else:
            start_min = '00'
            
            
        end_hour = match.group(5)
        if int(end_hour) > 12:
            raise ValueError
        
        if match.group(7) != None:
            end_min = match.group(7)
            if int(end_min) > 59:
                raise ValueError
        else:
            end_min = '00'

        start_meridiem = f"{match.group(4)}M"
        if start_meridiem == 'AM':
            start24 = AM[start_hour]
        elif start_meridiem == 'PM':
            start24 = PM[start_hour]

        end_meridiem = f"{match.group(8)}M"
        if end_meridiem == 'AM':
            end24 = AM[end_hour]
        elif end_meridiem == 'PM':
            end24 = PM[end_hour]
        
        format24 = f"{start24}:{start_min} to {end24}:{end_min}"
        return format24
    
    else:
        raise ValueError
    

if __name__ == "__main__":
    main()