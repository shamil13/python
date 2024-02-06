from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

# Путь к вашему Excel файлу на сетевом диске
excel_file_path = r'E:\\test.xlsx'

# Загрузка данных из Excel файла
df = pd.read_excel(excel_file_path)

# Роут для отображения таблицы на веб-странице
@app.route('/')
def display_table():
    # Преобразование данных в HTML-таблицу
    table_html = df.to_html(classes='table table-striped', index=False)

    # Отображение таблицы с использованием шаблона HTML
    return render_template('table.html', table=table_html)

if __name__ == '__main__':
    app.run(debug=True)
