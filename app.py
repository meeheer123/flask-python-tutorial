from flask import Flask, render_template

app = Flask(__name__)

JOBS = [{
  'id': 1,
  'title': 'Computer Teacher',
  'location': 'Pimpri, India',
  'salary': 'Rs. 10,00,000'
}, {
  'id': 2,
  'title': 'Chemistry Teacher',
  'location': 'Akurdi, India',
  'salary': 'Rs. 15,00,000'
}, {
  'id': 3,
  'title': 'Therapist',
  'location': 'Remote',
  'salary': 'Rs. 12,00,000'
}, {
  'id': 4,
  'title': 'Math Teacher',
  'location': 'Akurdi, India',
  'salary': 'Rs. 20,00,000'
}]


@app.route("/")
def mainHTML():
  return render_template('home.html', jobs=JOBS, title='Register For PCCOE')


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
