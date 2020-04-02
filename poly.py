import pandas
import numpy as np
def cost(X,y,theta):
    j=0
    m=np.size(y)
    x=np.matmul(X,theta)
    x=np.subtract(x,y)
    x=np.multiply(x,x)
    j=np.sum(x)
    j=j/m
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
        theta=np.subtract(theta,(alpha/m[0])*c)
    return theta
def pol(X,y,n):
    theta = np.zeros(np.size(y),1)
    for i in range(1,n):
        X=[X,np.multiply(X[:,0],X[:,i-1])]
    X=norm(X)
    X=[np.ones(np.size(y)),X]
    alpha=.01
    iter= 4000
    theta=graddescent(X,y,theta,alpha,iter)
    return theta
