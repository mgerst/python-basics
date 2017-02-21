#!/usr/bin/env python
import requests

# This URL gives us all the teams and their scores
SCOREBOARD_URL = "https://iscore-last.iseage.org/api/v1/teams/scoreboard.json"

resp = requests.get(SCOREBOARD_URL)

# The data is returned as JSON
data = resp.json()

# The with statement ensures that the file gets closed
# after we use it, even if an error occurs.
with open('cdc.csv', 'w') as fp:
    for team in data['scoreboard']:
        # Total is a float, and needs to be converted into a string
        name = team['team']['name']
        total_score = team['total']
        place = team['place']

        fp.write("{place},{name},{score}\n".format(place=place, 
                                                   name=name, 
                                                   score=total_score))

print("Done! Got the score data")
