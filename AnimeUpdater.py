from flask import Flask, request
import requests

# MAL Access key (necessary to make changes and retrieve data on user's MAL list)
key = {"Authorization": "Bearer ACCESS KEY"}

app = Flask(__name__)


# Retrieves the sent anime data from the Google Chrome Extension in a JSON type
@app.route('/anime_data', methods=['GET', 'POST'])
def retrieveData():
  with app.app_context():
    if request.method == 'POST':
      # Checks to see if the sent JSON data contains all the correct information
      if not request.form['title'] or not request.form['jtitle'] or not request.form['ep']:
        print('Enter all fields properly')
      else:
        # Saves JSON information into variables
        title = request.form['title']
        jtitle = request.form['jtitle']
        ep = request.form['ep']

        # Uses sent data from Chrome Extension to update user's anime entry on MAL
        updateMAL(title, jtitle, ep)
    return 'OK'


# Updates the anime on MAL to the most recently watched ep on anime website
def updateMAL(title, jtitle, ep):
  print(title + " | " + jtitle)
  # Searches for the ID of the anime user is currently watching
  id = findAnimeID(title, jtitle)
  if id == None:
    print(title + " | " + jtitle + " : CANNOT BE FOUND IN USERS MAL LIST" )
  else:
    print("Works")


# Searches the users current anime list on MAL and returns the specific anime id value,
# Returns None if anime entry does not exist on MAL
def findAnimeID(title, jtitle):
  r = requests.get('https://api.myanimelist.net/v2/users/@me/animelist?fields=list_status&limit=1000', headers=key).json()
  r = r['data']
  # Loops through user's MAL list in search for anime user is currently watching
  for anime in r:
    name = anime['node']['title']
    if name.lower() == title.lower() or name.lower() == jtitle.lower():
      print(anime)
      return anime['node']['id']


if __name__ == '__main__':
  app.run()