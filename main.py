from flask import Flask,render_template,request


from flask_paginate import Pagination,get_page_args
# just serve all the static files under root
app = Flask(__name__, static_folder='.', static_url_path='')

users = list(range(100))

@app.route('/')
def index():
  return render_template('index.html')


@app.route('/portfolio')
def portfolio():
  return render_template('portfolio.html')
# for / root, return Hello Word

# Remember from flask import request
# for /request and POST method
@app.route("/contact")
def contact():
  return render_template("contact.html")

@app.route("/skil")
def skil():
  return render_template("skil.html")
  
  
  
# start listening
if __name__ == "__main__":
    app.run(debug=True, port='3000', host='0.0.0.0')

