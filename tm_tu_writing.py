import pandas as pd
from transliterate import translit

# Загрузите Excel-файл
file_path = 'xyz.xlsx'  # Замените на путь к вашему файлу
output_file = 'output_with_translit.xlsx'

# Чтение данных из файла
df = pd.read_excel(file_path)

# Функция для обработки строки: транслитерация, удаление лишних символов, ограничение длины
def generate_description(row):
    # Проверяем, что значение в столбце "Название" является строкой
    if isinstance(row['Название'], str):
        # Транслитерация строки
        latin_name = translit(row['Название'], 'ru', reversed=True)
        # Убираем нежелательные символы
        latin_name = latin_name.replace('"', '').replace("'", "").replace(" ", "")
    else:
        # Если значение не строка, подставляем 'REZERV'
        latin_name = "REZERV"

    # Формируем строку как "[Столбец F]_[Транслитерированный столбец D]"
    combined_string = f"{row['Адрес объекта']}_{latin_name}"
    # Ограничиваем длину строки до 32 символов
    return combined_string[:32]

# Создаем новый столбец 'descriptionTU' на основе функции
df['descriptionTU'] = df.apply(generate_description, axis=1)

# Сохраняем результат в новый Excel-файл
df.to_excel(output_file, index=False)

print(f"Результат сохранен в {output_file}")

