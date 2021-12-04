# k fold with k = # of rows in dataset

import numpy
import math
import pandas


# load data into a dataframe
dataframe = pandas.read_fwf("large.txt",header=None) 
# dataframe = dataframe.iloc[0:40, : ]

# number of features
num_features = dataframe.iloc[0,1:].size
num_instances = dataframe.iloc[0:,0].size

def cross_validation_accuracy(data, current_set, feature_to_add):
    this_set = current_set
    # this_set.append(feature_to_add)
    
    for x in range(num_features):
        y = x + 1
        if y not in this_set and y != feature_to_add:
            data[y].values[:] = 0
    
    # print(data)

    num_correctly_classified = 0
    for i in range(num_instances):
        #label of curr instance
        label_object_to_classify = data.iloc[i, 0]
        #features of curr instance
        object_to_classify = data.iloc[i, 1:]
        
        nearest_neighbor_distance = math.inf
        nearest_neighbor_location = 0

        for k in range(num_instances):
            if k != i:
                #find euclidian distance to object at k, k cannot be i
                object_to_compare = data.iloc[k,1:]
                summation = 0
                for a in range(object_to_classify.size):
                    b = a+1
                    summation += ((object_to_classify.at[b] - object_to_compare.at[b]) **2)
                distance = math.sqrt(summation)

                if distance < nearest_neighbor_distance:
                    nearest_neighbor_distance = distance
                    nearest_neighbor_location = k
                    nearest_neighbor_label = data.iloc[k,0]
                # print(" ask if " + str(i) + " is nearest neighbor w/ " + str(k))
        
        
        
        print("Object " + str(i)  + " is class " + str(label_object_to_classify) + " and its nearest neighbor is " + str(nearest_neighbor_location) + " which is in class " + str(nearest_neighbor_label))
        if(label_object_to_classify == nearest_neighbor_label): 
            num_correctly_classified += 1
    accuracy = num_correctly_classified / num_instances
    return accuracy


# # test function
print(cross_validation_accuracy(dataframe.copy(), [], 1))
print(dataframe)
# print(cross_validation_accuracy(dataframe.copy(), [], 5))
# # print(dataframe)
# print(cross_validation_accuracy(dataframe.copy(), [], 4))
# # for i in range(num_features):
# #     print(i + 1)









    
