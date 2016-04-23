class TestRiotSummoner14():
  def __init__(self, api):
    self.api = api

  def test_get_playerid_from_playername(self):
    print "Testing specific player, specific id:\n" + \
      self.api.get_playerid_from_playername("Ellipson,T3lrec").replace(",", ",\n") + "\n"