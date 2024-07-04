
#region импортируем библиотеки
import os
import pandas as pd #excel для python
#endregion

#region путь к csv файлу
path_to_file = r"C:\python_for_traders" # Переменная для указания пути

csv_file_name = "strategy_positions.csv" # Переменная, содержащая название файла

# Используем os.path.join для создания полного пути
csv_full_name = os.path.join(path_to_file, csv_file_name) # Переменная, содержащая полный путь
#endregion

#region Чтение CSV файла с помощью pandas
positions_df = pd.read_csv(csv_full_name) # pd.read_csv читает CSV файл и возвращает DataFrame

# Вывод названий столбцов
# df.columns возвращает названия столбцов DataFrame
print("Названия столбцов:")
print(positions_df.columns)

# # Вывод первых пяти строк
# # df.head() возвращает первые 5 строк DataFrame
# print("\nПервые шесть строк:")
# print(positions_df.head(6))
#
# # Вывод последних пяти строк
# # df.tail() возвращает последние 5 строк DataFrame
# print("\nПоследние три строки:")
# print(positions_df.tail(3))
#endregion

#Переворот датафрейма. Замена столбцов строками
position_df_t = positions_df.T

# Выводим первые несколько строк DataFrame для проверки результата
print(position_df_t)

# Выводим типы данных столбцов для проверки
print(positions_df.dtypes)

#region преобразуем два столбца входа

# Объединяем строки из столбцов 'Entry Date' и 'Entry Time' с пробелом между ними
# Это создаст строки вида '22.08.2017 11:23:00'
combined_datetime_strings = positions_df['Entry Date'] + ' ' + positions_df['Entry Time']

# Преобразуем объединенные строки в тип данных datetime
# Указываем формат, чтобы pandas знал, как интерпретировать строки
positions_df['Entry DateTime'] = pd.to_datetime(combined_datetime_strings, format='%d.%m.%Y %H:%M:%S')

#endregion

#region преобразуем два столбца выхода

# Объединяем строки из столбцов 'Entry Date' и 'Entry Time' с пробелом между ними
# Это создаст строки вида '22.08.2017 11:23:00'
combined_datetime_strings = positions_df['Exit Date'] + ' ' + positions_df['Exit Time']

# Преобразуем объединенные строки в тип данных datetime
# Указываем формат, чтобы pandas знал, как интерпретировать строки
positions_df['Exit DateTime'] = pd.to_datetime(combined_datetime_strings, format='%d.%m.%Y %H:%M:%S')

# вывод новых двух столбцов Датавремя
columns_to_keep = ['Entry DateTime', 'Exit DateTime']
positions_df = positions_df[columns_to_keep]


# Выводим первые несколько строк DataFrame для проверки результата
print(positions_df.head())

# Выводим типы данных столбцов для проверки
print(positions_df.dtypes)

#endregion


# Внесли изменния в 11:20 компьютер win10
# Внесли изменения в 11:29 на github


