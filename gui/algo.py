from numpy.linalg import *
from scipy.sparse import csr_matrix
from scipy.sparse.linalg import svds
import numpy as np
from scipy.sparse import csr_matrix,csc_matrix, lil_matrix
import sys
import time
sys.path.append('../Fraudar/fraudar-master/fraudar/export')
from greedy import *

def parseToMatrix(file):

    ind = 639
    data_s = lil_matrix((ind, ind), dtype=np.int8)
    count = 0
    with open(file,'r') as file:
        for line in file:
            count = count +1
            a,b = line.split(" ")
            try:
                data_s[int(a),int(b)] = 1
            except:
                print("count : ",count)
                print(a,"/",b)
                print("line:",line)
    return data_s

def runFbox(tau, k,file):
    matrix = parseToMatrix(file).asfptype()
    """
        run the algorithm.
        tau: the percentile in reconstructed degree threshold under which a node is considered suspicious
    """
    # k = 50 is selected based on Figure 3 of the paper
    
    num_users,num_products  = matrix.shape

    u, s, vt = svds(matrix, k=k)
    # reconstructed out degree
    recOutDeg = norm(u.dot(np.diag(s)), axis=1)
    # reconstructed in degree
    recInDeg = norm(vt.T.dot(np.diag(s)), axis=1)

    # detect users
    out_deg = matrix.sum(axis=1)
    out_deg = np.array(out_deg).reshape(-1, )
    unique_out_deg = np.unique(out_deg)

    # store the indices of suspicious users
    suspicious_users = {}
    thresholds = {}
    for d in unique_out_deg:
        # find users with original degree = d
        users = (out_deg == d)
        user_deg = recOutDeg[users]
        thresholds[d] = np.percentile(user_deg, tau)

    for i in range(num_users):
        user_d = out_deg[i]
        if recOutDeg[i] < thresholds[user_d]:

            if user_d not in suspicious_users:
                suspicious_users[user_d] = []
            suspicious_users[user_d].append(i)

    # detect products
    in_deg = matrix.sum(axis=0)
    in_deg = np.array(in_deg).reshape(-1, )
    unique_in_deg = np.unique(in_deg)

    # store the indices of suspicious users
    suspicious_products = {}
    thresholds = {}

    for d in unique_in_deg:
        prods = (in_deg == d)
        prod_deg = recInDeg[prods]
        thresholds[d] = np.percentile(prod_deg, tau)

    for i in range(num_products):
        prod_d = in_deg[i]
        if recInDeg[i] < thresholds[prod_d]:
            if prod_d not in suspicious_products:
                suspicious_products[prod_d] = []
            suspicious_products[prod_d].append(i)

    return suspicious_users, suspicious_products

def runLinear(file):
    return

def runFraudar(file):
    M = readData(file)
    retour = []
    retour.append("finished reading data: shape = "+ str(M.shape))
    retour.append("finished writing data")
    lwRes = logWeightedAveDegree(M)
    retour.append(lwRes)
    #np.savetxt("%s.rows" % (sys.argv[2], ), np.array(list(lwRes[0][0])), fmt='%d')
    #np.savetxt("%s.cols" % (sys.argv[2], ), np.array(list(lwRes[0][1])), fmt='%d')
    retour.append("score obtained is "+ str(lwRes[1]))
    return retour