from flask import flask

app=Flask(__name__)

@app.route('/')
def index():
    pass

@app.route('/register')
def register():
    pass

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/question')
def question():
    return render_template('question.html')

@app.route('/answer')
def answer():
    pass

@app.route('ask')
def ask():
    pass

@app.route('/unanswered')
def unanswered():
    pass

@app.route('/users')
def users():
    pass

if __name__== '__main__':
    app.run(debug=True)