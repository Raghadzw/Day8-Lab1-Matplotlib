import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

plt.plot([100,200,300], [2015,2016,2017])
plt.xlabel("Sales", fontsize = 16)
plt.ylabel("Year" ,fontsize = 16)
plt.show()

plt.plot(pd.DataFrame([1000,2000,3000]))
plt.xlabel("Quantity" , fontsize = 16 )
plt.show()

plt.pie(np.arange(1,8), labels=['Sun','Mon','Tue', 'Wed',"Thu", "Fri" ,"Sat"], explode = [.1,.2,.3,.5,.4,.9,.7]);
plt.show()


x = np.random.randn(30)
y = np.random.randn(30)
z =plt.scatter(x, y , alpha=0.4 , s=50)
plt.title('Scatter Chart',color="red" , loc="left")
plt.show()

plt.plot([1,2,3,4,5] ,c="blue")
plt.plot([7,8,9,10], c="m")
plt.plot([11,12,13,14], c= "000000")
plt.legend(['2005','2006','2007'], loc = "upper left")
plt.show()




plt.figure(figsize=[20,10])
plt.suptitle('Subplots')

plt.subplot(1,3,1)
plt.pie(np.arange(1,4),labels=['Apple','Kiwi','Banana']);
plt.title('Fruits')
plt.show()

plt.subplot(1,3,2)
plt.plot([1,2,3])
plt.plot([10,9,8])
plt.legend(['2006','2007'])
plt.title('Years')
plt.show()

plt.subplot(1,3,3)
plt.plot([1000,2000,3000])
plt.plot([1,3,8])
plt.legend(['2019','2020'])
plt.title('Sales')
plt.show()
