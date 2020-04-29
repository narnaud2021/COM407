def convert(some_list):
	mylist = some_list
	mystring = ''.join(str(i) for i in mylist)
	return int(str(mystring),2)


chrom = [1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,5,
         1,1,1,2,2,2,2,2,3,3,3,3,3,4,4,4,4,4,5,5,5,6,6,6,6,7,7,7,7,7,8,8,8,8,9,9,9,9,9,10,10,10,10,11,11,11,11,12,12,12,
         1,1,1,1,1,2,2,2,2,2,3,3,3,3,3,4,4,4,4,4,5,5,5,5,5,6,6,6,6,6,7,7,7,7,7,8,8,8,8,8,9,9,9,10,10,10,10,10,11,11,11,11,11,12,12,12,13,13,13,13,13,14,14,14,14,14,15,15,15,15,15,16,16,16,16,16,17,17,17,17,17,18,18,18,18,18]

chrom = [0,1,0,1, 0,1,0,1,
         0,1,1, 1,0,1,0,0, 1,1,1,0,0, 1,1,1,0,0, 0,1,1, 0,1,1,1, 1,1,1,0,0,  1,1,1,0,0, 0,1,0,1, 1,0,1,0,0, 0,1,0,1, 1,1,0,0, 1,0,1,
         1,0,1,0,0, 1,0,1,0,0, 1,1,0,0,1, 1,0,1,0,0, 1,1,0,0,1, 1,0,1,0,0, 1,0,1,0,0, 1,0,1,0,0, 0,1,0, 1,0,1,0,0, 1,0,1,0,0, 0,1,0, 1,0,1,0,0, 1,0,1,0,0, 1,1,0,0,1, 1,1,0,0,1, 1,1,0,0,1, 1,1,0,0,1]

enemyrule1 = convert(chrom[0:4])*20+100
enemyrule2 = convert(chrom[4:8])*20+100

print(enemyrule1)
print(enemyrule2)
print('')
print(len(chrom))
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

print(thrustrule1)
print(thrustrule2)
print(thrustrule3)
print(thrustrule4)
print(thrustrule5)
print(thrustrule6)
print(thrustrule7)
print(thrustrule8)
print(thrustrule9)
print(thrustrule10)
print(thrustrule11)
print(thrustrule12)
print(thrustrule13)

print('')

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

print(turnrule1)
print(turnrule2)
print(turnrule3)
print(turnrule4)
print(turnrule5)
print(turnrule6)
print(turnrule7)
print(turnrule8)
print(turnrule9)
print(turnrule10)
print(turnrule11)
print(turnrule12)
print(turnrule13)
print(turnrule14)
print(turnrule15)
print(turnrule16)
print(turnrule17)
print(turnrule18)





















