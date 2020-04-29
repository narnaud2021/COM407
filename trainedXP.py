#Alex and Nelia
#April 2020
#Program Xpilot-GA
#trained agent for XPilot

import random
import libpyAI as ai

def convert(some_list):
	mylist = some_list
	mystring = ''.join(str(i) for i in mylist)
	return int(str(mystring),2)

def AI_loop():
  #This is the best chromosome from the history of the best individuals from the history
  chrom = [0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1]
  #Enemy rules
  enemyrule1 = convert(chrom[0:4])*20+100
  enemyrule2 = convert(chrom[4:8])*20+100

  #These are Thrusting Rules
  thrustrule1 = convert(chrom[8:11])*3
  thrustrule2 = convert(chrom[11:16])*10+100
  thrustrule3 = convert(chrom[16:21])*10+170
  thrustrule4 = convert(chrom[21:26])*10+170
  thrustrule5 = convert(chrom[26:29])*3
  thrustrule6 = convert(chrom[29:33])*20+150
  thrustrule7 = convert(chrom[33:38])*10+170
  thrustrule8 = convert((chrom[38:43]))*10+170
  thrustrule9 = convert(chrom[43:47])*20+100
  thrustrule10 = convert(chrom[47:52])*10+100
  thrustrule11 = convert(chrom[52:56])*20+100
  thrustrule12 = convert(chrom[56:60])*20+100
  thrustrule13 = convert(chrom[60:63])*9

  #Turn Rules
  turnrule1 = convert(chrom[63:68])*10+100
  turnrule2 = convert(chrom[68:73])*10+100
  turnrule3 = convert(chrom[73:78])*10+150
  turnrule4 = convert(chrom[78:83])*10+100
  turnrule5 = convert(chrom[83:88])*10+150
  turnrule6 = convert(chrom[88:93])*10+150
  turnrule7 = convert(chrom[93:98])*10+100
  turnrule8 = convert(chrom[98:103])*10+100
  turnrule9 = convert(chrom[103:106])*20+50
  turnrule10 = convert(chrom[106:111])*10+100
  turnrule11 = convert(chrom[111:116])*10+100
  turnrule12 = convert(chrom[116:119])*20+50
  turnrule13 = convert(chrom[119:124])*10+100
  turnrule14 = convert(chrom[124:129])*10+100
  turnrule15 = convert(chrom[129:134])*10+150
  turnrule16 = convert(chrom[134:139])*10+150
  turnrule17 = convert(chrom[139:144])*10+150
  turnrule18 = convert(chrom[144:149])*10+150

  #Release keys
  ai.thrust(0)
  ai.turnLeft(0)
  ai.turnRight(0)

  #Set variables
  heading = int(ai.selfHeadingDeg())
  tracking = int(ai.selfTrackingDeg())
  trackWall = ai.wallFeeler(500,tracking)

  #creates id for closest enemy ship
  closestShip = ai.closestShipId()
  #tracks enemy dist with enemy id
  eDist = int(ai.enemyDistanceId(closestShip))
  eTrack = int(ai.enemyTrackingDeg(closestShip))
  #eHead = int(ai.enemyHeadingDeg(closestShip)) 
	
  ePosX = ai.screenEnemyXId(closestShip)

  #enemyclose = False
  distwalls = []
  for i in range(8):
    distwalls.append(ai.wallFeeler(500,heading+(45*i)))
  index = 0
  shortest = 501
  for j in range(8):
    if distwalls[j] < shortest:
      shortest = distwalls[j]
      index = j
  ai.setTurnSpeedDeg(20)
 
  #Set variable to lock onto enemy ship  
  eLock = int(ai.lockHeadingDeg())
  sAlert = ai.shotDist(0)
  print("eLock ", eLock)
  print("Dist ", eDist)
  #print("eTrack ", eTrack)
  print("TW ",trackWall)
  print("ePosX", ePosX)
  print("S alert", sAlert)
  print("----------")
  
  if ai.selfSpeed() <= thrustrule1 and distwalls[0] >= thrustrule2 and distwalls[1] > thrustrule3 and distwalls[2] >thrustrule4:      
    ai.thrust(1)
  elif ai.selfSpeed() <= thrustrule5 and distwalls[0] >= thrustrule6 and distwalls[7] > thrustrule7 and distwalls[6] > thrustrule8:
    ai.thrust(1)
  elif trackWall < thrustrule9 and distwalls[0] > thrustrule10:
    ai.thrust(1)
  elif trackWall < thrustrule11 and distwalls[1] > thrustrule12:
    ai.thrust(1)
  elif distwalls[4] < thrustrule13:
    ai.thrust(1)
 
  if eDist < trackWall and eDist < enemyrule1:
    ai.turnToDeg(ai.aimdir(0))
    ai.fireShot()
  elif eDist < trackWall and eDist > enemyrule2:
    ai.turnToDeg(ai.aimdir(0))
    ai.fireShot()

  #Turn Rules
  if trackWall < turnrule1 and distwalls[6] < turnrule2:
    ai.turnLeft(1)
  elif trackWall < turnrule3 and distwalls[3] < turnrule4:
    ai.turnRight(1)
  elif trackWall < turnrule5 and distwalls[7] < turnrule6:
    ai.turnLeft(1)
  elif trackWall < turnrule7 and distwalls[2] < turnrule8:
    ai.turnRight(1)
  elif trackWall < turnrule9 and distwalls[3] < turnrule10 and distwalls[7] > turnrule11:
    ai.turnRight(1)
  elif trackWall < turnrule12 and distwalls[5] < turnrule13 and distwalls[1] > turnrule14:
    ai.turnRight(1)
  elif trackWall < turnrule15 and distwalls[5] < turnrule16:
    ai.turnLeft(1)
  elif trackWall < turnrule17 and distwalls[3] < turnrule18:
    ai.turnRight(1)
  elif index <= 4:
    ai.turnRight(1)
  elif index > 4:
    ai.turnLeft(1)  

ai.start(AI_loop,["-name","A&N"])
