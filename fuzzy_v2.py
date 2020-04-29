def close(distance):
  if distance < 150:
    mVal = 1
    return mVal
  elif distance >=150 and distance <= 190:
    mVal = -(1/40) * distance + (19/4)
    return mVal
  else:
    mVal = 0
    return mVal

def medium(distance):
  if distance < 160:
    mVal = 0
    return mVal
  elif distance >= 160 and distance<=220:
    mVal =(1/60) * distance - (8/3)
    return mVal
  elif distance > 220 and distance < 400:
    mVal = -(1/180) * distance + (20/9)
    return mVal
  else:
    mVal = 0
    return mVal

def far(distance):
  if distance < 370:
    mVal = 0
    return mVal
  elif distance >= 370 and distance <= 420:
    mVal = (1/50)* distance - (37/5)
    return mVal
  else:
    mVal = 1
    return 1

def distWall(distance):
  #distance = 400
  wClose = close(distance)
  wMed = medium(distance)
  wFar = far(distance)
  print(wFar)
  return(wClose, wMed, wFar)

def distTrackWall(distance):
  #distance = 400
  tClose = close(distance)
  tMed = medium(distance)
  tFar = far(distance)
  return(tClose, tMed, tFar)

def distEnemy(distance):
  #distance = 400
  eClose = close(distance)
  eMed = medium(distance)
  eFar = far(distance)
  return(eClose, eMed, eFar)

def crashRisk(d1,d2,d3):
  cVLow = 0
  cVHigh = 0
  cLow = 0
  cMed = 0
  cHigh = 0
  tClose,tMed,tFar = distTrackWall(d1)
  eClose,eMed,eFar = distEnemy(d2)
  wClose,wMed,wFar = distWall(d3)
  if tFar > 0:
    cLow = tFar
  if tMed > 0:
    cMed = tMed  
  if tClose > 0:
    cHigh = tClose

  if wFar > 0 and eFar > 0 :
    cVLow = min(wFar, eFar)
  if wMed > 0 and eFar > 0:
    cMed = min(wMed, eFar)
  if tClose > 0 and eFar > 0:
    cHigh = min(tClose, eFar)

  if wFar > 0 and eMed > 0:
    cLow = min(wFar, eMed)
  if wMed > 0 and eMed > 0:
    cMed = min(wMed, eMed)  
  if tClose > 0 and eMed > 0:
    cHigh = min(tClose, eMed)

  if wFar > 0 and eClose > 0:
    cMed = min(wFar, eClose)
  if wMed > 0 and eClose > 0:
    cMed = min(wMed, eClose)  
  if tClose > 0 and eClose > 0:
    cVHigh = min(tClose, eClose)

  print(cVHigh)
  defuzz = ((cVLow * d2) + (cLow * d2) + (cMed * d2)+ (cHigh * d1)+ (cVHigh * d1)) / (cVLow + cLow + cMed +cHigh +cVHigh)
  return defuzz
