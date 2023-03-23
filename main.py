import pandas as pd
import openpyxl
import datetime

book = openpyxl.load_workbook('Статистика библа 21-23.xlsx')
sheet = book['Библиотека 2023']
row = sheet.max_row
week_start = sheet['C2'].value
day_people = {}
for n in range(7):
    day_from_first = datetime.timedelta(n)
    day = (week_start + day_from_first).strftime("%m.%d")
    print(day)
    count = []
    for t in range(7):
        uni_let = ord('C') + t
        for i in range (5, 12):
            count.append(sheet[chr(uni_let) + str(i)].value)
    day_people[day] = count

for key, val in day_people.items():
    print(key, val)

'''
wb = xw.Book('Статистика библа 21-23.xlsx') # Открываем книгу
data_excel = wb.sheets['Библиотека 2023'] # Читаем лист Данные
print(data_excel.cell_value(rowx=6, colx=3))

data_pd = data_excel.range('B3:I15').options(pd.DataFrame, header=3, index=False).value # Создаем DataFrame
print(data_pd)
val = data_pd.loc[[5], [3]]
print(val)

xl = pd.read_excel(
    io='Статистика библа 21-23.xlsx',
    sheet_name=['Библиотека 2023'],
    usecols='B:I',
    header=2
)
for key in xl.keys():
    print(key)
xl = pd.DataFrame(xl, index=[181])

print(xl.iloc[:, 6])
'''