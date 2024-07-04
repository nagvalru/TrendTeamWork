import pandas as pd
import os

folder_path = r'C:\Users\TSLab\Downloads' # Переменная, содержащая путь к папке
file_name = 'Donch_stopATR_StartStop_10min_Fut1_trades.csv' # Переменная, содержащая название файла
full_file_path = os.path.join(folder_path, file_name) # Переменная, содержащая полный путь к файлу

strategy_trades_df = pd.read_csv(full_file_path) # Считываем данные из CSV файла в DataFrame

pd.set_option('display.max_columns', None) # Устанавливаем опцию для отображения всех столбцов

# print(strategy_trades_df.head(5)) # Выводим первые несколько строк для проверки

# Создаем новый DataFrame с названиями столбцов
columns_df = pd.DataFrame(strategy_trades_df.columns, columns=['Column Names'])

# Выводим новый DataFrame
print(columns_df)

# Внесли изменния в 11:20 компьютер win10


