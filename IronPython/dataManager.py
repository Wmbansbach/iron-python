# dataManager.py
# Author: WmBansbach
# Purpose: Python script containing tools to manipulate dataframes for .csv files

import os
import pandas as pd
import datetime


# list used for index movement
indexList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14,
       15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]


# class being called from .NET file to run script
class dManager:
    def manage(self, date, amount, gas, expDict):
        taxDeducted = int(amount * 0.20)
        managerData = FileSearch()
        nameList, valueList = dictFormatter(expDict)
        dFrame = DataFrameCreator(managerData[1], date, amount,
                                       taxDeducted, gas, nameList, valueList)
        FileManagement(managerData[0], dFrame,
                        managerData[2], managerData[3])
        return 0

    
# Creates individual lists for keys
# and values in a given dictionary
def dictFormatter(expDict):
    keyList = []
    valList = []
    for key in expDict.keys():
        keyList.append(key)
        valList.append(expDict[key])
    return keyList, valList


# Manipulates directory finding if file
# exists, if not, states are set for management func.
def FileSearch():
    # Getting path, moving to Documents
    rootPath = os.path.dirname(__file__)
    rootSplit = rootPath.split("\\")
    if len(rootSplit) < 3:
        rootSplit = rootPath.split("/")
    print(rootSplit)
    newDir = os.path.join(rootSplit[0], "\\" + str(rootSplit[1]))
    print(newDir)
    docDir = os.path.join(newDir, rootSplit[2] + "\\Documents")
    print(docDir)

    # Trying to open file
    try:
        os.chdir(os.path.join(docDir, "RABTAX"))
        rabtax = pd.read_csv('RABTAX2017.csv', index_col=0)
    except FileNotFoundError:
        # Catch Exception, set variables for new file creation
        ct = 0
        counter = indexList[0]
        rabtax = None
        pass
    else:
        # Find leading index to work with,
        # set state variables accordingly
        ct = 1
        counter = rabtax.index.max()
        if counter == 26:
            counter = indexList[0]
            ct = 2
        else:
            INDEX = indexList[0]
            x = 0
            while INDEX != counter:
                INDEX = INC(x)
                x += 1
                continue
            else:
                counter = INC(x)
        print(rabtax)
    return [ct, counter, rabtax, docDir]


def DataFrameCreator(counter, date, rbchk, txded, gas, expName = None, expValue = None):
    # New dictionary is created with newly input data
    key_dic = {'Date': pd.Series([date], index=[counter]),
               'Paycheck': pd.Series([rbchk], index=[counter]),
               'TaxDeducted': pd.Series([txded], index=[counter]),
               'Gas': pd.Series([gas], index=[counter])}
    # If there are any extra expense they
    # will be added to the data from dynamically here
    if expName != None:
        xE_count = 0
        for ind in expName:
            key_dic[ind] = pd.Series([expValue[xE_count]], index=[counter])
            xE_count += 1

    df = pd.DataFrame(key_dic)
    return df


def FileManagement(state, df, rabtax, path):
    # Create new Dir, Make new Dir called RochellesTaxStuff, Save data frame as RABTAX
    if state == 0:
        os.chdir(path)
        os.mkdir('RABTAX')
        os.chdir(os.path.join(path, 'RABTAX'))
        df.to_csv('RABTAX2017.csv')  # df will be the variable for the created dataframe.
        return 1
        pass
    elif state == 1:
        # Updates existing file by appending
        rabtax2 = rabtax.append(df)
        os.chdir(os.path.join(path, 'RABTAX'))
        rabtax2.to_csv('RABTAX2017.csv')
        return 2

    # Create new CSV file with name RABTAX + Year
    if state == 2:
        newDate = datetime.strftime('%Y')
        os.chdir(os.path.join(path, 'RABTAX'))
        df.to_csv('RABTAX' + str(newDate) + '.csv')
        return 3


def INC(x):
    # Increment index within data structure
    ind = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]
    return ind[x+1]

