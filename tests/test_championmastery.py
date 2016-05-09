class TestRiotChampionMastery():
  def __init__(self, api):
    self.api = api

  def test_get_championmastery_playerid_championid(self):
    result = self.api.get_championmastery_playerid_championid(32209760, 36)
    print(result)

  def test_get_championmastery_playerid_allchampions(self):
    result = self.api.get_championmastery_playerid_allchampions(32209760)
    print(result)

  def test_get_championmastery_playerid_totalmasterylevel(self):
    result = self.api.get_championmastery_playerid_totalmasterylevel(32209760)
    print(result)
  
  def test_get_championmastery_playerid_topcount(self):
    result = self.api.get_championmastery_playerid_topcount(32209760, 2)
    print(result)


