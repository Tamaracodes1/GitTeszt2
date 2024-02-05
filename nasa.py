def file_readin():
    with open('astronauts.csv', 'r', encoding='utf-8') as astronauts:
        astronauts.readline()
        imp_data = []
        for line in astronauts:
            data = line.strip().split(',')
            month, day, year = data[4].split('/')
            imp_data.append(month)
        return imp_data


def birth_date(month_list):
    res = [eval(i) for i in month_list]
    x = 1
    how_many = []
    for i in range(12):
        count = res.count(x)
        how_many.append(count)
        x += 1
    print(how_many)
    return how_many


def percent(dates):
    hightest = sorted(dates)[-3:]
    x = 2
    y = 1
    for i in range(3):
        number = dates.index(hightest[x]) + 1
        print(f'A(z) {number}. hónapban {hightest[x]}-en születtek, ezzel ez a {y}. legtöbb születésű hónap'
              f' az asztronauták között, ez az összes szüetésnek a(z) {round(hightest[x]/sum(dates)*100, 1)}%-a.')
        x -= 1
        y += 1


def main():
    percent(birth_date(file_readin()))


main()
