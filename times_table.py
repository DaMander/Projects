def create_timetable():
    time_table = []
    for row in range(1, 13):
        row_num = []
        for number in range(1, 13):
            row_num.append(row * number)
        time_table.append(row_num)
    return time_table


def print_time_table():
    timetable = create_timetable()
    for row in timetable:
        print(row)


print_time_table()
