import urllib2

region_dict = {
    'br': 'BR1',
    'eune': 'EUN1',
    'euw': 'EUW1',
    'kr': 'KR',
    'lan': 'LA1',
    'las': 'LA2',
    'na': 'NA1',
    'oce': 'OC1',
    'ru': 'RU',
    'tr': 'TR1'}

class RiotAPI():
    
    def __init__(self, api_key, region='na'):
        self.region = region
        self.api_key = api_key
        self.api_key_amp = '&api_key=' + self.api_key
        self.api_key_question = '?api_key=' + self.api_key
        self.base_url = "https://" + region + ".api.pvp.net"

    def set_region(self, region):
        self.region = region

    #championmastery (no version listed)
    def get_championmastery_playerid_championid(self, player_id, champion_id):
        url = self.base_url + '/championmastery/location/' + region_dict[self.region] + "/player/" + \
            str(player_id) + "/champion/" + str(champion_id) + self.api_key_question
        f =  urllib2.urlopen(url)
        return f.read()

    def get_championmastery_playerid_allchampions(self, player_id):
        url = self.base_url + '/championmastery/location/' + region_dict[self.region] + "/player/" + \
            str(player_id) + "/champions" + self.api_key_question
        f =  urllib2.urlopen(url)
        return f.read()

    def get_championmastery_playerid_totalmasterylevel(self, player_id):
        url = self.base_url + '/championmastery/location/' + region_dict[self.region] + "/player/" + \
            str(player_id) + "/score" + self.api_key_question
        f =  urllib2.urlopen(url)
        return f.read()

    def get_championmastery_playerid_topcount(self, player_id, count):
        url = self.base_url + '/championmastery/location/' + region_dict[self.region] + "/player/" + \
            str(player_id) + "/topchampions?count=" + str(count) + self.api_key_amp
        f =  urllib2.urlopen(url)
        return f.read()

    #summoner-v1.4
    def get_playerid_from_playername(self, player_names):
        url = self.base_url + "/api/lol/" + self.region + "/v1.4/summoner/by-name/" + \
            player_names + self.api_key_question
        f =  urllib2.urlopen(url)
        return f.read()


