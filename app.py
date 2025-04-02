from flask import Flask
app = Flask(__name__)
@app.route('/')
def home():
    return "Hello, Jenkins Deployment Successful!"
if __name__ == '__main__':
    app.run(host='3.12.107.215', port=5000)

