#Alex and Nelia
#Feb 1 2020
#Program 1
import libpyAI as ai
from random import *
import Genetic_Algorithm as GA

def convert(some_list):
	mylist = some_list
	mystring = ''.join(str(i) for i in mylist)
	return int(str(mystring),2)
global score
global last
global frames
global fframe
def AI_loop():
  global score
  global frames
  global fframe
  global generation
  global temp_chrom
  global temp_score
  global population
  global individual_index
  global scores_of_gen
  global best_ind
  global mutation_rate
  global average_scoreA
  
  if fframe:
    fframe = False 
  #chrom = [0,1,0,1, 0,1,0,1, 0,1,0,1, 0,1,0,1, 1,1,1,1,1, 0,1,1, 1,0,1,0,0, 1,1,1,0,0, 1,1,1,0,0, 0,1,1, 0,1,1,1, 1,1,1,0,0,  1,1,1,0,0, 0,1,0,1, 1,0,1,0,0, 0,1,0,1, 1,1,0,0, 1,0,1, 1,0,1,0,0, 1,0,1,0,0, 1,1,0,0,1, 1,0,1,0,0, 1,1,0,0,1, 1,0,1,0,0, 1,0,1,0,0, 1,0,1,0,0, 0,1,0, 1,0,1,0,0, 1,0,1,0,0, 0,1,0, 1,0,1,0,0, 1,0,1,0,0, 1,1,0,0,1, 1,1,0,0,1, 1,1,0,0,1, 1,1,0,0,1]
  print('current gen', generation)
  print('current index', individual_index)
  temp_chrom = population[individual_index][0]
  chrom = temp_chrom
  print("current_chrom is", chrom)
  enemyrule1 = convert(chrom[0:4])*20+100
  enemyrule2 = convert(chrom[4:8])*20+100

  #chrom = population[current_chrom][0]
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

  #Thrust rules
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

 #Shooting Rules
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
  
  print("frames", frames)

#Logic to apply GA Operators
  if ai.selfAlive() == 1:
    frames = frames + 1
  elif ai.selfAlive() == 0 and frames == 0:
    pass
  else:
    print('got hereeee')
    score.append(ai.selfScore())
    if len(score) < 2:
      temp_score = score[-1]
    else:
      temp_score = score[-1] - score[-2]
    if temp_score <= 0:
      temp_score = 2
    print('temp_score', temp_score) 
    temp_score = (frames**2) * temp_score 
    population[individual_index][1] = temp_score
    scores_of_gen.append(temp_score)
    print('all scores', scores_of_gen)
    print('new population', population)

    #Write Txt File for Best Ind and their Fitness across pop each gen
    individual_index += 1
    #fscore = GA.calc_fitness(temp_chrom,population)
    if individual_index==pop_size:
      temp_fit = max(scores_of_gen)
      best_score_index = scores_of_gen.index(temp_fit)
      best_score = population[best_score_index][0]
      best_file = open("Best_ind.txt","a+")
      best_file.write("Generation: ")
      best_file.write(str(generation))
      best_file.write("\n")
      best_file.write("Best individual: ")
      best_file.write(str(best_score))
      best_file.write("\n")
      best_file.write("Best fitness: ")
      best_file.write("\n")
      best_file.write(str(temp_fit))
      best_file.write("\n")
      best_file.close()

    #Average Fitness
    if individual_index == pop_size:
      total_score = 0
      for i in range(len(scores_of_gen)):
        total_score = total_score + scores_of_gen[i]
      print('total score', total_score)
      average_score = total_score/pop_size
      print('average score', average_score)
      average_scoreA.append(average_score)
      print('array', average_scoreA)
      avg_file = open("Avg_score.txt","a+")
      avg_file.write(str(average_scoreA))
      avg_file.write("\n")

   #TExtfile for chrmosome of each individual
    if generation%10 == 0 and individual_index == pop_size:
      pg_file = open("Population_gen.txt","a+")
      pg_file.write("It workss")
      pg_file.write("Generation: ")
      pg_file.write("\n")
      pg_file.write(str(generation))
      pg_file.write("\n")
                
      for i in population:
        pg_file.write(str(i))
      pg_file.close()
    if individual_index >= len(population):
      print("temp_chrom", temp_chrom)
      print("index", individual_index)
      print('population', population)
      #Geenerate new pop
      new_population = []
      for i in range(pop_size):
        individual = []
        for j in range(chrom_size):
          individual.append(0)
        new_population.append([individual, -1])
      #print('hereee1')
      #print('scoreees', scores_of_gen)
        
      #For loop in order to obtain offspring for the next population
      for i in range(0, pop_size):
        #Obtaining two parents through selection
        parent_1 = GA.roulette_wheel_selection(population, scores_of_gen)
        parent_2 = GA.roulette_wheel_selection(population, scores_of_gen)
        par1_index = population.index(parent_1)
        par2_index = population.index(parent_2)
        #If the parents are the same, it looks for another partner
        print('hereee2')
        while par1_index == par2_index:
            parent_2 = GA.roulette_wheel_selection(population, scores_of_gen)
            par2_index = population.index(parent_2)
        
        #Breeding both parents in order to obtain an individual
        child = GA.breed_by_crossover(parent_1[0], parent_2[0])
        #Inserting the child into the matrix of zeros
        new_population[i][0] = child
      print('hereee4')
      #Mutating the populatiob
      new_population = GA.mutation(new_population, mutation_rate)
      print('hereeee5')

      #Setting the new population to the current population and increasing the generation
      population = new_population
      scores_of_gen = []
      generation = generation + 1
      individual_index = 0
    frames = 0
    
frames = 0
score = []
generation = 0
individual_index = 0
fframe = True
last = False
temp_chrom = []
temp_score = 0
pop_size = 128
chrom_size = 149
population = []
fscore = []
scores_of_gen = []
best_ind = []
mutation_rate = 0.01
average_scoreA = []
#initialize random pop
population = GA.init_population(pop_size, chrom_size)

ai.start(AI_loop,["-name","A&N2"])
    

