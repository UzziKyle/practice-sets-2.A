# 2. Create a function that determines whether a given year is a leap year or not. 
def is_leap_year(year: int) -> bool:
    '''
    Determines whether a given year is leap year or not

    Args:
        year - The year to be determined

    Return
        A boolean to answer if given year is a leap year or not
    '''
    if year % 4 != 0:
        return False
    elif year % 100 == 0:
        if year % 400 != 0:
            return False
    
    return True


def main():
    print('Let\'s check if your year is a leap year!')
    year = int(input('*Enter year: ').strip())
    print(f'Is given year a leap year? - {is_leap_year(year)}')


if __name__ == '__main__':
    main()