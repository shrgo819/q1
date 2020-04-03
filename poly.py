import pandas
import numpy as np
def cost(X,y,theta):# calculates the squuared error vale or the cost function
    j=0
    m=np.size(y)
    x=np.matmul(X,theta)
    x=np.subtract(x,y)
    x=np.multiply(x,x)
    j=np.sum(x)
    j=j/m
    return j
def norm(X):#normalises the feature for efficeint running of gradient descent by subtraccting the mean of each feature of all examples and dividing by standard deviation
    s=np.size(X)
    a=np.empty(1,s[1])
    a=np.mean(X,0)
    xnorm=np.subtract(X,a)
    mu=np.std(X,0)
    for i in range(s[1]):
        xnorm[:,i]=np.divide(xnorm[:,i],mu[i])
    return xnorm
def graddescent(X, y, theta, alpha,num,lambd):# finds value of theta for which the cost function is minimum by moving the direction of partial derivative wrt all features
    m=np.size(X)
    d=m[1]
    for iter in range(num):#iterates over all the no of times after whhich minima is reached
        c=np.zeros(m[0],1)
        for i in range(m[0]):#iterates over all the examples in data set x
            c=np.add(c,np.matmul(np.subtract(np.matmul(np.transpose(theta),np.transpose(X[i])),y)))
        theta=np.subtract(theta,(alpha/m[0])*c)
    return theta
def pol(X,y,n):
    theta = np.zeros(np.size(y),1)# initialises theta vector
    for i in range(1,n):# adds higher power term to the feature like x squared upto x to power of n
        X=[X,np.multiply(X[:,0],X[:,i-1])]
    X=norm(X)
    X=[np.ones(np.size(y)),X]#adding a column of ones for the intercept term
    alpha=.01#step in gradient descent 
    iter= 4000
    theta=graddescent(X,y,theta,alpha,iter)
    return theta#returns the optimum vector theta which predicts values for normalised features
