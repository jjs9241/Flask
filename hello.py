from flask import Flask, escape, request,render_template
import random

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

@app.route('/lunch')
def lunch():
    # menu=[['부대찌개','https://post-phinf.pstatic.net/20160727_124/14696074495060Ff2u_JPEG/thLWUI1LMK.jpg?type=w1200'],
    # ['함박스테이크','http://blogfiles.naver.net/20140723_186/irumys_1406090954335iXCuS_JPEG/%C7%D4%B9%DA%BD%BA%C5%D7%C0%CC%C5%A9%B8%C0%C1%FD3.jpg']]
    # rand=random.choice(menu)
    # return '<image src={}>{}</image>'.format(rand[1],rand[0])
    
    menus ={'부대찌개':'https://post-phinf.pstatic.net/20160727_124/14696074495060Ff2u_JPEG/thLWUI1LMK.jpg?type=w1200',
    '함박스테이크':'http://blogfiles.naver.net/20140723_186/irumys_1406090954335iXCuS_JPEG/%C7%D4%B9%DA%BD%BA%C5%D7%C0%CC%C5%A9%B8%C0%C1%FD3.jpg'}
    pick=random.choice(list(menus.keys()))    
    return '<image src={}>{}</image>'.format(menus[pick],pick)

@app.route('/movies')
def movies():
    movies=['겨울왕국','쥬만지','신의한수2']
    return render_template('movies.html',movies=movies)


if __name__=='__main__':
    app.run(debug=True)
