import json
from pprint import pprint

class TestRiotSummoner14():
  def __init__(self, api):
    self.api = api

  def test_get_playerid_from_playername(self):
    result = self.api.get_playerid_from_playername("Ellipson,T3lrec")
    print(result)