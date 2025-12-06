from helpers import *
directory = [{'Name': 'Fox, Susan', 'Phone': '6553', 'Building': 'Olin-Rice', 'OfficeNum': '230'},
             {'Name': 'Cranford, James', 'Phone': '2083', 'Building': 'Olin-Rice', 'OfficeNum': '143'},
             {'Name': 'Syed, Una', 'Phone': '1059', 'Building': 'Campus Center', 'OfficeNum': '399'},
             {'Name': 'Thimus, Reg', 'Phone': '9989', 'Building': 'Leonard', 'OfficeNum': '22'},
             {'Name': 'Warner, Elen', 'Phone': '1113', 'Building': 'Old Main', 'OfficeNum': '402'},
             {'Name': 'Best, Fleur', 'Phone': '9281', 'Building': 'Carnegie', 'OfficeNum': '003'},
             {'Name': 'Ryan, Frazer', 'Phone': '1923', 'Building': 'Old Main', 'OfficeNum': '281'},
             {'Name': 'Mueller, Marcel', 'Phone': '9011', 'Building': 'Leonard', 'OfficeNum': '234'},
             {'Name': 'Glover, Stephanie', 'Phone': '2341', 'Building': 'Carnegie', 'OfficeNum': '832'},
             {'Name': 'Glass, Abdullah', 'Phone': '1122', 'Building': '77 Mac', 'OfficeNum': '102'},
             {'Name': 'Petersen, Rosa', 'Phone': '2392', 'Building': 'Olin-Rice', 'OfficeNum': '333'},
             {'Name': 'Mora, Mohamed', 'Phone': '2229', 'Building': 'Campus Center', 'OfficeNum': '012'},
             {'Name': 'Friedman, Maryam', 'Phone': '3142', 'Building': 'Old Main', 'OfficeNum': '194'},
             {'Name': 'Li, Elena', 'Phone': '1923', 'Building': 'Olin-Rice', 'OfficeNum': '119'}]

def lookup_phone(name, direct_table):
    for row in direct_table:
        if row['Name'] == name:
            return row['Phone']

    return "No entry: " + name

def lookup_office(name, direct_table):
    for row in direct_table:
        if row['Name'] == name:
            return row['Building'], row['OfficeNum']

    return "No entry: " + name, None
def lookup_by_date(month, day, sun_table):
    day_str = str(day)
    for row in sun_table:
        if row['Month'] == month and row['Day'] == day_str:
            return row

    return None
def collect_by_building(building, table):
    match_list = []
    for row in table:
        if row['Building'] == building:
            match_list.append(row)

    return match_list

def collect_by_letter(letter, table):

    match_list = []
    for row in table:
        if row['Name'][0] == letter:
            match_list.append(row)

    return match_list

def select_by_month(month, sun_table):
    match_list = []
    for row in sun_table:
        if row['Month'] == month:
            match_list.append(row)

    return match_list
def count_sunsets_before(hour_time, table):
    count = 0
    for row in table:
        sunset_hr = row['SunSetHour']
        if int(sunset_hr) < hour_time:
            count += 1

    return count


def daylight_hours(rise_hour, rise_min, set_hour, set_min):
    rise_time = (60 * rise_hour) + rise_min
    set_time = (60 * set_hour) + set_min
    minute_diff = set_time - rise_time
    hour_diff = minute_diff / 60
    return hour_diff

def average_daylight_time(table):
    if not table:  # handle case where table is empty
        return 0

    total_daylight = 0
    for row in table:
        rise_h = int(row['SunRiseHour'])
        rise_m = int(row['SunRiseMin'])
        set_h = int(row['SunSetHour'])
        set_m = int(row['SunSetMin'])
        hours = daylight_hours(rise_h, rise_m, set_h, set_m)
        total_daylight += hours

    return total_daylight / len(table)
def main():
    print("--- Testing Directory Functions ---")
    print("Phone for 'Fox, Susan':", lookup_phone('Fox, Susan', directory))
    print("Phone for 'Shoop, Libby':", lookup_phone('Shoop, Libby', directory))

    print("\nOffice for 'Syed, Una':", lookup_office('Syed, Una', directory))
    building, office = lookup_office('Warner, Elen', directory)
    print(f"Office for 'Warner, Elen': Building {building}, Office {office}")
    print("Office for 'John Doe':", lookup_office('John Doe', directory))

    print("\nPeople in Olin-Rice:")
    olri = collect_by_building('Olin-Rice', directory)
    print_table(olri, ['Name', 'Phone', 'Building', 'OfficeNum'])

    print("\nPeople whose name starts with 'F':")
    f_people = collect_by_letter('F', directory)
    print_table(f_people, ['Name', 'Phone', 'Building', 'OfficeNum'])

    print("\n\n--- Testing Sunrise/Sunset Functions ---")
    field_names, sun_table = read_csv("DataFiles/sunRiseSet.csv")
    print("First row of sunrise/sunset data:", sun_table[0])

    print("\nData for May 15:")
    may15_data = lookup_by_date('May', 15, sun_table)
    print(may15_data)
    print("\nData for October 31:")
    oct31_data = lookup_by_date('October', '31', sun_table)
    print(oct31_data)

    print("\nData for January:")
    january_data = select_by_month('January', sun_table)
    print_table(january_data, field_names, 15)

    print("\nSunset Counts:")
    print("Sunsets before 6pm (18:00) =", count_sunsets_before(18, sun_table))
    print("Sunsets before 10pm (22:00) =", count_sunsets_before(22, sun_table))

    print("\nAverage Daylight Hours:")
    print(f"Average daylight for the whole year: {average_daylight_time(sun_table):.2f} hours")
    july_data = select_by_month('July', sun_table)
    print(f"Average daylight for July: {average_daylight_time(july_data):.2f} hours")
    december_data = select_by_month('December', sun_table)
    print(f"Average daylight for December: {average_daylight_time(december_data):.2f} hours")


if __name__ == '__main__':
    main()