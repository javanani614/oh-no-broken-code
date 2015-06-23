from datetime import datetime

number_endings = {
    1: 'st',
    2: 'nd',
    3: 'rd'
}

today = datetime.now()
todays_day = today.day

# get the right ending, e.g. 1 => 1st, 2 => 2nd
# but beware! 11 => 11th, 21 => 21st, 31 => 31st

# test your code by forcing todays_day to be something different
#todays_day = 22

birthday = int(raw_input("What day of the month is your birthday?"))
ending = 'th'

if birthday< 10 or birthday > 20:
    # x % y (mod) will give the remainder when x is divided by y
    # -- but x needs to be an integer!
    number = birthday % 10
    # look up number in number_endings
    # and if you find it as a key, put the value in ending
    if number in number_endings:
        ending = number_endings[number]

    
# make this print ending, not 'th'
# make this print the birthday, and the right ending
print ("Your Birthday is on the {}"+ending).format(birthday)



