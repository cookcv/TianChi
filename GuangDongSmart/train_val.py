import os
import random
import shutil
from  shutil import copy2

root_path = "guangdong_round1_train2_20180916/è¦´ÃÑù±¾/train/"
files = os.listdir(root_path)
trainDir = root_path + '/train'
valDir = root_path + '/val'
os.mkdir(trainDir)
os.mkdir(valDir)
for filename in files:
    print(filename)
    trainfiles = os.listdir(root_path+filename)
    num_train = len(trainfiles)
    index_list = range(num_train)
    random.shuffle(list(index_list))
    num = 0
    traindir = trainDir+"/"+filename
    os.mkdir(traindir)
    valdir = valDir+"/"+filename
    os.mkdir(valdir)
    file_path = root_path+filename
    for i in index_list:
        fileName = os.path.join(file_path, trainfiles[i])
        if num < num_train*0.9:
            copy2(fileName, traindir)
        else:
            copy2(fileName, valdir)
        num += 1