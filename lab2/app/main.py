from flask import Flask, request, make_response, render_template

app = Flask(__name__)

application = app

@app.route('/', methods=['GET', 'POST'])
def requestData():
    user_data = None
    if request.method == 'POST':
        user_data = {
            'name' : request.form.get('name'), 
            'email' : request.form.get('email'),
            'message' : request.form.get('message'),
            'URLparams' : dict(request.args),
            'headers' : dict(request.headers),
            'cookies' : dict(request.cookies),
        }
    return render_template('requestData.html', title = 'Отображние данных запроса', user_data = user_data)

@app.route('/phone', methods=['GET', 'POST'])
def phone():
    user_data = ''
    error = None
    result = ''
    if request.method == 'POST':
        user_data = request.form.get('number', '')
        numbers = ''
        for i in user_data:
            if i.isdigit():
                numbers += i
            elif i not in ' ()-.+':
                error = "Недопустимый ввод. В номере телефона встречаются недопустимые символы."
                break
        if not error:
            if len(numbers) == 11 and (numbers[0] == '7' or numbers[0] == '8'):
                result = f'8-{numbers[1:4]}-{numbers[4:7]}-{numbers[7:9]}-{numbers[-2:]}' 
            elif len(numbers) == 10:
                result = f'8-{numbers[0:3]}-{numbers[3:6]}-{numbers[6:8]}-{numbers[-2:]}'
            else:
                result = ''
                error = 'Недопустимый ввод. Неверное количество цифр.'
    return render_template('phone.html', 
                                   title = 'Форма с обработкой ошибок', 
                                   user_data = user_data, 
                                   error = error, 
                                   result = result)

if __name__ == '__main__':
    app.run(debug=True)