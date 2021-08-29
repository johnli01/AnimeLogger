from flask import Flask, request
import requests

app = Flask(__name__)

@app.route('/anime_data', methods=['GET', 'POST'])
def retrieveData():
  with app.app_context():
    global data
    if request.method == 'POST':
      print("RUNNING")
      if not request.form['title'] or not request.form['jtitle'] or not request.form['ep']:
        print('Enter all fields properly')
      else:
        print(request.form['title'])
        title = request.form['title']
        jtitle = request.form['jtitle']
        ep = request.form['ep']

        print(request.form['jtitle'])
        print(request.form['ep'])
        print('RUNNING 3.0')
        updateMAL(title, jtitle, ep)
    return 'OK'

def updateMAL(title, jtitle, ep):
  r = requests.get('https://api.myanimelist.net/v2/anime/suggestions?limit=4')
  print(r.status_code)


if __name__ == '__main__':
  app.run()