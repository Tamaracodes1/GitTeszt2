def file_readin():
    with open('astronauts.csv', 'r', encoding='utf-8') as astronauts:
        astronauts.readline()
        important_data = []
        for line in astronauts:
            data = line.strip().split(',')
            month, day, year = data[4].split('/')
            important_data.append(month)
        return important_data


def birth_date(month_list):
    new_month_list = [eval(i) for i in month_list]
    numerator = 1
    how_many = []
    for i in range(12):
        count = new_month_list.count(numerator)
        how_many.append(count)
        numerator += 1
    return how_many


def percent(dates):
    hightest = sorted(dates)[-3:]
    numerator_1 = 2
    numerator_2 = 1
    for i in range(3):
        number = dates.index(hightest[numerator_1]) + 1
        print(f'A(z) {number}. hónapban {hightest[numerator_1]}-en születtek, ezzel ez a {numerator_2}. legtöbb '
              f'születésű hónap az asztronauták között, ez az összes szüetésnek a(z) '
              f'{round(hightest[numerator_1] / sum(dates) * 100, 1)}%-a.')
        numerator_1 -= 1
        numerator_2 += 1


def main():
    percent(birth_date(file_readin()))


main()
