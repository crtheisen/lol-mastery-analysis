import yaml
from riot_api import RiotAPI

f = open("./api_key", "r")
api = RiotAPI(f.read())
f.close()

print "Testing specific player, specific id:\n" + \
    api.get_championmastery_playerid_championid(32209760, 36).replace(",", ",\n") + "\n"
print "Testing specific player, all champs:\n" + \
    api.get_championmastery_playerid_allchampions(32209760).replace(",", ",\n") + "\n"
print "Testing specific player, sum of individual champion mastery levels:\n" + \
    api.get_championmastery_playerid_totalmasterylevel(32209760).replace(",", ",\n") + "\n"
print "Testing specific player, top X champs:\n" + \
    api.get_championmastery_playerid_topcount(32209760, 2).replace(",", ",\n") + "\n"


