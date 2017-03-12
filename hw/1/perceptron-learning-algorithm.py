import numpy as np
import matplotlib.pyplot as plt
import random
from texttable import Texttable

x1 = random.uniform(-1, 1)
y1 = random.uniform(-1, 1)
x2 = random.uniform(-1, 1)
y2 = random.uniform(-1, 1)
X1 = []
X2 = []
result = []

def calculatetargetvalue(x1,x2,y1,y2,x,y):
    diff = (x2-x1)*(y-y1) - (y2-y1)*(x-x1)
    if diff >= 0:
        return 1
    else:
        return 0


t = Texttable()
buff = []
adder = [['X1','X2','Y']]
yt = []
f = open('data.txt','r')
#for i in range(20):
    #x = random.uniform(-1,1)
    #y = random.uniform(-1,1)
    #target = calculatetargetvalue(x1,x2,y1,y2,x,y)
x = 0.0
y = 0.0
target = 0.0
for i in f.readlines():
    wl = i.split('\t')
    x = float(wl[0])
    y = float(wl[1])
    target = int(wl[2])
    X1.append(x)
    X2.append(y)
    adder.append([x,y,target])
    buff.append([1,x,y])
    yt.append([target])

    if target == -1:
        target += 1

    result.append(target)
#    f.write(str(x)+'\t'+str(y)+'\t'+str(target))
#    f.write('\n')
t.add_rows(adder)
#f.close()
print(t.draw())


def calculateweights(x1,x2,w):
    return w[0] + w[1]*x1 + w[2]*x2



def train():
    converged = False
    weights = [0.0,0.0,0.0]
    iterations = 0
    print(X1,X2,weights)
    while(not converged):
        #iteration begin
        iterations += 1
        modified = False
        for index in range(20):
            predict = calculateweights(X1[index],X2[index],weights)
            actual = result[index]
            if predict >= 0:
                predict = 1
            else:
                predict = -1
            if actual == 0:
                actual = actual - 1
            if predict != actual:
                weights[0] += actual * 1
                weights[1] += actual * X1[index]
                weights[2] += actual * X2[index]
                print(weights)
                plt.figure()
                colormap = np.array(['r', 'k'])
                X1A = np.asarray(X1)
                X2A = np.asarray(X2)
                plt.scatter(X1, X2, c=colormap[result], s=40)
                ymin, ymax = -1,+1
                xx = np.linspace(ymin,ymax)
                slop = weights[1]/weights[2]
                yintercept = weights[0]/weights[2]
                yy = slop * xx + yintercept
                plt.plot(xx,yy,'--')
                axes = plt.gca()
                axes.set_xlim([-1,1])
                axes.set_ylim([-1,1])
                plt.savefig(str(iterations)+'.png', bbox_inches='tight')
                break
        if iterations == 50:
            converged = True
            #plt.show()
    print('weights with perceptron learning algorithm : ',weights)
def linearregression():
    m = np.asmatrix(buff)
    mt = m.getH()
    y1t = np.asmatrix(yt)

    weightsl = (mt*m).getI()*(mt*y1t)
    print('weights after applying linear regression : ')
    print(weightsl)
    colormap = np.array(['r', 'k'])
    print(X1)
    print(X2)
    ymin, ymax = -1,+1
    xx = np.linspace(ymin,ymax)
    slop = weightsl[1].item()/weightsl[2].item()
    yintercept = weightsl[0].item()/weightsl[2].item()
    yy = float(slop) * xx + float(yintercept)
    plt.plot(xx,yy,'--')
    axes = plt.gca()
    axes.set_xlim([-1,1])
    axes.set_ylim([-1,1])
    plt.savefig('linearregression.png', bbox_inches='tight')
train()
linearregression()
