# -*- coding:utf8 -*-

import os
head = 0
allFileNum = 0
def printPath(path):
    global head
    arry = []
    head = 0
    name = path + '.csv'
    result=open(name,'w')
    files = os.listdir(path)
    for f in files:
        ftmp=f.split('.')
        print ftmp[0]
        
    for f in files:
        proline(f, path, arry)
    for x in arry:
        print x
    result.writelines(arry)

def proline(filename, path, arry):
    global head
    full_path = path + '/' + filename
    file_object = open(full_path, 'r')
    list_of_all_the_lines = file_object.readlines()
    if head==0:
        headline = ''
        headline = 'File Name' + ',' + list_of_all_the_lines[0]
        arry.append(headline)
        head = 1
    #print list_of_all_the_lines[2]
    tmpline = ''
    tmpline = filename + ',' + list_of_all_the_lines[2]
    arry.append(tmpline)
    
if __name__ == '__main__':
    printPath('BCB-S')
    printPath('BO-S')
    printPath('CBC-S')
    printPath('CO-S')
    printPath('CX-S')
    printPath('NC-S')
    print 'total =', allFileNum
