"pip3 install matplotlib"
from matplotlib import pyplot as pl
import service
A1=service.score_evolution('a')
A2=service.score_evolution('b')
A3=service.score_evolution('c')

avg=service.avg()
y=[score for year,score in avg]
x=[str(year) for year,score in avg]
a=[score for year,score in A1]
b=[str(year) for year,score in A1]
c=[score for year,score in A2]
d=[str(year) for year,score in A2]
e=[score for year,score in A3]
f=[str(year) for year,score in A3]
pl.figure(figsize=(15,10))
pl.bar(x,y)
pl.xlabel('Years')
pl.ylabel('Scores')
pl.plot(b,a,'r-s',color='red',label='STU 1')
pl.plot(d,c,'r-s',color='black',label='STU 2')
pl.plot(f,e,'r-s',color='pink',label='STU 3')
pl.show()



