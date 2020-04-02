import pandas
import numpy as np
def cost(X,y,theta,lambd):
    j=0
    m=np.size(y)
    x=np.matmul(X,theta)
    x=np.subtract(x,y)
    x=np.multiply(x,x)
    j=np.sum(x)
    j=j/m
    j=j+(lambd/2)*(np.sum(np.multiply(theta,theta)))
    j=j-(theta[0]**2)*(lambd/2)
    return j
def norm(X):
    s=np.size(X)
    a=np.empty(1,s[1])
    a=np.mean(X,0)
    xnorm=np.subtract(X,a)
    mu=np.std(X,0)
    for i in range(s[1]):
        xnorm[:,i]=np.divide(xnorm[:,i],mu[i])
    return xnorm
def graddescent(X, y, theta, alpha,num,lambd):
    m=np.size(X)
    d=m[1]
    for iter in range(num):
        c=np.zeros(m[0],1)
        for i in range(m[0]):
            c=np.add(c,np.matmul(np.subtract(np.matmul(np.transpose(theta),np.transpose(X[i])),y)))
        c=np.divide(np.add(c,lambd*theta),m[0])
        c[0]=c[0]-(theta[0]*lambd)/m[0]
        theta=np.subtract(theta,(alpha/m[0])*c)
    return theta
def pol(X,y):
    theta = np.zeros(np.size(y),1)
    X=norm(X)
    X=[np.ones(np.size(y)),X]
    alpha=.01
    iter= 4000
    lambd=1
    min=9999999
    for i in range(1,10):    
        if min< cost(X,y,theta,lambd):
            min=cost(X,y,theta,lambd)
            theta=graddescent(X,y,theta,alpha,iter,lambd+i)
    return theta

        

                 