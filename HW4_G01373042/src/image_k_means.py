# -*- coding: utf-8 -*-
"""Image_K-Means.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1eyDurXWKLgZVNY5CNBHrkjJ6b7FRGk_F
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import warnings
warnings.simplefilter("ignore")

image_data=pd.read_csv('/content/drive/MyDrive/image.txt', sep=",",header=None)

image_data.head()

image_data.describe()

# from sklearn.decomposition import TruncatedSVD

# svd = TruncatedSVD(n_components=11)
# image_data_svd = svd.fit_transform(image_data)
# print(svd.explained_variance_ratio_)

image_data.shape

image_data.tail()

# print(svd.explained_variance_ratio_.sum())

image_data.info()

def euclidean_distance(point1, point2):
  dist = np.linalg.norm(point1 - point2)
  return dist

def manhattan_distance(point1, point2):
    return np.sum([abs(value1 - value2) for value1, value2 in zip(point1, point2)])

def cosine_similarity(point1,point2):
  return np.dot(point1, point2) / (np.linalg.norm(point1) * np.linalg.norm(point2))

def sse_k(data,cluster,centroids,K):
  sse = []
  count = [0]*K
  dist = [0]*K
  
  for i in range(data.shape[0]):
    value = cluster[i]
    dist[value-1]+= (euclidean_distance(data[i],centroids[value-1])**2)
    count[value-1]+=1
  # print(count[0])
  # print(count[1])
  # print(count[2])
  # print(count[3])
  # print(count[4])
  # print(count[5])
  # print(count[6])
  # print(count[7])
  # print(count[8])
  # print(count[9])
  
  # print(dist1)
  # print(dist2)
  # print(dist3)
  # print(dist4)
  # print(dist5)
  # print(dist6)
  # print(dist7)
  # print(dist8)
  # print(dist9)
  # print(dist10)
  #sse_1 = (dist1/count1)+(dist2/count2)+(dist3/count3)+(dist4/count4)+(dist5/count5)+(dist6/count6)+(dist7/count7)+(dist8/count8)+(dist9/count9)+(dist10/count10)
  #sse.append(sse_1)
  sse_1 = sum(dist)
  #sse_total = np.array(sse)
  return sse_1,count

def ssb(data,count,centroids,K):
  cent_1 = [0]*len(centroids[0])
  for i in range(K):
    cent_1 += centroids[i]
  
  cent_1 /= K

  
  print(cent_1)
  value = 0
  for i in range(K):
    print((euclidean_distance(centroids[i],cent_1)**2))
    value+= count[i]*(euclidean_distance(centroids[i],cent_1)**2)
    print(value,i)
  return value

image_data_np = image_data.to_numpy()
image_np = image_data_np/255

!pip install umap-learn
import umap

reducer = umap.UMAP(n_components=2)
image_data_umap = reducer.fit_transform(image_data_np)

image_data_umap

from sklearn.manifold import TSNE

model = TSNE(n_components=2, random_state=0)
image_data_tsne = model.fit_transform(image_data_np)

image_data_tsne

import random
from collections import defaultdict
def K_Means_predict_man(data,K,max_iter,rand_seed):
  centroids = defaultdict(int)
  cluster = [0]*data.shape[0]
  random.seed(rand_seed)
  mylist = np.arange(data.shape[0])
  list1 = mylist.tolist()
  x = random.sample(list1,K)
  #print(x)
  for i in range(K):
  #initializing 1st cluster center
    num1 = x[i]
    #print(data[num1])
    centroids[i] = data[num1]

  iter=0
  #print(2)

  for iteration in range(max_iter):
    iter+=1
    labels=defaultdict(list)
    #print(data.shape)
    #print(centroids)

    for keys in range(K):
      labels[keys]=[]

    for datapoint1 in range(len(data)):
      distance=[]
      for datapoint2 in range(K):
        dist=manhattan_distance(data[datapoint1],centroids[datapoint2])
        #print("Dp",data[i])
        #print("Cent",centroids[j])
        #print(dist)
        distance.append(dist)
      min_distance=min(distance)
      index=distance.index(min_distance)
      labels[index].append(data[datapoint1])
      cluster[datapoint1] = index+1
      centroid_old=dict(centroids)
    
    for i in range(K):
      label=labels[i]
    
      centroid_new=np.mean(label,axis=0)
      centroids[i]=centroid_new
      flag=1

    for i in range(K):
      a=centroids[i]
      b=centroid_old[i]
      temp = 0
      for i in range(len(a)):
        d = abs(a[i] - b[i])
        temp+=d
      if temp !=0:
        flag = 0

      
    if flag==1:
      break
  #print(iter)
  return labels,centroids,cluster,iter

import random
from collections import defaultdict
def K_Means_predict(data,K,max_iter,rand_seed):
  centroids = defaultdict(int)
  cluster = [0]*data.shape[0]
  random.seed(rand_seed)
  mylist = np.arange(data.shape[0])
  list1 = mylist.tolist()
  x = random.sample(list1,K)
  print("Initial Cluster Center Indices \n",x)
  print("Initial Cluster Centers\n")
  for i in range(K):
  #initializing 1st cluster center
    num1 = x[i]
    #print(data[num1])
    centroids[i] = data[num1]

  iter=0
  #print(2)

  for iteration in range(max_iter):
    iter+=1
    labels=defaultdict(list)
    #print(data.shape)
    #print(centroids)

    for keys in range(K):
      labels[keys]=[]

    for datapoint1 in range(len(data)):
      distance=[]
      for datapoint2 in range(K):
        dist=euclidean_distance(data[datapoint1],centroids[datapoint2])
        #print("Dp",data[i])
        #print("Cent",centroids[j])
        #print(dist)
        distance.append(dist)
      min_distance=min(distance)
      index=distance.index(min_distance)
      labels[index].append(data[datapoint1])
      cluster[datapoint1] = index+1
      centroid_old=dict(centroids)
    
    for i in range(K):
      label=labels[i]
    
      centroid_new=np.mean(label,axis=0)
      centroids[i]=centroid_new
      flag=1

    for i in range(K):
      a=centroids[i]
      b=centroid_old[i]
      temp = 0
      for i in range(len(a)):
        d = abs(a[i] - b[i])
        temp+=d
      if temp !=0:
        flag = 0

      
    if flag==1:
      break
  #print(iter)
  return labels,centroids,cluster,iter

import random
from collections import defaultdict
def K_Means_predict_man1(data,K,max_iter,rand_seed):
  centroids = defaultdict(int)
  cluster = [0]*data.shape[0]
  random.seed(rand_seed)
  mylist = np.arange(data.shape[0])
  list1 = mylist.tolist()
  x = random.sample(list1,K)
  #print(x)
  for i in range(K):
  #initializing 1st cluster center
    num1 = x[i]
    #print(data[num1])
    centroids[i] = data[num1]

  iter=0
  #print(2)

  for iteration in range(max_iter):
    iter+=1
    labels=defaultdict(list)
    #print(data.shape)
    #print(centroids)

    for keys in range(K):
      labels[keys]=[]

    for datapoint1 in range(len(data)):
      distance=[]
      for datapoint2 in range(K):
        dist=manhattan_distance(data[datapoint1],centroids[datapoint2])
        #print("Dp",data[i])
        #print("Cent",centroids[j])
        #print(dist)
        distance.append(dist)
      min_distance=min(distance)
      index=distance.index(min_distance)
      labels[index].append(data[datapoint1])
      cluster[datapoint1] = index+1
      centroid_old=dict(centroids)
    
    for i in range(K):
      label=labels[i]
    
      centroid_new=np.median(label,axis=0)
      centroids[i]=centroid_new
      flag=1

    for i in range(K):
      a=centroids[i]
      b=centroid_old[i]
      temp = 0
      for i in range(len(a)):
        d = abs(a[i] - b[i])
        temp+=d
      if temp !=0:
        flag = 0

      
    if flag==1:
      break
  #print(iter)
  return labels,centroids,cluster,iter

import random
from collections import defaultdict
def K_Means_predict1(data,K,max_iter,rand_seed):
  centroids = defaultdict(int)
  cluster = [0]*data.shape[0]
  random.seed(rand_seed)
  mylist = np.arange(data.shape[0])
  list1 = mylist.tolist()
  x = random.sample(list1,K)
  #print(x)
  for i in range(K):
  #initializing 1st cluster center
    num1 = x[i]
    centroids[i] = data[num1]

  iter=0
  #print(2)

  for iteration in range(max_iter):
    iter+=1
    labels=defaultdict(list)
    #print(data.shape)
    #print(centroids)

    for keys in range(K):
      labels[keys]=[]

    for datapoint1 in range(len(data)):
      distance=[]
      for datapoint2 in range(K):
        dist=euclidean_distance(data[datapoint1],centroids[datapoint2])
        #print("Dp",data[i])
        #print("Cent",centroids[j])
        #print(dist)
        distance.append(dist)
      min_distance=min(distance)
      index=distance.index(min_distance)
      labels[index].append(data[datapoint1])
      cluster[datapoint1] = index+1
      centroid_old=dict(centroids)
    
    for i in range(K):
      label=labels[i]
    
      centroid_new=np.median(label,axis=0)
      centroids[i]=centroid_new
      flag=1

    for i in range(K):
      a=centroids[i]
      b=centroid_old[i]
      temp = 0
      for i in range(len(a)):
        d = abs(a[i] - b[i])
        temp+=d
      if temp !=0:
        flag = 0

      
    if flag==1:
      break
  #print(iter)
  return labels,centroids,cluster,iter

import random
from collections import defaultdict
def K_Means_predict_cos(data,K,max_iter,rand_seed):
  centroids = defaultdict(int)
  cluster = [0]*data.shape[0]
  random.seed(rand_seed)
  mylist = np.arange(data.shape[0])
  list1 = mylist.tolist()
  x = random.sample(list1,K)
  #print(x)
  for i in range(K):
  #initializing 1st cluster center
    num1 = x[i]
    centroids[i] = data[num1]

  iter=0
  #print(2)

  for iteration in range(max_iter):
    iter+=1
    labels=defaultdict(list)
    #print(data.shape)
    #print(centroids)

    for keys in range(K):
      labels[keys]=[]

    for datapoint1 in range(len(data)):
      distance=[]
      for datapoint2 in range(K):
        dist=cosine_similarity(data[datapoint1],centroids[datapoint2])
        #print("Dp",data[i])
        #print("Cent",centroids[j])
        #print(dist)
        distance.append(dist)
      min_distance=max(distance)
      index=distance.index(min_distance)
      labels[index].append(data[datapoint1])
      cluster[datapoint1] = index+1
      centroid_old=dict(centroids)
    
    for i in range(K):
      label=labels[i]
    
      centroid_new=np.mean(label,axis=0)
      #print(centroid_new)
      centroids[i]=centroid_new
      flag=1

    for i in range(K):
      a=centroids[i]
      b=centroid_old[i]
      temp = 0
      #print(a)
      #print(b)
      for i in range(len(a)):
        d = abs(a[i] - b[i])
        temp+=d
      if temp !=0:
        flag = 0

      
    if flag==1:
      break
  #print(iter)
  return labels,centroids,cluster,iter

import random
from collections import defaultdict
def K_Means_predict_cos1(data,K,max_iter,rand_seed):
  centroids = defaultdict(int)
  cluster = [0]*data.shape[0]
  random.seed(rand_seed)
  mylist = np.arange(data.shape[0])
  list1 = mylist.tolist()
  x = random.sample(list1,K)
  #print(x)
  for i in range(K):
  #initializing 1st cluster center
    num1 = x[i]
    centroids[i] = data[num1]

  iter=0
  #print(2)

  for iteration in range(max_iter):
    iter+=1
    labels=defaultdict(list)
    #print(data.shape)
    #print(centroids)

    for keys in range(K):
      labels[keys]=[]

    for datapoint1 in range(len(data)):
      distance=[]
      for datapoint2 in range(K):
        dist=cosine_similarity(data[datapoint1],centroids[datapoint2])
        #print("Dp",data[i])
        #print("Cent",centroids[j])
        #print(dist)
        distance.append(dist)
      min_distance=max(distance)
      index=distance.index(min_distance)
      labels[index].append(data[datapoint1])
      cluster[datapoint1] = index+1
      centroid_old=dict(centroids)
    
    for i in range(K):
      label=labels[i]
    
      centroid_new=np.median(label,axis=0)
      centroids[i]=centroid_new
      flag=1

    for i in range(K):
      a=centroids[i]
      b=centroid_old[i]
      temp = 0
      for i in range(len(a)):
        d = abs(a[i] - b[i])
        temp+=d
      if temp !=0:
        flag = 0

      
    if flag==1:
      break
  #print(iter)
  return labels,centroids,cluster,iter

# from sklearn.decomposition import PCA

# pca = PCA(n_components=0.95)
# image_data_pca = pca.fit_transform(image_data)

sse_2 = []
value1 = 20
iterations = np.arange(value1)
iterations1 = np.arange(2,21,2)
from collections import defaultdict
for K in range(2,21,2):
  sse_1 = []
  for rand_seed in range(value1):
    classes,centroids,cluster,iter=K_Means_predict(image_data_tsne,K,10000,rand_seed)
  # classes1,centroids1,cluster1,iter1=K_Means_predict1(image_data_tsne,10,10000,rand_seed)
  # classes2,centroids2,cluster2,iter2=K_Means_predict_man(image_data_tsne,10,10000,rand_seed)
  # classes3,centroids3,cluster3,iter3=K_Means_predict_man1(image_data_tsne,10,10000,rand_seed)
  # classes4,centroids4,cluster4,iter4=K_Means_predict_cos(image_data_tsne,10,10000,rand_seed)
  # classes5,centroids5,cluster5,iter5=K_Means_predict_cos1(image_data_tsne,10,10000,rand_seed)
    for i in range(0,10):
      classes[i]=np.array(classes[i]).tolist()
    # for i in range(0,10):
    #   classes1[i]=np.array(classes1[i]).tolist()
    print("Iteration=%d \n"%rand_seed)    
    print("Euclidean")
    print("Mean \n")
    print("Max Iteratins Run=%d \n"%iter)
    print("Final Centroids:",centroids)
    print("\n")
    SSE,count = sse_k(image_data_tsne,cluster,centroids,K)
    sse_1.append(SSE)
  print(sse_1)
  x = plt.subplot( )
  x.plot(iterations, sse_1, label='SSE')
  #x.plot(k_1, cv_auc, label='AUC CV')
  plt.title('Runs vs SSE')
  plt.xlabel('Random Center')
  plt.ylabel('SSE')
  x.legend()
  plt.show()
  sse_2.append(min(sse_1))

x = plt.subplot( )
x.plot(iterations1, sse_2, label='SSE')
#x.plot(k_1, cv_auc, label='AUC CV')
plt.title('K vs SSE')
plt.xlabel('K')
plt.ylabel('SSE')
x.legend()
plt.show()


  # for i in range(0,10):
  #  print("Cluster %d"%i,len(classes[i]))
  # print("Median \n")
  # print("Max Iteratins Run=%d \n"%iter1)
  # print("Final Centroids:",centroids1)
  # print("\n")  
  # for i in range(0,10):
  #   print("Cluster %d"%i,len(classes1[i]))
  # print("\n")
  # print("Manhattan")
  # print("Mean \n")
  # print("Max Iteratins Run=%d \n"%iter2)
  # print("Final Centroids:",centroids2)
  # print("\n")
  # for i in range(0,10):
  #   print("Cluster %d"%i,len(classes2[i]))
  # print("Median \n")
  # print("Max Iteratins Run=%d \n"%iter3)
  # print("Final Centroids:",centroids3)
  # print("\n")  
  # for i in range(0,10):
  #   print("Cluster %d"%i,len(classes3[i]))
  # print("\n")
  # print("Cosine")
  # print("Mean \n")
  # print("Max Iteratins Run=%d \n"%iter4)
  # print("Final Centroids:",centroids4)
  # print("\n")
  # for i in range(0,10):
  #   print("Cluster %d"%i,len(classes4[i]))
  # print("Median \n")
  # print("Max Iteratins Run=%d \n"%iter5)
  # #print("Final Centroids:",centroids5)
  # print("\n")  
  # for i in range(0,10):
  #   print("Cluster %d"%i,len(classes5[i]))
  #print("\n")
  #print("**********XXXXX********")
  #print(centroids)

# pca1 = PCA(n_components=10)
# image_data_pca1 = pca.fit_transform(image_data)

rand_seed = 0
classes,centroids,cluster,iter=K_Means_predict(image_data_umap,10,10000,rand_seed)
for i in range(0,10):
  classes[i]=np.array(classes[i]).tolist()
  
for i in range(0,10):
  print(len(classes[i]))

print(iter)

# for i in range(0,10):
#     classes[i]=np.array(classes[i]).tolist()
    
# for i in range(0,10):
#     print(len(classes[i]))
# #print(centroids)

print(cluster)

with open('image_cluster75.txt', 'w') as f:
  for i in cluster:
    f.write(str(i) +"\n")

# from sklearn.preprocessing import StandardScaler

# scaler = StandardScaler()
# image_data_sc = scaler.fit_transform(image_data)
# #print(scaler.mean_)

# image_data_pca.shape

# import matplotlib.pyplot as plt
# import seaborn as sns
# sns.set(style='whitegrid')
# plt.plot(np.cumsum(pca.explained_variance_ratio_))
# plt.xlabel('number of components')
# plt.ylabel('cumulative explained variance')
# plt.axvline(linewidth=4, color='r', linestyle = '--', x=152, ymin=0, ymax=1)
# display(plt.show())
# evr = pca.explained_variance_ratio_
# cvr = np.cumsum(pca.explained_variance_ratio_)
# pca_df = pd.DataFrame()
# pca_df['Cumulative Variance Ratio'] = cvr
# pca_df['Explained Variance Ratio'] = evr
# display(pca_df.head(152))

# classes,centroids,cluster=K_Means_predict(image_data_pca,10,10000)

# for i in range(0,10):
#     classes[i]=np.array(classes[i]).tolist()
    
# for i in range(0,10):
#     print(len(classes[i]))
# #print(centroids)

# print(cluster)

# with open('image_cluster67.txt', 'w') as f:
#   for i in cluster:
#     f.write(str(i) +"\n")

# #image_data = image_data.astype('float32') 
# #image_data = image_data / 255.0
# image_data_1 = image_data.to_numpy()

# image_data_1.shape

# for rand_seed in range(100):  
#   classes,centroids,cluster,iter=K_Means_predict(image_data_tsne,10,10000,rand_seed)
#   for i in range(0,10):
#       classes[i]=np.array(classes[i]).tolist()
#   values = []  
#   for i in range(0,10):
#       values.append(len(classes[i]))
#   print(values)
  # print("\n")

# classes,centroids,cluster=K_Means_predict(image_data_1,10,10000,10)
# for i in range(0,10):
#     classes[i]=np.array(classes[i]).tolist()
# values = []  
# for i in range(0,10):
#     values.append(len(classes[i]))
# print(values)
# print("\n")

# print(cluster)

# with open('image_cluster76.txt', 'w') as f:
#   for i in cluster:
#     f.write(str(i) +"\n")

# from sklearn.manifold import TSNE

# model = TSNE(n_components=2, random_state=0,metric = 'cosine')
# image_data_tsne = model.fit_transform(image_data_np)

# for rand_seed in range(100):  
#   classes,centroids,cluster,iter=K_Means_predict_cos1(image_data_tsne,10,10000,rand_seed)
#   print("Iteration = %i"%rand_seed)
#   print("Iter %i"%iter)
#   for i in range(0,10):
#       classes[i]=np.array(classes[i]).tolist()
#   values = []  
#   for i in range(0,10):
#       values.append(len(classes[i]))
#   print(values)
#   print("\n")

# # classes,centroids,cluster=K_Means_predict(image_data_1,10,10000,10)
# # for i in range(0,10):
# #     classes[i]=np.array(classes[i]).tolist()
# # values = []  
# # for i in range(0,10):
# #     values.append(len(classes[i]))
# # print(values)
# # print("\n")

# from sklearn.manifold import MDS
# embedding = MDS(n_components=2)

# image_data_mds = embedding.fit_transform(image_data_np)

# for rand_seed in range(100):  
#   classes,centroids,cluster,iter=K_Means_predict(image_data_tsne,10,10000,rand_seed)
#   print("Iteration = %i"%rand_seed)
#   print("Iter %i"%iter)
#   for i in range(0,10):
#       classes[i]=np.array(classes[i]).tolist()
#   values = []  
#   for i in range(0,10):
#       values.append(len(classes[i]))
#   print(values)
#   print("\n")

# # classes,centroids,cluster=K_Means_predict(image_data_1,10,10000,10)
# # for i in range(0,10):
# #     classes[i]=np.array(classes[i]).tolist()
# # values = []  
# # for i in range(0,10):
# #     values.append(len(classes[i]))
# # print(values)
# # print("\n")

# image_data_mds

sse_2 = []
value1 = 20
iterations = np.arange(value1)
iterations1 = np.arange(2,21,2)
from collections import defaultdict
for K in range(2,21,2):
  sse_1 = []
  for rand_seed in range(value1):
    classes,centroids,cluster,iter=K_Means_predict(image_data_umap,K,10000,rand_seed)
  # classes1,centroids1,cluster1,iter1=K_Means_predict1(image_data_tsne,10,10000,rand_seed)
  # classes2,centroids2,cluster2,iter2=K_Means_predict_man(image_data_tsne,10,10000,rand_seed)
  # classes3,centroids3,cluster3,iter3=K_Means_predict_man1(image_data_tsne,10,10000,rand_seed)
  # classes4,centroids4,cluster4,iter4=K_Means_predict_cos(image_data_tsne,10,10000,rand_seed)
  # classes5,centroids5,cluster5,iter5=K_Means_predict_cos1(image_data_tsne,10,10000,rand_seed)
    for i in range(0,10):
      classes[i]=np.array(classes[i]).tolist()
    # for i in range(0,10):
    #   classes1[i]=np.array(classes1[i]).tolist()
    print("Iteration=%d \n"%rand_seed)    
    print("Euclidean")
    print("Mean \n")
    print("Max Iteratins Run=%d \n"%iter)
    print("Final Centroids:",centroids)
    print("\n")
    SSE,count = sse_k(image_data_umap,cluster,centroids,K)
    sse_1.append(SSE)
  print(sse_1)
  x = plt.subplot( )
  x.plot(iterations, sse_1, label='SSE')
  #x.plot(k_1, cv_auc, label='AUC CV')
  plt.title('Runs vs SSE')
  plt.xlabel('Random Center')
  plt.ylabel('SSE')
  x.legend()
  plt.show()
  sse_2.append(min(sse_1))

x = plt.subplot( )
x.plot(iterations1, sse_2, label='SSE')
#x.plot(k_1, cv_auc, label='AUC CV')
plt.title('K vs SSE')
plt.xlabel('K')
plt.ylabel('SSE')
x.legend()
plt.show()


  # for i in range(0,10):
  #  print("Cluster %d"%i,len(classes[i]))
  # print("Median \n")
  # print("Max Iteratins Run=%d \n"%iter1)
  # print("Final Centroids:",centroids1)
  # print("\n")  
  # for i in range(0,10):
  #   print("Cluster %d"%i,len(classes1[i]))
  # print("\n")
  # print("Manhattan")
  # print("Mean \n")
  # print("Max Iteratins Run=%d \n"%iter2)
  # print("Final Centroids:",centroids2)
  # print("\n")
  # for i in range(0,10):
  #   print("Cluster %d"%i,len(classes2[i]))
  # print("Median \n")
  # print("Max Iteratins Run=%d \n"%iter3)
  # print("Final Centroids:",centroids3)
  # print("\n")  
  # for i in range(0,10):
  #   print("Cluster %d"%i,len(classes3[i]))
  # print("\n")
  # print("Cosine")
  # print("Mean \n")
  # print("Max Iteratins Run=%d \n"%iter4)
  # print("Final Centroids:",centroids4)
  # print("\n")
  # for i in range(0,10):
  #   print("Cluster %d"%i,len(classes4[i]))
  # print("Median \n")
  # print("Max Iteratins Run=%d \n"%iter5)
  # #print("Final Centroids:",centroids5)
  # print("\n")  
  # for i in range(0,10):
  #   print("Cluster %d"%i,len(classes5[i]))
  #print("\n")
  #print("**********XXXXX********")
  #print(centroids)

rand_seed = 7
classes,centroids,cluster,iter=K_Means_predict(image_data_umap,10,10000,rand_seed)
for i in range(0,10):
  classes[i]=np.array(classes[i]).tolist()
  
for i in range(0,10):
  print(len(classes[i]))

print(cluster)

sse,count = sse_k(image_data_umap,cluster,centroids,10)
sse

with open('image_cluster95.txt', 'w') as f:
  for i in cluster:
    f.write(str(i) +"\n")