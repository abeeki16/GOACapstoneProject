
class Robot:
  def __init__(self):
    self.canCooperition=False
    self.objectInfo={"Totes":{"lift":"","push":"","Stack Height":0,"flip":""},"Bins":{"lift":"","push":"","Stack Height":0,"flip":""}}
    self.objectInfo["Litter"]={"lift":"","push":""}
    self.driveSystem=""
    
  
  def updateObjectInfo(self,item):
      inputDict={"YES":"X","NO":"","1":"X","2":""}
    
      for action in self.objectInfo[item]:
        
        if (action=="Stack Height"):
          while True:
            userInput=input("How many "+item+" can this robot stack: ")
            try:
              userInput=int(userInput)
              if (userInput==-1):
                break
              elif(userInput<=0):
                print("Invalid input")
              else:
                self.objectInfo[item]["Stack Height"]=userInput
                break
            except ValueError:
              print("Invalid input")
              
        else:
          
          while (True):
            userInput=input("Can this robot "+action+" "+item+" \n1.Yes\n2.No\nEnter choice here: ")
          
            userInput=userInput.upper()
            try:
              self.objectInfo[item][action]=inputDict[userInput]
              break
            except KeyError:
              if (userInput=="-1"):
                break
              else:
                print("Invalid input")
          
      
  def displayRobotInfo(self):
    print("\n\n\n\nObject\t\tPush\t\tLift\t\tFlip\t\tStack Height\t\t")
    print("\n\nTotes\t\t"+self.objectInfo["Totes"]["push"]+"\t\t"+self.objectInfo["Totes"]["lift"]+"\t\t"+self.objectInfo["Totes"]["flip"]+"\t\t"+str(self.objectInfo["Totes"]["Stack Height"]))
    print("\n\nBins\t\t"+self.objectInfo["Bins"]["push"]+"\t\t"+self.objectInfo["Bins"]["lift"]+"\t\t"+self.objectInfo["Bins"]["flip"]+"\t\t"+str(self.objectInfo["Bins"]["Stack Height"]))    
    print("\n\nLitter\t\t"+self.objectInfo["Litter"]["push"]+"\t\t"+self.objectInfo["Litter"]["lift"]+"\t\t\n\n\n\n\n\n\n")
      


