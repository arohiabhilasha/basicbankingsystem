from flask import Flask, render_template

app = Flask("tsf_b")
app.config['DEBUG'] = True

@app.route('/')
def index():
    return render_template("index.html")

app.run()