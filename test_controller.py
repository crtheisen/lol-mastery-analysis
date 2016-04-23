import sys
sys.dont_write_bytecode = True

from riot_api import RiotAPI
from tests import test_championmastery as cm
from tests import test_summoner14 as smn

f = open("./api_key", "r")
api = RiotAPI(f.read())
f.close()

choice = 1

while(choice > 0 and choice < 3):
  choice = input("Enter which API to test: ")

  if(choice == 1): #championmastery
    tests = cm.TestRiotChampionMastery(api)

    tests.test_get_championmastery_playerid_championid()
    tests.test_get_championmastery_playerid_allchampions()
    tests.test_get_championmastery_playerid_totalmasterylevel()
    tests.test_get_championmastery_playerid_topcount()

  if(choice == 2): #summonerv1.4
    tests = smn.TestRiotSummoner14(api)

    tests.test_get_playerid_from_playername()

