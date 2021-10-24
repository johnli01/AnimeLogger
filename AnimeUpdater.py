from flask import Flask, request
from flask.globals import current_app
import requests

# MAL Access key (necessary to make changes and retrieve data on user's MAL list)
key = {"Authorization": "Bearer "}

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
        updateMAL(title, jtitle, int(ep))
    return 'OK'


# Updates the anime on MAL to the most recently watched ep on anime website
def updateMAL(title, jtitle, ep):
  print("NAME: " + title + " | " + jtitle)
  print("EP: ", ep)
  # Searches for the ID of the anime user is currently watching
  id, status, mal_ep = findAnimeID(title, jtitle)
  if id == None:
    print(title + " | " + jtitle + " : CANNOT BE FOUND IN USERS MAL LIST" )
  elif status == 'watching' and ep > mal_ep:
    update = {
      'num_watched_episodes': ep
    }
    url = 'https://api.myanimelist.net/v2/anime/' + str(id) + '/my_list_status'
    r = requests.put(url, headers=key, data=update)
    print("FINISHED UPDATING MAL")
  else:
    print("USER IS REWATCHING PREV EP")


# Searches the users current anime list on MAL and returns the specific anime id value,
# Returns None if anime entry does not exist on MAL
def findAnimeID(title, jtitle):
  r = requests.get('https://api.myanimelist.net/v2/users/@me/animelist?fields=list_status&limit=1000', headers=key).json()
  r = r['data']
  # Loops through user's MAL list in search for anime user is currently watching
  # for anime in r:
  #   name = anime['node']['title']
  #   if name.lower() == title.lower() or name.lower() == jtitle.lower():
  #     return anime['node']['id'], anime['list_status']['status'], anime['list_status']['num_episodes_watched']
  if checkTitle(title, r) != None:
    return checkTitle(title, r)
  elif checkTitle(jtitle, r) != None:
    return checkTitle(title, r)
  else:
    return (None, None, None)


# Calculates a score that compares the given chrome anime title to the one on the website,
# Which allows for flexibility rather than precise one-for-one name
def checkTitle(title, r):
  currWatching = getWatching(r)

  filteredTitle = title.lower()
  invalidPunctuations = "!.~"
  for punctuation in invalidPunctuations:
    filteredTitle = filteredTitle.replace(punctuation, " ")
  
  titleWords = filteredTitle.split()
  for anime in currWatching:
    name = anime['node']['title'].lower()
    matchedWords = 0
    for word in titleWords:
      if word in name:
        matchedWords += 1
    score = matchedWords / len(titleWords)
    if score >= 0.5:
      return anime['node']['id'], anime['list_status']['status'], anime['list_status']['num_episodes_watched']
  return None


# Helper method to get only current watching animes on one's list
def getWatching(r):
  watching = []
  for anime in r:
    if anime['list_status']['status'] == 'watching':
      watching.append(anime)
  return watching



if __name__ == '__main__':
  app.run()