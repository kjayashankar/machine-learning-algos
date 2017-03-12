import numpy as np
import matplotlib.pyplot as plt
import math

learningrate = 0.2
x2 = [0.85 , 0.80 , -.88 , -0.99,- 0.7, -0.8 , -0.96, -0.8]
x1 = [0.9, 0.85, 0.15 , 0.25, -0.8, -0.9 , -0.83 , -0.7]
y = [ 1, 1, 1, 1, 0, 0, 0, 0]
weights = np.matrix('[0;1;2]')
data = np.array([x1,x2])
y = np.array(y)
plt.figure()
colormap = np.array(['r', 'k'])
plt.scatter(data[0], data[1], c=colormap, s=40)
#line = plt.plot((1, -1),(0.5, -0.5) ,'g')
#plot.setp(line, color='r',linewidth = 2.0)
#xintercept = weights[0].item()/weights[1].item()
#yintercept = weights[0].item()/weights[2].item()
#line1 = plt.plot((-1*xintercept,0),(0, -1*yintercept) ,'r')
#line = plt.plot((0.5,0),(0,0.5 ) ,'g')
#plt.show()
converged = False
iterations = 0
while(not converged):
    iterations += 1
    index = 0
    while(index < len(x1)):
        currx = np.matrix([1, x1[index], x2[index]])
        cy = y[index]
        if cy == 0: cy = -1
        prod = round((currx*weights).item(),5)
        if( cy == 1 and prod < 0 ):
            # sum the weights
            weights = weights + (cy) * weights
            print('weights changed, iteration : + ',weights,round((currx*weights).item(),5))
            print('\n\n')

        elif( cy == -1 and prod >= 0):
            # subtract weights
            weights = weights + (cy) * weights
            print('weights changed, iteration : - ',weights,round((currx*weights).item(),5))
            print('\n\n')


        else:
            pass
        index += 1
    if iterations == 10: converged = True
#print(prod , cy)
slop = weights[1].item()/weights[2].item()
yintercept = weights[0].item()/weights[2].item()
plt.scatter(data[0], data[1], c=colormap[y], s=40)
#line = plt.plot((-1*xintercept,0),(0, -1*yintercept) ,'g')
ymin, ymax = plt.ylim()
xx = np.linspace(ymin,ymax)
yy = slop * xx + yintercept

plt.plot(xx,yy,'--')

print('final weights', weights)
plt.show()
