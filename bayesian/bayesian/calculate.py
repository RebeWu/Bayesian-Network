#-*-coding:utf-8-*-
import random

import numpy as np
import pandas as pd

quary_set = {'0': 0, '2': 1}
#array=[('VisitAsia', 'Tuberculosis'), ('Smoking', 'Cancer'), ('Smoking', 'Bronchitis'), ('Cancer', 'TbOrCa'),('Bronchitis', 'TbOrCa'), ('Bronchitis', 'Dyspnea'), ('TbOrCa', 'XRay')]
array=[('0','1'),('0','3'),('2','1'),('2','6')]
needToQuary=['0', '1', '2', '3', '6']

def cal(quary_set,array,needToQuary):
    np.set_printoptions(threshold=np.inf)
    """
    a = []
    file = open("da.txt", "r")
    list_arr = file.readlines()
    l = len(list_arr)
    for i in list_arr:
        o = i.replace('\n', '')
        o1 = o.replace('\t', ' ')
        o2=o1.split(' ')
        a += o2
    print (a)
    #a.reshape(9,200)
    """

    # 读取文件
    data = pd.read_csv("/home/rebecca/workplace/pgmpy/da.txt", sep='\t', header=None)
    # print (data)
    # data.columns = ['IDnum', 'VisitAsia', 'Tuberculosis', 'Smoking', 'Cancer', 'TbOrCa', 'XRay', 'Bronchitis','Dyspnea']
    data.columns = ['8','0', '1', '2', '3', '4', '5', '6', '7']

    from pgmpy.models import BayesianModel
    from pgmpy.estimators import MaximumLikelihoodEstimator, BayesianEstimator
    """"
    根据边构建网络
    """
    model = BayesianModel(array)
    # Learing CPDs using Maximum Likelihood Estimators
    model.fit(data, estimator=MaximumLikelihoodEstimator)

    for cpd in model.get_cpds():
        print(cpd)
        #    print (cpd.values)
        print(cpd.cardinality)

    """"
    根据概率查询网络
    """
    from pgmpy.inference import VariableElimination
