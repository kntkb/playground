from flask import Flask, render_template, request, redirect, url_for
#from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sample.db'
#db = SQLAlchemy(app)


#--- useful links
# https://www.cyokodog.net/blog/web-speechi-api/
# https://qiita.com/hmmrjn/items/4b77a86030ed0071f548

@app.route('/')
def index():
    #return render_template('index.html')
    return render_template('sample.html')


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")