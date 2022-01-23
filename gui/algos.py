import networkx as nx
import numpy as np
import matplotlib.pyplot as plt


from scipy.sparse import csr_matrix, lil_matrix
from scipy.sparse.csgraph import connected_components
from scipy.sparse import csc_matrix
from scipy.sparse.linalg import svds, eigs
from scipy.io import savemat, loadmat
import os
import pylab
from fbox import run

def executeFbox(mat):
    mat = loadmat('../data_out/data_amz.mat')
    adj = mat['M'].asfptype()
    adj = adj.transpose()
    sus_users, sus_prod = run(adj,20,50)
    retour = [" number of suspected users : "+len(sus_users)]
    retour.append(" number of suspected products : "+len(sus_prod))
    retour.append("Suspects users : ")
    se = ""
    for s in sus_users:
        se+=","+s
    retour.append(se)
    retour.append("Suspects products : ")
    se = ""
    for s in sus_prod:
        se+=","+s
    retour.append(se)
    return

def executeFraudar(mat):
    return


def executeLinear(mat):
    return