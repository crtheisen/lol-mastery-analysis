class TestRiotChampionMastery():
  def __init__(self, api):
    self.api = api

  def test_get_championmastery_playerid_championid(self):
    print "Testing specific player, specific id:\n" + \
      self.api.get_championmastery_playerid_championid(32209760, 36).replace(",", ",\n") + "\n"

  def test_get_championmastery_playerid_allchampions(self):
    print "Testing specific player, all champs:\n" + \
      self.api.get_championmastery_playerid_allchampions(32209760).replace(",", ",\n") + "\n"

  def test_get_championmastery_playerid_totalmasterylevel(self):  
    print "Testing specific player, sum of individual champion mastery levels:\n" + \
      self.api.get_championmastery_playerid_totalmasterylevel(32209760).replace(",", ",\n") + "\n"

  def test_get_championmastery_playerid_topcount(self):
    print "Testing specific player, top X champs:\n" + \
      self.api.get_championmastery_playerid_topcount(32209760, 2).replace(",", ",\n") + "\n"


