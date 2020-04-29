#Alex and Nelia
#Feb 1 2020
#Program 1

import random
import libpyAI as ai
def AI_loop():
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
  
  #Enemy Rules
  #if enemy is too close turn and thrust to evade
  #if shot is dangerous turn and thrust to evade
  if eDist < 200 and eDist < trackWall and ePosX < ai.selfX() and ai.shotAlert(0) < 100:
    ai.turnLeft(1)
    ai.thrust(1)
  elif eDist < 200 and eDist < trackWall and ePosX > ai.selfX() and ai.shotAlert(0) < 100:
    ai.turnRight(1)
    ai.thrust(1)
  #enemy is close enough and 
  #dist to wall is prioritized over enemy
  if eDist < 450 and eDist < trackWall:
    ai.lockClose()        #returns deg of closest Ship
    ai.turnToDeg(eLock)
    ai.fireShot()

  #elif enemyclose == False:

  #Thrust rules
  if ai.selfSpeed() <= 10 and distwalls[0] >= 300 and distwalls[1] > 450 and distwalls[2] >450:      
    ai.thrust(1)
  elif ai.selfSpeed() <= 10 and distwalls[0] >= 300 and distwalls[7] > 450 and distwalls[6] > 450:
    ai.thrust(1)
  elif trackWall < 200 and distwalls[0] > 300:
    ai.thrust(1)
  elif trackWall < 200 and distwalls[1] > 350:
    ai.thrust(1)
  elif distwalls[4] < 50:
    ai.thrust(1)
 
  #Turn Rules
  if trackWall < 300 and distwalls[6] < 300:
    ai.turnLeft(1)
  elif trackWall < 400 and distwalls[3] < 300:
    ai.turnRight(1)
  elif trackWall < 400 and distwalls[7] < 350:
    ai.turnLeft(1)
  elif trackWall < 300 and distwalls[2] < 300:
    ai.turnRight(1)
  elif trackWall < 100 and distwalls[3] < 300 and distwalls[7] > 300:
    ai.turnRight(1)
  elif trackWall < 100 and distwalls[5] < 300 and distwalls[1] > 300:
    ai.turnRight(1)
  elif trackWall < 400 and distwalls[5] < 400:
    ai.turnLeft(1)
  elif trackWall < 400 and distwalls[3] < 400:
    ai.turnRight(1)
  elif index <= 4:
    ai.turnRight(1)
  elif index > 4:
    ai.turnLeft(1)  

  #Just keep shooting
  ai.fireShot()
ai.start(AI_loop,["-name","A&N2",])