import csv
from datetime import datetime
# 1 2 3
DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"


def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees
        and celcius symbols.

    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees celcius."
    """
    return f"{temp}{DEGREE_SYBMOL}"


# print(format_temperature('57')) #example in class - testing how the function is working, outside the function-DO NOT leave in assignment

def convert_date(iso_string):
    """Converts and ISO formatted date into a human readable format.

    Args:
        iso_string: An ISO date string..
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """
    # format = "%A %d %B %Y"
    # date_string = datetime.strftime(iso_string)
    # date = datetime.strptime(date_string, format)
    # # date = datetime.strptime(iso_string, format)
    # return (date)
    # pass


def convert_f_to_c(temp_in_farenheit):
    """Converts an temperature from farenheit to celcius.

    Args:
        temp_in_farenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees celcius, rounded to 1dp.
    """
    temp_in_c = (float(temp_in_farenheit) - 32)/1.8
    return (round(temp_in_c, 1))
    # pass

# print(convert_f_to_c (100))

def calculate_mean(weather_data):
    """Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """
    A = 0
    num_length = len(weather_data)
    for num in weather_data[1]:
        A += num
    mean = float(A / num_length)
    return mean
    # pass


def load_data_from_csv(csv_file):
    """Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """
    pass


def find_min(weather_data):
    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minium value and it's position in the list.
    """
    # min_temp = weather_data[0]
    # for num in weather_data:
    #     if num < min_temp:
    #         min_temp = num
    # return min_temp

    min_temp = weather_data[0]
    min_location = 0
    min_index = 0
    for num in weather_data[0]:
        if num < min_temp:
            min_temp = num
            min_location = min_index
        min_index +=1

    pass


def find_max(weather_data):
    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list.
    """
    max_temp = weather_data[1]
    for num in weather_data:
        if num > max_temp:
            max_temp = num
    return max_temp
    pass


def generate_summary(weather_data):
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    pass


def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    pass
