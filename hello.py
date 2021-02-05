from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'I love you Xiaofan!'

@app.route('/admin')
def hello_admin():
    return f'Hello admin. You can edit this page'

@app.route('/<guest>')
def hello_guest(guest):
    return f'Hello {guest} as guest'

@app.route('/<name>')
def hello_name(name):
    if name == 'admin':
        return redirect(url_for('hello_admin'))
    else:
        return redirect(url_for('hello_guest', guest = name))
        
if __name__=="__main__":
    app.run(debug = True)