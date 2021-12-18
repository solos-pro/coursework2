from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/',)
def page_index():
    return 'server works'
    # return render_template('index.html', posts=posts)

app.run(debug=True)
