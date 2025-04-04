from idlelib.iomenu import encoding

import pandas as pd


def dict_df(dict, row1, row2):
    dict[row1] = int(row2)

pd.set_option('display.max_columns', None)

bye_book = pd.read_csv('покнижно корзина.csv', encoding='UTF-8', sep = ';')
requests = pd.read_csv('report (2).csv', encoding='UTF-8', sep = ';', dtype={"Reporting Period Total": int})

bye_book_dict = {}

requests[['ISBN', 'Reporting Period Total']].apply(lambda x: (dict_df(bye_book_dict, x['ISBN'], x['Reporting Period Total'])), axis = 1)
bye_book['Выдачи'] = bye_book['ISBN'].apply(lambda x : 0 if (x not in bye_book_dict.keys()) else bye_book_dict[x])

bye_book.to_csv('isbn.csv', encoding = 'cp1251')

'''bye_book_list = requests['ISBN'].to_list()
print(bye_book_list)


bye_book['Выдачи'] = bye_book['ISBN'].apply(lambda x : 'нет' if (x not in bye_book_list) else 'да')

bye_book.to_csv('isbn.csv', encoding = 'cp1251')'''