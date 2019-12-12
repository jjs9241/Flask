from flask import Flask, escape, request,render_template

app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'

@app.route('/hi')
def hi():
    return 'hi'

@app.route('/html_tag')
def html_tag():
    return '<h1>안녕하세요</h1>'

@app.route('/html_file')
def html_file():
    return render_template('index.html')

@app.route('/variable')
def variable():
    name='장지승'
    return render_template('variable.html',html_name=name)

@app.route('/greeting/<string:name>/')
def greeting(name):
    def_name = name
    return render_template('greeting.html',html_name=def_name)

@app.route('/cube/<int:number>/')
def cube(number):
    return render_template('cube.html',html_number=number,cube_number=number**3)

if __name__=='__main__':
    app.run(debug=True)
