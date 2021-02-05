from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'I love you Xiaofan!'
    
@app.route('/<name>')
def hello_name(name):
    return f'Hello {name}! This is Jiahao\'s website'

if __name__=="__main__":
    app.run(debug = True)