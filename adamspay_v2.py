from distutils.log import debug
from flask import json
from flask import request
from flask import Flask

app = Flask(__name__)
@app.route('/')
def app_root():
  return 'hola'

  if __name__ == '__main__':
    app.run(debug=true)