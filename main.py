from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def share():
    return render_template('share.html', app_key='c03ce9560aa54cba52b9fc2c4db6b3aa')

if __name__ == '__main__':
    app.run(debug=True, port=8787)