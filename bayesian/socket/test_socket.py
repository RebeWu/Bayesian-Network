# -*- coding:utf8 -*-
#-*-coding:utf-8-*-
import random

import numpy as np
import pandas as pd

#quary_set = {'0': 0, '2': 1}
#array=[('VisitAsia', 'Tuberculosis'), ('Smoking', 'Cancer'), ('Smoking', 'Bronchitis'), ('Cancer', 'TbOrCa'),('Bronchitis', 'TbOrCa'), ('Bronchitis', 'Dyspnea'), ('TbOrCa', 'XRay')]
#array=[('0','1'),('0','3'),('2','1'),('2','6')]
#needToQuary=['0', '1', '2', '3', '6']

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
    data = pd.read_csv("da.txt", sep='\t', header=None)
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
        print(quary_set)
        print(layer1)
        print(layer2)
        print(layer3)
        print(layer4)
        num-=1




import threading
import hashlib
import socket
import base64

import bayesian


class websocket_thread(threading.Thread):
    def __init__(self, connection):
        super(websocket_thread, self).__init__()
        self.connection = connection

    def run(self):
        print ('new websocket client joined!')
        reply = 'i got u, from websocket server.'
        length = len(reply)
        while True:
            data = self.connection.recv(1024)
            a=parse_data(data)
            print(a)
            c = a.split(',##')
            c1 = c[0].split(',')
            c2 = c[1].split(',')
            array = []
            print('------------------')
            for i in range(len(c1)):
                x = (c1[i], c2[i])
                array.append(x)
            print(array)
            d = c[2].split(',')
            c3 = []
            print(d)
            for i in d:
                q = list(i)
                for j in q:
                    c3.append(j)
            print(c3)
            dist = {}
            dist['A'] = '0'
            dist['B'] = '1'
            dist['C'] = '2'
            dist['D'] = '3'
            dist['E'] = '4'
            dist['F'] = '5'
            dist['G'] = '6'
            dist['H'] = '7'
            dist['0'] = 0
            dist['1'] = 1
            quary_seting = {}
            print(c3)
            for i in range(len(c3)):
                # print (dist[c3[i]])
                if i % 2 == 0:
                    quary_seting[dist[c3[i]]] = dist[c3[i + 1]]
            needTo = []
            for p in c1:
                needTo.append(p)
            for q in c2:
                needTo.append(q)
            print(needTo)
            l2 = list(set(needTo))
            print(quary_seting)
            print(array)
            print(l2)
            cal(quary_seting, array, l2)
            print (quary_seting)

            value123 = []  # ======================================最后他要得值
            option = ['0', '1', '2', '3', '4', '5', '6', '7']
            for i in option:
                op = quary_seting.keys()
                if i in op:
                    value123.append(quary_seting.get(i))
                else:
                    value123.append(2)
            print('value123',value123)
            """
            fina = {}
            fina['0']=(value123[0])
            fina['1']=(value123[2])
            fina['2']=(value123[1])
            fina['3']=(value123[3])
            fina['4']=(value123[6])
            fina['5']=(value123[4])
            fina['6']=(value123[5])
            fina['7']=(value123[7])
            print(fina)

            print('str(fina)',str(fina))
            reply=str(fina)
            length=len(reply)
            """
            fina = []
            fina.append(value123[0])
            fina.append(value123[2])
            fina.append(value123[1])
            fina.append(value123[3])
            fina.append(value123[6])
            fina.append(value123[4])
            fina.append(value123[5])
            fina\
                .append(value123[7])
            print(fina)

            print('str(fina)',str(fina))
            reply=str(fina)
            length=len(reply)

            self.connection.send(b'%c%c%s' % (0x81, length, bytes(reply,encoding="utf-8")))


def parse_data(msg):
    v = msg[1] & 0x7f
    if v == 0x7e:
        p = 4
    elif v == 0x7f:
        p = 10
    else:
        p = 2
    mask = msg[p:p + 4]
    data = msg[p + 4:]

    return ''.join([chr(v ^ mask[k % 4]) for k, v in enumerate(data)])


def parse_headers(msg):
    headers = {}
    header, data = bytes.decode(msg).split('\r\n\r\n', 1)
    for line in header.split('\r\n')[1:]:
        key, value = line.split(': ', 1)
        headers[key] = value
    headers['data'] = data
    return headers


def generate_token(msg):
    key = msg + '258EAFA5-E914-47DA-95CA-C5AB0DC85B11'
    ser_key = hashlib.sha1(key.encode('utf8')).digest()
    return base64.b64encode(ser_key)


if __name__ == '__main__':
    #socket(family,type[,protocal]) 使用给定的地址族、套接字类型、协议编号（默认为0）来创建套接字。
    '''
    socket.AF_UNIX  只能够用于单一的Unix系统进程间通信
    socket.AF_INET  服务器之间网络通信
    socket.AF_INET6 IPv6
    socket.SOCK_STREAM  流式socket , for TCP
    socket.SOCK_DGRAM   数据报式socket , for UDP
    创建TCP Socket：s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    创建UDP Socket：s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    '''

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #s.setsockopt(level,optname,value) 设置给定套接字选项的值。
    #打开或关闭地址复用功能。当option_value不等于0时，打开，否则，关闭。它实际所做的工作是置sock->sk->sk_reuse为1或0。
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(('127.0.0.1', 9000))
    sock.listen(5)
    #首先，我们创建了一个套接字，然后让套接字开始监听接口，并且最多只能监听5个请求
    while True:
        connection, address = sock.accept()
	#接受监听到的连接请求，
        print (address)
        try:
            data = connection.recv(1024)
            headers = parse_headers(data)
            token = generate_token(headers['Sec-WebSocket-Key'])
            connection.send(b'\
HTTP/1.1 101 WebSocket Protocol Hybi-10\r\n\
Upgrade: WebSocket\r\n\
Connection: Upgrade\r\n\
Sec-WebSocket-Accept: %s\r\n\r\n' % bytes(token))
            thread = websocket_thread(connection)
            thread.start()
        except socket.timeout:
            print ('websocket connection timeout')




