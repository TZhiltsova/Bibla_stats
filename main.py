import pandas as pd
import openpyxl

book = openpyxl.load_workbook('Статистика библа 21-23.xlsx')
sheet = book['Библиотека 2023']
print(sheet['D6'].value)
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