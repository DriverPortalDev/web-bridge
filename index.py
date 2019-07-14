from japronto import Application

def hello(request):
    return request.Response(text='Hello world!')

app = Application()

app.router.add_route('/', hello)

app.run(debug=True,host='127.0.0.1', port=3000)