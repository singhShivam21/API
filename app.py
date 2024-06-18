from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    email = request.form['email']
    password = request.form['password']
    # Process the form data here (e.g., save it in a variable)
    # For demonstration, I'll just print the values
    print(f'Email: {email}, Password: {password}')
    return 'Data received successfully!'

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True )
