from flask import Flask, render_template, request
from BaseModel import *
app = Flask(__name__)

@app.route('/search', methods=['GET', 'POST'])
def search():
    query = request.form['query']
    results = BoleanModel(query)
    return render_template('search.html', query=query, results=results)

if __name__ == '__main__':
    app.run(debug=True)
