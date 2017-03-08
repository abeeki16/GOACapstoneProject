#Ajit Capstone
from Team import Team
import urllib.request
import json
import requests
import pickle
import os

def getTeamInfo(Team):
  
  
  print("What information would you like to print")
  x=0
  inputList=[]
  for info in Team.teamDict:
    x+=1
    print(str(x)+".",info)
    inputList.append(info)
    
  Quit=False
  while (not Quit):
    isInputValid=False
    while (not isInputValid):
      userInput=input("Enter selection here(or -1 to quit): ")
  
      try:
        userInput=int(userInput)
        if(userInput==-1):
          Quit=True
        elif(userInput>0 and userInput<=len(inputList)):
          print(Team.teamDict[inputList[userInput-1]])
        
        else:
          print("Invalid input")
        isInputValid=True
      except ValueError:
        userInput=userInput.lower()
        userInput=userInput.capitalize()
        try:
          print(Team.teamDict[userInput])
          isInputValid=True
        except KeyError:
          print("Invalid Input, Please try again. ")
          isInputValid=False
  
  
  
def scout(Team):
  
  while True:

      
      
      print("Which game mode?\n1.Autonomous\n2.Teleop")
      inputIsValid=False
      while (not inputIsValid):
        userInput=input("Enter choice here: ")
        
        if(userInput.upper()=="AUTONOMOUS" or userInput.upper()=="TELEOP"):
          mode=userInput.lower().capitalize()
          inputIsValid=True
        elif(userInput=="1"):
          mode="Autonomous"
          inputIsValid=True
        elif(userInput=="2"):
          mode="Teleop"
          inputIsValid=True
        elif(userInput=="-1"):
          mode="-1"
          inputIsValid=True
          
      
      inputDict={"1":"Bins","2":"Totes","3":"Litter","BINS":"Bins","TOTES":"Totes","LITTER":"Litter"}
      if(mode=="-1"):
         break
      else:
          
        print("Display or update robot information\n1.Update\n2.Display")

        while True:
          dispOrUpdate=input("Enter selection here: ")
          
          if(dispOrUpdate.lower()=="display" or dispOrUpdate=="2"):
            print("\n\n\n\n\n\n\n\n")
            print(mode,"SUMMARY","for",Team.teamDict["Official team name"],"\n\n\n")
        
            Team.scoutingInfo[mode].displayRobotInfo()
            break

          elif(dispOrUpdate=="1" or dispOrUpdate.lower()=="update"):

            print("Which information would you like to update: ")

            Quit=False

            while (not Quit):

              print("1.Bins","\n2.Totes","\n3.Litter")
            
              while True:
                userInput=input("")
                userInput=userInput.upper()

                try:
                  Team.scoutingInfo[mode].updateObjectInfo(inputDict[userInput])
                  break
                except KeyError:
                  if(userInput=="-1"):
                    Quit=True
                  break
                else:
                  print("Invalid Input")
          
            break

          elif(dispOrUpdate=="-1"):
            break
          else:
            print("Invalid input")
        
          
        
try:
  inputFile= open("data.pkl","rb")
  userInput=input("Would you like to load previous settings or start new?\n1.Load Previous save\n2.New\n")
  if(userInput.lower()=="load" or userInput=="1"):
    teams=pickle.load(inputFile)
  else:
    os.remove("data.pkl")
    teams={}
except FileNotFoundError:
  teams={}

print("Welcome to the FRC Scouting/Team Info Program!")
print("NOTE: Enter -1 at anytime to exit loop/end program\n\n\n\n\n\n")
Quit=False
while (not Quit):
  
  while True:
    
    teamSelection=input("What team would you like to see info/scout about: ")
    if(teamSelection=="-1"):
      Quit=True
      break
    else:
      if teamSelection in teams:
        break
      else:
        url="http://www.thebluealliance.com/api/v2/team/frc"+teamSelection+"?X-TBA-App-Id=frc2353:legion:v02"
        if (requests.get(url).status_code==200):
          teams[teamSelection]=Team(url)
          break
        else:
          print("Invalid team")
  
  if(teamSelection!="-1"):
    
    print("Would you like to Scout or explore database: ")
    print("1.Scouting\n2.Team Info")
    while True:
      selection=input("Enter your choice: ")
      if(selection=="1" or selection.upper()=="SCOUTING"):
        scout(teams[teamSelection])
        print("1.Scouting\n2.Team Info")
      elif(selection=="2" or selection.upper()=="TEAM INFO"):
        getTeamInfo(teams[teamSelection])
        print("1.Scouting\n2.Team Info")
      
      elif(selection=="-1"):
        break
      
      else:
        print("Invalid input")

  

while True:
  userInput=input("Would you like to save your data?\n1.Yes\n2.No\n")
  if (userInput.lower()=="yes" or userInput=="1"):
    outputFile=open("data.pkl","wb")
    pickle.dump(teams,outputFile)
    outputFile.close()
    break
  elif(userInput.lower()=="no" or userInput=="2"):
    break
  else:
    print("Invalid input")
  

