from flask import Flask, request, make_response, Response

app = Flask(__name__)

@app.route('/')
def index():
    print (request.method) #GET/POST/PUT/DELETE/etc.
    print (request.headers) #dictionary of HTTP-headers (находится внутри самого запроса. куда направляется, инфа о браузере, с которого запрос и тд)
    print (request.args) #dictionary of URL params (в адресной строке. все что после ? парам = знач & ...)
    print (request.form) #dictionary of form data (все, что заполянем в формах, например, при авторизации username=alina&password=123456)
    print (request.cookies) #dictionary of cookies-files (в браузере пользователя)

# methods of request object Flask
# get - ключ - аргумент, возвращает соответствующее значение из аргументов запроса или данных формы
# getlist - ключ - аргумент, возвращает список значений из аргументов запроса или данных формы
# files - cвойство files содержит словарь файлов, загруженных в запросе. Каждый файл
# представлен объектом FileStorage, который предоставляет методы для доступа к
# данным файла, имени файла, типу содержимого и другим метаданным

@app.route('/')
def search():
    query = request.args.get('q')
    return f'Searching for: {query}'


#Создание объектов ответа через функцию make_response
response = make_response('Hello')#принимает тело ответа - возвращает объект Response
#Создание объектов ответа напрямую через импорт класса + передачи тела ответа в качетсве аргуемнта конструктору
response = Response('Hello')

#Для двух этих способов в качестве второго аргумента можно передать код состояния
response = make_response('Hello', 404)
response = Response('Hello', 404)

#Отправка изображений/др. файлов как байты 
@app.route('/image')
def image():
    with open('image.jpg', 'rb') as f: #открываем файл в бинарном режиме read binary
        image_data = f.read()

    response = make_response(image_data) #ответ с содержимым изображениием
    
    response.headers.set('Content-Type', 'image/jpeg') #заголовок с типом содержимого 
    
    return response