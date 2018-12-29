import os
from flask import Flask , render_template
app=Flask(__name__)


@app.route('/')
def main_index():
    return render_template('index.html')


@app.route('/places')
def places():
    return render_template('places.html')


@app.route('/gallery')
def gallery():
    return render_template('gallery.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
   app.run(debug=True)