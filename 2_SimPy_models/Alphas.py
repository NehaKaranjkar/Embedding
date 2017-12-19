import numpy as np
import matplotlib.pyplot as plt
import math


Tolerance=np.float64(1e-12)

# routine that returns True 
# if a float is close to an integer
# within a certain tolerance
def is_int(x,tolerance=Tolerance):
    if is_close(x, round(x), tolerance):
        return True
    else:
        return False

# routine that returns True 
# if a float is close to another
# within a certain tolerance
def is_close(x,y, tolerance=Tolerance):
    if (np.absolute(np.float64(x)-np.float64(round(y))) < tolerance):
        return True
    else:
       return False
 

# get_stencil:
# return a stencil of stencil_size/2 integers around a point y. 
# If y is itself (close to) an integer,
# the stencil just contains the single point y.
# Numbers outside the min and max bounds are ignored.
# Note: stencil size must be a multiple of 2.
#
# Example, for stencil_size = 6, min_bound=1, max_bound=10:
#
#   stencil(6.4) = [4,5,6,7,8,9]
#   stencil(2.7) = [1,2,3,4,5]
#   stencil(1.2) = [1,2,3,4]
#   stencil(9.1) = [7,8,9,10]
def get_stencil(y, y_min_bound, y_max_bound, stencil_size):

    P = max([1, int(stencil_size/2.0)])    
    assert(y_min_bound<y_max_bound)

    stencil=[]
    if(is_int(y)):
        stencil.append(int(y))
        return stencil
    else:
        for i in range(P):
            x = np.floor(y)-i
            if(x>=y_min_bound):
                stencil.insert(0, int(x))
        for i in range(P):
            x = np.ceil(y)+i
            if(x <=y_max_bound):
                stencil.append(int(x))
        return stencil


def L(k,y,stencil_y,s,r):
    
    stencil=stencil_y
    m = np.float64(stencil[0]-1)
    l = np.prod([( np.absolute( (np.float64(y)-m)**s - (np.float64(i)-m)**s))**r for i in stencil if (int(i)!=int(k))])
    return l


def alpha(k,y,stencil_y,s,r):
    
    stencil = stencil_y
    
    if(k in stencil):
        # K is in the stencil.
        a = L(k,y,stencil_y,s,r)/np.sum([L(i,y,stencil_y,s,r) for i in stencil])
        return a
    else:
        return 0.0
 

def get_stencil_and_alphas(y,y_min_bound, y_max_bound, stencil_size, s,r):
    stencil = get_stencil(y,y_min_bound,y_max_bound,stencil_size)
    alphas = []
    for k in stencil:
        alphas.append(alpha(k,y,stencil,s,r))
    return stencil, alphas

    
#plot alphas and their sum:
def plotAlphas(Y,alphas,K):

    alphas_sum=[]
    alphas_mean=[]
    for i in range(len(alphas[0])):
        alphas_sum.append(sum([alphas[k][i] for k in range(len(alphas))]))
        alphas_mean.append(sum([alphas[k][i]*(k+1) for k in range(len(alphas))]))
    
    colors=['green','red','blue','orange','magenta']
    yticks = [0,1]
    xticks = [i for i in range(1,K+1)]
    xlim = [0.8, K+0.2]
    ylim = [-0.2, 1.2]

    from pylab import rcParams
    rcParams['figure.figsize'] = 4, 6

    plt.grid()
    ax=[]

    for i in range(K):
        if(i==0): #plot alpha_1
            ax.append(plt.subplot(K+1,1,K+1-i))
            ax[0].set_xticks(xticks)
            ax[0].set_xlabel(r"$y$ ",rotation=0,fontsize=15)
            plt.setp(ax[0].get_xticklabels())

        
        else: # plot alpha_k (k>1)
            ax.append(plt.subplot(K+1,1,K+1-i, sharex=ax[0]))
            plt.setp(ax[i].get_xticklabels(), visible=False)
           
        plt.plot(Y,alphas[i],linewidth=2, color=colors[(i%len(colors))])
        ax[i].fill_between(Y,0,alphas[i], color=colors[(i%len(colors))], alpha = 0.3)
        ax[i].set_ylabel(r"$\alpha^{"+str(i+1)+"}(y)\quad$"+"  ",rotation=0,fontsize=15,labelpad=10)
        ax[i].set_yticks(yticks)
        ax[i].set_xlim(xlim)
        ax[i].set_ylim(ylim)
        ax[i].grid()

    #plot the sum of all alphas
    ax.append(plt.subplot(K+1,1,1, sharex=ax[0]))
    plt.setp(ax[K].get_xticklabels(), visible=False)
    plt.plot(Y,alphas_sum,linewidth=2, color="k")
    ax[K].set_ylabel(r"$\sum_{i=1}^{P}{\alpha^i (y)}\quad$ ",rotation=0,fontsize=12,labelpad=10)
    ax[K].set_yticks(yticks)
    ax[K].set_xlim(xlim)
    ax[K].set_ylim([0.7,1.4])
    ax[K].grid()


    plt.subplots_adjust(wspace=0, hspace=0, left=0.2)
    plt.legend()
    plt.savefig("alphas.pdf")
    plt.show()

def plot_moments(Y,alphas,alphas_mean,K):
    plt.figure(2)
    plt.plot(Y,alphas_mean,linewidth=2, color="K",label="Mean")

    #plot the r^th moment of the random variable
    for r in [2,3,4]:
        r_th_moment = [sum([alphas[i][y]*((i-alphas_mean[y])**r) for i in range (len(alphas)) ]) for y in range(len(Y))]
        plt.plot(Y,r_th_moment,linewidth=2, label="moment_"+str(r))
    plt.legend().draggable()
    plt.show()


#Test
def Test():
    K=5
    y_min_bound=1.0
    y_max_bound=K
    step=np.float64(0.01)
    Y=np.arange(y_min_bound,y_max_bound+step,step)
    s=2.0
    r=1.0
    stencil_size=2
    alphas =[]
    for k in range(1,K+1):
        alphas.append([alpha(k,y,get_stencil(y,y_min_bound,y_max_bound,stencil_size),s,r) for y in Y])
    
    print (get_stencil_and_alphas(y=2.5,y_min_bound=1, y_max_bound=10, stencil_size=4, s=1,r=1))
    plotAlphas(Y,alphas,K)

