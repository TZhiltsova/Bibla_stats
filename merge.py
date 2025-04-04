import pandas as pd

pd.set_option('display.max_columns', None)

j_list = pd.read_csv('scimagojr 2023-3.csv', encoding='UTF-8', sep = ';')
white_list = pd.read_csv('белый список_26.03.2025.csv', encoding='UTF-8', sep = '\t', dtype={"ajg21": str,
                                                                                              "zbm_id": str})
j_list = j_list.rename(columns={'Title': 'title'})

white_list['title'] = white_list['title'].apply(lambda x: x.lower())
j_list['title'] = j_list['title'].apply(lambda x: x.lower())

white_names = white_list['title'].to_list()

j_list['title'] = j_list['title'].apply(lambda x : None if (x not in white_names) else x)
j_list = j_list.dropna(subset=['title'])

white_list = white_list.merge(j_list, how='outer')

white_list.to_csv('white_filter.csv', encoding='UTF-8', sep = ';')
