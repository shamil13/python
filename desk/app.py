from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Хранилище для запросов (просто для примера, в реальном проекте используйте базу данных)
requests_storage = []


@app.route('/')
def index():
    return render_template('index.html', requests=requests_storage)


@app.route('/submit_request', methods=['POST'])
def submit_request():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        issue = request.form['issue']

        # Добавление запроса в хранилище
        requests_storage.append({'name': name, 'email': email, 'issue': issue})

    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
