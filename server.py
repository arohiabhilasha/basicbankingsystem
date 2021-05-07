from flask import Flask, render_template

app = Flask("tsf_b")
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/customer')
def index():
    return render_template("customer.html")

app.run()