#======================================================================================================
    # quary_set = {'VisitAsia': 0, 'Smoking': 1}
    #layer1 = ['VisitAsia', 'Smoking']
    #layer2 = ['Tuberculosis', 'Cancer', 'Bronchitis']
    #layer3 = ['TbOrCa']
    #layer4 = ['Dyspnea', 'XRay']
    infer = VariableElimination(model)
    #needToQuary = ['VisitAsia', 'Tuberculosis', 'Smoking', 'Cancer', 'TbOrCa', 'XRay', 'Bronchitis', 'Dyspnea']
    # result = infer.query(needToQuary, evidence=quary_set)
    # class DiscreteFactor(BaseFactor):
    #needToQuary = ['0', '1', '2', '3', '6']#=========================================================
    layer1 = ['0', '2']
    layer2 = ['1', '3', '6']
    layer3 = ['4']
    layer4 = ['5', '7']
    # 更新quaryset查询层列表
    def update_layer():
        print(quary_set)
        for i in quary_set:
            for j in layer1:
                if i == j:
                    layer1.remove(j)
            for j in layer2:
                if i == j:
                    layer2.remove(j)
            for j in layer3:
                if i == j:
                    layer3.remove(j)
            for j in layer4:
                if i == j:
                    layer4.remove(j)

    # 更新quary列表
    def updata_quarySet(quary_set):
        for i in result:
            a = []
            b = []
            """
            print (i)
            print(result[i])
            print(result[i].values)
            """
            for j in layer1:
                if i == j:
                    rand = random.uniform(0, 1)
                    print(rand)
                    print(result[i].values)
                    if ((rand < result[i].values)[0]):
                        a.append(0)
                        b.append(i)
                    else:
                        a.append(1)
                        b.append(i)
            for j in layer2:
                if i == j:
                    rand = random.uniform(0, 1)
                    print(rand)
                    print(result[i].values)
                    if ((rand < result[i].values)[0]):
                        a.append(0)
                        b.append(i)
                    else:
                        a.append(1)
                        b.append(i)
                for j in layer3:
                    if i == j:
                        rand = random.uniform(0, 1)
                        print(rand)
                        print(result[i].values)
                        if ((rand < result[i].values)[0]):
                            a.append(0)
                            b.append(i)
                        else:
                            a.append(1)
                            b.append(i)
            for j in layer4:
                if i == j:
                    rand = random.uniform(0, 1)
                    print(rand)
                    print(result[i].values)
                    if ((rand < result[i].values)[0]):
                        a.append(0)
                        b.append(i)
                    else:
                        a.append(1)
                        b.append(i)
        print(a)
        for i in range(len(a)):
            m = b[i]
            quary_set[m] = a[i]
        print(quary_set)
        return quary_set

    # 需要查询的集合
    def update_needToQuary(needToQuary):
        tmp = quary_set.keys()
        for i in tmp:
            print(i)
            for j in needToQuary:
                print(j)
                if (i == j):
                    needToQuary.remove(i)
        return needToQuary
    num=7
    # while len(layer1) or len(layer2) or len(layer3) or len(layer4):
    while num!=0:
        tmp = quary_set.keys()
        for i in tmp:
            print(i)
            for j in needToQuary:
                print(j)
                if (i == j):
                    needToQuary.remove(i)
        result = infer.query(needToQuary, evidence=quary_set)
        print(needToQuary)
        # updata_quarySet
        for i in result:
            a = []
            b = []
            """
            print (i)
            print(result[i])
            print(result[i].values)
            """
            for j in layer1:
                if i == j:
                    rand = random.uniform(0, 1)
                    print(rand)
                    print(result[i].values)
                    if ((rand < result[i].values)[0]):
                        a.append(0)
                        b.append(i)
                    else:
                        a.append(1)
                        b.append(i)
            for j in layer2:
                if i == j:
                    rand = random.uniform(0, 1)
                    print(rand)
                    print(result[i].values)
                    if ((rand < result[i].values)[0]):
                        a.append(0)
                        b.append(i)
                    else:
                        a.append(1)
                        b.append(i)
                for j in layer3:
                    if i == j:
                        rand = random.uniform(0, 1)
                        print(rand)
                        print(result[i].values)
                        if ((rand < result[i].values)[0]):
                            a.append(0)
                            b.append(i)
                        else:
                            a.append(1)
                            b.append(i)
            for j in layer4:
                if i == j:
                    rand = random.uniform(0, 1)
                    print(rand)
                    print(result[i].values)
                    if ((rand < result[i].values)[0]):
                        a.append(0)
                        b.append(i)
                    else:
                        a.append(1)
                        b.append(i)
        print(a)
        for i in range(len(a)):
            m = b[i]
            quary_set[m] = a[i]

        # updatalayer
        print(quary_set)
        for i in quary_set:
            for j in layer1:
                if i == j:
                    layer1.remove(j)
            for j in layer2:
                if i == j:
                    layer2.remove(j)
            for j in layer3:
                if i == j:
                    layer3.remove(j)
            for j in layer4:
                if i == j:
                    layer4.remove(j)
        print(needToQuary)
        #dict = sorted(quary_set.iteritems(), key=lambda d: d[1]['val'], reverse=True)
        value = []#======================================最后他要得值
        option = ['0', '1', '2', '3', '4', '5', '6', '7']
        for i in option:
            op = quary_set.keys()
            if i in op:
                value.append(quary_set.get(i))
            else:
                value.append(2)
        print(value)
        fina=[]
        fina.append(value[0])
        fina.append(value[2])
        fina.append(value[1])
        fina.append(value[3])
        fina.append(value[6])
        fina.append(value[4])
        fina.append(value[5])
        fina.append(value[7])
        print(fina)

        print(str(fina))


        print(quary_set.values())
        print(quary_set)
        print(layer1)
        print(layer2)
        print(layer3)
        print(layer4)
        num-=1
cal(quary_set,array,needToQuary)