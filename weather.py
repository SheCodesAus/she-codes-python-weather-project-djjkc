import csv
from datetime import datetime
from operator import index
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


def convert_date(iso_string):
    """Converts and ISO formatted date into a human readable format.

    Args:
        iso_string: An ISO date string..
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """
    date = datetime.fromisoformat(iso_string)
    return date.strftime("%A %d %B %Y")


def convert_f_to_c(temp_in_farenheit):
    """Converts an temperature from farenheit to celcius.

    Args:
        temp_in_farenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees celcius, rounded to 1dp.
    """
    temp_in_c = (float(temp_in_farenheit) - 32)/1.8
    return (round(temp_in_c, 1))


def calculate_mean(weather_data):
    """Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """
    A = 0
    num_length = len(weather_data)
    for num in weather_data:
        A += float(num)
    mean = float(A / num_length)
    return mean


def load_data_from_csv(csv_file):
    # """Reads a csv file and stores the data in a list.

    # Args:
    #     csv_file: a string representing the file path to a csv file.
    # Returns:
    #     A list of lists, where each sublist is a (non-empty) line in the csv file.
    # """
    a = []
    with open(csv_file, mode = 'r', encoding = "utf-8") as csv_file:
        csv_reader = csv.reader(csv_file,delimiter=",")
        for index,line in enumerate(csv_reader):
            if index !=0 and line != []:
                a.append([line[0],int(line[1]),int(line[2])])
    return a


def find_min(weather_data):
    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minium value and it's position in the list.
    """
    if weather_data == []:
        return ()
    else:
        min_temp = weather_data[0]
        min_location = 0
        index = 0
        for num in weather_data:
            if float(num) <= float(min_temp):
                min_temp = float(num)
                min_location = index
            index +=1
        return min_temp, min_location


def find_max(weather_data):
    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list.
    """
    if weather_data == []:
        return ()
    else:
        max_temp = weather_data[0]
        max_location = 0
        index = 0
        for num in weather_data:
            if float(num) >= float(max_temp):
                max_temp = float(num)
                max_location = index
            index +=1
        return max_temp, max_location


def generate_summary(weather_data):
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    min_temp_list = []
    max_temp_list = []
    summary = ""
    for line in weather_data:
        min_temp_list.append(line[1])
        max_temp_list.append(line[2])
    min_temp, min_index = find_min(min_temp_list)
    max_temp, max_index = find_max(max_temp_list)
    min_date = weather_data[min_index][0]
    max_date = weather_data[max_index][0]
    avg_min = calculate_mean(min_temp_list)
    avg_max = calculate_mean(max_temp_list)
    summary = summary + f"{len(weather_data)} Day Overview\n"
    summary += f"  The lowest temperature will be {(format_temperature(convert_f_to_c(min_temp)))}, and will occur on {convert_date(min_date)}.\n"
    summary += f"  The highest temperature will be {format_temperature(convert_f_to_c(max_temp))}, and will occur on {convert_date(max_date)}.\n" 
    summary += f"  The average low this week is {format_temperature(convert_f_to_c(avg_min))}.\n" 
    summary += f"  The average high this week is {format_temperature(convert_f_to_c(avg_max))}.\n"
    return summary



def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    daily_final = ""
    for line in weather_data:
        daily_final = daily_final + f"---- {convert_date(line[0])} ----\n  Minimum Temperature: {format_temperature(convert_f_to_c(line[1]))}\n  Maximum Temperature: {format_temperature(convert_f_to_c(line[2]))}\n\n"
    return daily_final
