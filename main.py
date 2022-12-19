

import numpy as np
import csv
myList = []
nr_juc= 0
poz_total = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
with open(r'C:\Users\robot\Desktop\Teams\Atacanti_Chelsea.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        if len(row) == 13:
            myList.append([int(row[0]), int(row[1]), int(row[2]), int(row[3]),int(row[4]),int(row[5]),int(row[6]),int(row[7]),int(row[8]),int(row[9]),int(row[10]),int(row[11]),int(row[12])])
            poz_total[int(row[1])]+=1


for i in range(len(poz_total)):
    nr_juc+=poz_total[i]
juc_total=[0]*nr_juc
print(juc_total)

juc_total[0]=1
juc_total[poz_total[13]]=1
juc_total[poz_total[13]+poz_total[14]-1]=1

juc_total2=[0]*nr_juc
juc_total2[1]=1
juc_total2[poz_total[13]+1]=1
juc_total2[poz_total[13]+poz_total[14]]=1

print(juc_total)
print(juc_total2)






def breed(crom):
    for i in range(0,len(crom)-1,2):
        nrbit=np.random.randint(len(crom))
        nrbit=len(crom)-nrbit
        print("nr biti schimbati=",nrbit)
       #crom[i][nrbit:],crom[i+1][nrbit:]=crom[i+1][nrbit:],crom[i][nrbit:].copy()
        temp=np.copy(crom[i][nrbit:])
        crom[i][nrbit:]=crom[i+1][nrbit:]
        crom[i+1][nrbit:]=temp


#breed(np.array(juc_total_fin[0:poz_total[12]]))
#breed(juc_total[poz_total[12]:poz_total[12]+poz_total[13]])
#breed(juc_total[poz_total[12]+poz_total[13]:])



npArray = np.array(myList)
print(npArray)

def calc_player_score(player_info):
    mp=player_info[2]
    assists=player_info[3]
    passes=player_info[4]
    pass_accuracy=player_info[5]
    crosses=player_info[6]
    cross_accuraacy=player_info[7]
    goals=player_info[8]
    dribbles=player_info[9]
    shots=player_info[10]
    shot_accuracy=player_info[11]
    status=player_info[12]
    score=(passes*(pass_accuracy/100)+assists*2+crosses*(cross_accuraacy/100)+goals*3+dribbles+shots*(shot_accuracy/100))*mp*status
    return score

def get_position(player_info):
    return player_info[1]

def get_id(player_info):
    return player_info[0]

scores = []
positions=[]
ids=[]
for row in range(npArray.shape[0]):
    score=calc_player_score(npArray[row])
    position=get_position(npArray[row])
    id=get_id(npArray[row])
    scores.append(score)
    positions.append(position)
    ids.append(id)
scores=np.array(scores)
positions=np.array(positions)
ids=np.array(ids)

mylist_calculated=np.stack((ids,positions,scores),axis=1);



myList_nume=[]
with open(r'C:\Users\robot\Desktop\Teams\Atacanti_Chelsea_Nume.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        if len(row) == 5:
             myList_nume.append([int(row[0]),(row[1]),(row[2]),(row[3]),(row[4])])
myList_nume=np.array(myList_nume)
print(myList_nume)


def get_best_jucator(pozitie):
    pozitie_cautata = []
    for row in range(mylist_calculated.shape[0]):
        if(pozitie==mylist_calculated[row][1]):
            pozitie_cautata.append(mylist_calculated[row])

    scor_max=max(np.amax(pozitie_cautata,axis=1))

    for row in range(mylist_calculated.shape[0]):
        if(mylist_calculated[row][2]==scor_max):
            best_id=mylist_calculated[row][0]
    best_name=""
    for row in range(myList_nume.shape[0]):
        if(int(myList_nume[row][0])==best_id):
            best_name=myList_nume[row][3]
    print(best_name)
    print (scor_max)

def get_best_lineup(a,b):
     for i in range(a,b):
        get_best_jucator(i)

print("Statistic, cei mai buni 3 atacanti de la Chelsea sunt: ")
get_best_lineup(12,15)







