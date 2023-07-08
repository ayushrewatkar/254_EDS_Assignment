import csv
from datetime import datetime

from datetime import date
print("Today's Date:",date.today())
def cal_age(d):
    td=date.today()#today date
    age=td.year-d.year-((td.month,td.day)<(d.month,d.day))
    return age

f1=open("player.csv","r")
f2=open("odi.csv","r")
f3=open("t20.csv","r")

data1= list(csv.reader(f1))
data2= list(csv.reader(f2))
data3= list(csv.reader(f3))

sr=[]; nm=[]; bd=[]; typ=[]; city=[]
odm=[]; odr=[]; odw=[]; odc=[]; odhc=[]
tm=[]; tr=[]; tw=[]; tc=[]; thc=[]

for i in range(len(data1)):
    sr.append(int(data1[i][0]))
    nm.append(data1[i][1])
    d=datetime.strptime(data1[i][2],"%d-%m-%Y")#in this line BOD is Converted into age
    bd.append(str(cal_age(d)))
    typ.append(data1[i][3])
    city.append(data1[i][4])

    odm.append(int(data2[i][0]))
    odr.append(float(data2[i][1]))
    odw.append(int(data2[i][2]))
    odc.append(int(data2[i][3]))
    odhc.append(int(data2[i][4]))

    tm.append(int(data3[i][0]))
    tr.append(float(data3[i][1]))
    tw.append(int(data3[i][2]))
    tc.append(int(data3[i][3]))
    thc.append(int(data3[i][4]))

print("Serial No.:",sr,"\n")
print("Player name:",nm,"\n")
print("Age of player:",bd,"\n")
print("Type of Player:",typ,"\n")
print("City:",city,"\n")

print("odi matches played:",odm,"\n")
print("Odi run:",odr,"\n")
print("odi wickets:",odw,"\n")
print("century in odi:",odc,"\n")
print("half-century in odi:",odhc,"\n")

print("T20 matches played:",tm,"\n")
print("T20 run:",tr,"\n")
print("t20 wickets:",tw,"\n")
print("century in T20:",tc,"\n")
print("half-century in T20:",thc,"\n")
print("\n\n\n")

print("Most matches played in Odi:",max(odm),"\t","Player name:",nm[odm.index(max(odm))],"\n")
print("Most Centuruy in odi:",max(odc),"\t","Player name:",nm[odc.index(max(odc))],"\n")
print("Most half-century in odi:",max(odhc),"\t","Player name:",nm[odhc.index(max(odhc))],"\n")
print("Most Wickets in odi:",max(odw),"\t","Player name:",nm[odw.index(max(odw))],"\n")
print("Most Runs in odi:",max(odr),"\t","player name:",nm[odr.index(max(odr))],"\n")

print("Most matches played in T20:",max(tm),"\t","Player name:",nm[tm.index(max(tm))],"\n")
print("Most Centuruy in T20:",max(tc),"\t","Player name:",nm[tc.index(max(tc))],"\n")
print("Most half-century in T20:",max(thc),"\t","Player name:",nm[thc.index(max(thc))],"\n")
print("Most Wickets in T20:",max(tw),"\t","Player name:",nm[tw.index(max(tw))],"\n")
print("Most Runs in T20:",max(tr),"\t","player name:",nm[tr.index(max(tr))],"\n")

print("Young player age:",min(bd),"Player name:","\t",nm[bd.index(min(bd))],"\n")
print("Old player age:",max(bd),"Player name:","\t",nm[bd.index(max(bd))],"\n")

print("Count Batsman in indian team",typ.count("Batsman"))
print("Count Bowler in indian team",typ.count("Bowler"))
print("Count All-Rounder in indian team",typ.count("All-Rounder"))


f1.close()
f2.close()
f3.close()
