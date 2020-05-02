import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
import time

class data_cluster:
    def __init__(self,document,color):
        self.document = document
        self.color = color
        
    def load_txt_array(self):
        data = np.loadtxt(self.document, delimiter=" ")
        #Select z np.array data 0 index => x 
        arr_x = np.array([])
        for i in range(0,data.shape[0]):
            x = float(np.take(data[i],0))
            arr_x = np.append(arr_x,[x],axis = 0)
        #Select z np.array data 1 index => z 
        arr_y = np.array([])
        for i in range(0,data.shape[0]):
            x = float(np.take(data[i],1))
            arr_y = np.append(arr_y,[x],axis = 0)
        stack = np.stack((arr_x,arr_y))
        return stack
     
    def graph(self):
        array = self.load_txt_array()
        x = array[0]
        y = array[1]
        plt.grid()
        graph = plt.plot(x,y,'bo',c=self.color)
        return graph
    
    def cluster_img(self):
        #create cluster_img for dataset
        data = np.loadtxt(self.document, delimiter=" ")
        img = plt.imshow(data, interpolation='none', aspect='auto')
        doc = self.document
        plt.title("Claster for dataset "+doc)
        return img
    
    def get_x_values(self):
        array = self.load_txt_array()
        x = array[0]
        return x
    
    def get_y_values(self):
        array = self.load_txt_array()
        y = array[1]
        return y    
    
    def get_document(self):
        get_doc = self.document
        return get_doc

def show_graphs():
    plt.subplots_adjust(left=None, bottom=None, right=2, top=2, wspace=None, hspace=None)
    plt.subplot(2, 2, 1)
    cluster1.graph()
    plt.title('2D Visualisation of datasets ')
    plt.ylabel('Dataset1')

    plt.subplot(2, 2, 2)
    cluster2.graph()
    plt.ylabel('Dataset 2')

def show_clusters():
    plt.subplots_adjust( right=2, top=2)
    plt.subplot(2,2,1)
    cluster1.cluster_img()
    plt.xlabel('Cluster for Dataset 1')
    plt.subplot(2,2,2)
    cluster2.cluster_img()
    plt.xlabel('Cluster for Dataset 2')

def merge_graph():
    x1 = cluster1.get_x_values()
    x2 = cluster2.get_x_values()
    y1 = cluster1.get_y_values()
    y2 = cluster2.get_y_values()
    x = np.concatenate((x1, x2), axis=None)
    y = np.concatenate((y1, y2), axis=None)
    plt.scatter(x1, y1, c='green')
    plt.scatter(x2, y2, c='lightblue')
    graph = plt.show()
    return graph

def merge_dataset():
    d1 = np.loadtxt(cluster1.get_document(), delimiter=" ")
    d2 = np.loadtxt(cluster2.get_document(), delimiter=" ")
    merge_data = np.concatenate((d1,d2))
    return merge_data

def merge_cluster_img():
    merge_data = merge_dataset()
    img_plt = plt.imshow(merge_data, interpolation='none', aspect='auto')
    return img_plt