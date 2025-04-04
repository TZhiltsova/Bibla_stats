import pandas as pd

pd.set_option('display.max_rows', None)

books = pd.read_csv('excel_biblio_stat_books_movement (1).csv', encoding='UTF-8', sep=';')
#print(books[books['Тип книги'] == 'Аудиокнига']['Наименование книги'].value_counts())
print(books['Наименование книги'].value_counts())