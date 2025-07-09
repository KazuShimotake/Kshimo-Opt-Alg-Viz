import math
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb

# given 3 points, find the parabola params that
# pass through those points
def find_para_params(x0,x1,x2,f0,f1,f2):
    F = np.array([f0,f1,f2])
    X = np.array([
        [x0**2, x0, 1],
        [x1**2, x1, 1],
        [x2**2, x2, 1]
    ])
    Xinv = np.linalg.inv(X)
    return np.dot(Xinv,F)

# minimize a function of one variable using successive parabolas
def s_paras(f,x0,x2, eps = 1e-6):
    plt.axhline(y=0, color='k')
    plt.axvline(x=0, color='k')
    xold = np.linspace(-5,5,20)
    yold = [f(x) for x in xold]
    plt.plot(xold,yold, linewidth=3)
    count = 0
    # need some kind of iteration
    # while loop to keep track of the spread of points - stop when points are spread
    # out less than eps
    test = 0
    while(abs(x2-x0)>eps):
        x1 = (x0+x2)/2

        f0,f1,f2 = [f(x) for x in [x0, x1, x2]]
        count+=3

        # plt.figure(test)
        a,b,c = find_para_params(x0,x1,x2,f0,f1,f2)
        print("a,b,c:",a,b,c)
        print("x0,x2:",x0,x2)
        x = np.linspace(-5,5,20)
        y = [a*x**2 + b*x + c for x in x]
        # print(y)
        # sb.lineplot(x = x, y = y)
        print("made a plot")
        plt.plot(x,y)
        test+=1

        # need to make sure a is not zero
        # if it is, you should take a different sort of step
        
        # This checks if the points are collinear
        m1 = (f1-f0)/(x1-x0)
        m2 = (f2-f1)/(x2-x1)
        change = (x2 - x0) / 2
        if m1==m2:
            print("1")
            if m1>0:
                count+=1
                if f(x0-eps)>f(x0):
                    # plt.show()
                    return {"x":x0,"fun":f0,"count":count}
                x0-=change
            else:
                count+=1
                if f(x2+eps)>f(x2):
                    plt.show()
                    return {"x":x2,"fun":f2,"count":count}
                x2+=change
        elif a == 0:
            print("2")
            if b > 0:
                x0-=change
            else:
                x2+=change
        else:
            print("3")
            # need to find the min of our parabola, xnew
            xnew = (-b)/(2*a)
            print("xnew:",xnew)
            if abs(xnew-x1)<eps:  
                print("abs")
                # plt.show()
                return {"x":x1,"fun":f1,"count":count}
            # elif abs(xnew-x0)<eps:  
            #     print("abs")
            #     plt.show()
            #     return {"x":x0,"fun":f1,"count":count}
            # if abs(xnew-x2)<eps:  
            #     print("abs")
            #     plt.show()
            #     return {"x":x2,"fun":f1,"count":count}
            elif xnew<x0 and xnew<x2:
                print("<<")
                x0 = xnew
            elif xnew>x0 and xnew>x2:
                print(">>")
                x2 = xnew
            elif abs(x0 - xnew) > abs(x2 - xnew):
                print("-")
                x0 = xnew
            else:
                print("else")
                x2 = xnew
    min_idx = sorted([0,1,2,],key=lambda x: [f0,f1,f2][x])[0]
    min_x = [x0,x1,x2][min_idx]
    min_f = [f0,f1,f2][min_idx]
    plt.show()
    print("min_x:",min_x)
    return {"x":min_x,"fun":min_f,"count":count}

if __name__ == '__main__':
    # (5,-2.5)
    def f1(x):
        return x**2 - 5*x + 10
    # (-3.75,-76.25)
    def f2(x):
        return 4*x**2 + 30*x - 20
    # (-1.93598,-56.0635)
    def f3(x):
        return x**4
    # (5,0)
    def f4(x):
        return .02*x**2 - .2*x + .5
    # (-50,-100)
    def f5(x):
        return abs(x)
    def f6(x):
        return (x-1)**2+1
    
    s_paras(f3,-5,4)

    # x = [0,1,2]
    # y = [0,1,2]
    # a = [3,4,5]
    # b = [3,4,5]
    # plt.scatter(x,y)
    # plt.scatter(a,b)
    # plt.show()