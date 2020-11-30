import json
from libbgg.apiv1 import BGG

conn = BGG()

# Perform a search
results = conn.search('bruges')
print(json.dumps(results, indent=4, sort_keys=True))

# Print out a list of names that were returned
for game in results.boardgames.boardgame:
    print(game.name.TEXT)

# You can also access items as a dictionary
for game in results['boardgames']['boardgame']:
    print(game['name']['TEXT'])

# # Get game info
# results = conn.get_game(136888 , stats=True)
# print(json.dumps(results, indent=4, sort_keys=True))