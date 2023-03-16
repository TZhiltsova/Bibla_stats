import pandas as pd


xl = pd.read_excel(
    io='Статистика библа 21-23.xlsx',
    sheet_name=['Библиотека 2023'],
    usecols='B:I',
    header=2
)
for key in xl.keys():
    print(key)
    '''
xl = pd.DataFrame(xl, index=[181])

print(xl.iloc[:, 6])
'''