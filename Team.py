import urllib.request
import json
from Robot import Robot
def getApiDict(url):
  
  lines = urllib.request.urlopen(url).readlines()
  list_of_strings = []
  for line in lines:
    list_of_strings.append(line.decode('utf-8').strip('\n'))
  merged_string = ''
  for string in list_of_strings:
    if string not in ('// [', ']'):
      merged_string += string
  return json.loads(merged_string)

class Team:
    
  def __init__(self,url):
      
    
      
    self.teamDict=getApiDict(url)
    self.scoutingInfo={"Teleop":Robot(),"Autonomous":Robot()}
    
   
    
   #cleans up the dictionary keys for printing and User input
    self.teamDict["School/sponsors"] = self.teamDict.pop("name")
    self.teamDict["Locality"] = self.teamDict.pop("locality")
    self.teamDict["Rookie year"]=self.teamDict.pop("rookie_year")
    self.teamDict["Team number"]=self.teamDict.pop("team_number")
    self.teamDict["Location"]=self.teamDict.pop("location")
    self.teamDict["Official team name"]=self.teamDict.pop("key")
    self.teamDict["Country name"]=self.teamDict.pop("country_name")
    self.teamDict["Website"]=self.teamDict.pop("website")
    self.teamDict["Region"]=self.teamDict.pop("region")
    self.teamDict["Nickname"]=self.teamDict.pop("nickname")  
  
                
              
