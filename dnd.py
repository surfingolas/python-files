import urllib.request, urllib.parse, urllib.error
import json

player_atts = []
player_dict = dict()
player_dict_lst = [{'core' : 0}]
serviceurl = 'http://www.dnd5eapi.co/api/'

extend = 'Ability-Scores'

url = serviceurl + extend

uh = urllib.request.urlopen(url)
data = uh.read().decode()
js = json.loads(data)


for stuff in js['results']:#finds the core skills
    atts_url = stuff["url"]
    atts_sock = urllib.request.urlopen(atts_url)
    atts_data = atts_sock.read().decode()
    atts_js = json.loads(atts_data)
    player_atts.append(atts_js['full_name'])
    player_dict[atts_js['name']] = player_dict_lst
    for stuff in atts_js['skills']:#finds the skills within the core skills
        player_atts.append(stuff["name"])
        skill_url = stuff['url']
        skill_sock = urllib.request.urlopen(skill_url)
        skill_data = skill_sock.read().decode()
        skill_js = json.loads(skill_data)
        print(json.dumps(skill_js, indent=4))
        




for stuff in player_atts:
    print(stuff)

print(player_dict)
print(player_dict_lst)
