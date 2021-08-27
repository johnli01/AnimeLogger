from flask import Flask, request

app = Flask(__name__)

@app.route('/anime_data', methods=['GET', 'POST'])
def retrieveData():
  with app.app_context():
    global data
    if request.method == 'POST':
      print("RUNNING")
      if not request.form['title'] or not request.form['jtitle'] or not request.form['ep']:
        print('Enter all fields properly')
        print('RUNNING 2.0')
      else:
        print(request.form['title'])
        print(request.form['jtitle'])
        print(request.form['ep'])
        print('RUNNING 3.0')


if __name__ == '__main__':
  app.run(debug=True)