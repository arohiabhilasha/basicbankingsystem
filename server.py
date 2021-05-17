from flask import Flask, render_template

app = Flask("tsf_b")
app.config['DEBUG'] = True

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/customer')
def cust():
    customer = {"Abhinav":3000000, "Ritul":50000, "Abhilasha": 20000, "Vaibhav": 12000}
    return render_template("customer.html", arrayx=customer)

app.run()