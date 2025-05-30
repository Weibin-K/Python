import pytest

import re

import pandas as pd

from pandas import DataFrame

import openpyxl

from openpyxl import load_workbook

from Subsave import Subsave

import time

import motor_turn

from motor import Motor

from DMM import DMMController

from Relay import RelayController

from PSU import PSUController

from time import sleep

from colorama import Fore, Style

 

RL1, RL2, RL3, RL4, RL5, RL6, RL7 = 1, 2, 3, 4, 5, 6, 7

DMM, relay = None, None

 

def INIT():

    global relay, DMM, PSU

 

    PSU = PSUController()

    DMM = DMMController()

    relay = RelayController()

 

def DISCONNECT_DEVICES():

    PSU.CLOSE_DEVICE()

    DMM.CLOSE_DEVICE()

    relay.CLOSE_DEVICE()

 

def SEQUENCE_CQ():

    relay.OFF_RELAY(RL1)

 

def SEQUENCE_PNP_Q1():

    relay.ON_RELAY(RL1)

    relay.OFF_RELAY(RL2)

 

def SEQUENCE_NPN_Q1():

    relay.ON_RELAY(RL1)

    relay.ON_RELAY(RL2)

 

def SEQUENCE_PNP_Q2():

    relay.OFF_RELAY(RL3)

    relay.OFF_RELAY(RL4)

 

def SEQUENCE_NPN_Q2():

    relay.OFF_RELAY(RL3)

    relay.ON_RELAY(RL4)

 

def SEQUENCE_QAC():

    relay.ON_RELAY(RL3)

    relay.OFF_RELAY(RL5)

 

def SEQUENCE_QAV():

    relay.ON_RELAY(RL3)

    relay.ON_RELAY(RL5)

 

def ACTIVATE_PSU():

    relay.ON_RELAY(RL6)

 

def DEACTIVATE_PSU():

    relay.OFF_RELAY(RL6)

 

def SEQUENCE_IN_GND():

    relay.OFF_RELAY(RL7)

 

def SEQUENCE_IN_LOAD():

    relay.ON_RELAY(RL7)

 

def test_START_UP():

    INIT()

 

    if relay.DEVICE_STATUS() and DMM.DEVICE_STATUS() and PSU.DEVICE_STATUS():

        print(Fore.GREEN + "MAIN: INITIALIZATION SUCCESS" + Style.RESET_ALL)

 

        PSU.SET_VOLTAGE_CURRENT(24, 1)

        sleep(0.1)

        PSU.ON_OUTPUT() # Enable PSU output

        sleep(2)

        ACTIVATE_PSU() # Supply to DUT

        sleep(80)

 

    else:

        DISCONNECT_DEVICES()

        print(Fore.RED + "MAIN: INITIALIZATION FAIL" + Style.RESET_ALL)

 

 

 

print("===============================Save path location for result ==================================================")

 

path = r'C:\work\VV\gbc08-test-repo\DX80\fullrun029.xlsx'                       #Specify the save path location

 

print("================================================================================================================")

 

Sdf = 0

Sdf2 = 0

sname = ['Testcase_name', 'Index' , 'SubIndex', 'Expected result', 'Output result', 'Outcome']

sname2 = ['Testcase_name', 'Index', 'ERFirst', 'ORFirst','outcomeFirst','ERSecond','ORSecond','outcomeSecond','ERThird','ORThird','outcomeThird','ERFourth','ORFourth','outcomeFourth']

Sdf: DataFrame = pd.DataFrame(columns=sname, index=range(0, 242))

Sdf2: DataFrame = pd.DataFrame(columns=sname2, index=range(0,242))

 

print("================================================================================================================")

 

print("=======================Start with IO link specific=============================================")

@pytest.mark.test_id(15497)   #2

def test_Vendor_Name(iolink_master):

 

    print(Fore.GREEN + "RUNNING TEST" + Style.RESET_ALL)

    systemcommand = 2

    resetprod_name = iolink_master.write(130, systemcommand)

 

    num1 = 0                                     # which row to save the data

    Name1 = 'Vendor Name'                        # Name of the testcase

    Index1 =  16                                 # IO index

    SubIndex1 = 0

    ER1 = "SICK AG"                              # Expected return result

 

    prod_name = iolink_master.read(Index1)       #for the IO link index

    # prod_name = iolink_master.read("Vendor Name")

    Rname1 = prod_name.rstrip(" ")                #strip it

 

    if ER1 == Rname1:

        result1 = "Passed"

    else:

        result1 = "Failed"

 

    Subsave().savetoexcel1(path, num1, Name1, Index1, SubIndex1, ER1, Rname1, result1 , Sdf)  # save all the data in excel

    assert Rname1 == ER1

 

@pytest.mark.test_id(15562)   #3

def test_Product_Name(iolink_master):

    systemcommand = 2

    resetprod_name = iolink_master.write(130, systemcommand)

 

    num1 = 1                                     # which row to save the data

    Name1 = 'Product Name'                       # Name of the testcase

    Index1 = 18                                  # IO index

    SubIndex1 = 0

    ER1 = "DT80-IOLINK"                                 # Expected return result

 

    prod_name1 = iolink_master.read(Index1)

    # prod_name = iolink_master.read("Product Name")

    Rname1 = prod_name1.rstrip(" ")

 

    if ER1 == Rname1:

        result1 = "Passed"

    else:

        result1 = "Failed"

 

    Subsave().savetoexcel1(path, num1, Name1, Index1,SubIndex1, ER1, Rname1, result1, Sdf)  # save all the data in excel

    assert Rname1 == ER1

 

@pytest.mark.test_id(15563)   #4

def test_Product_ID(iolink_master):

    systemcommand = 2

    resetprod_name = iolink_master.write(130, systemcommand)

 

    num1 = 2

    Name1 = 'Product ID'

    Index1 = 19

    SubIndex1 = 0

    ER1 = '1118113'

 

    prod_name1 = iolink_master.read(Index1)

    Rname1 = prod_name1.rstrip(" ")

 

    if ER1 == Rname1:

        result1 = "Passed"

    else:

        result1 = "Failed"

 

    Subsave().savetoexcel1(path, num1, Name1, Index1,SubIndex1, ER1, Rname1, result1, Sdf)  # save all the data in excel

    assert Rname1 == ER1

 

@pytest.mark.test_id(15564)  #5

def test_Product_Text(iolink_master):

    systemcommand = 2

    resetprod_name = iolink_master.write(130, systemcommand)

 

    num1 = 3

    Name1 = 'Product Text'

    Index1 = 20

    SubIndex1 = 0

    ER1 = 'Distance Sensor'

 

    prod_name1 = iolink_master.read(Index1)

    # prod_name = iolink_master.read("Product Name")

    Rname1 = prod_name1.rstrip(" ")

 

    if ER1 == Rname1:

        result1 = "Passed"

    else:

        result1 = "Failed"

 

    Subsave().savetoexcel1(path, num1, Name1, Index1,SubIndex1, ER1, Rname1,result1, Sdf)  # save all the data in excel

    assert Rname1 == ER1

 

@pytest.mark.test_id(15565)  #6

def test_Serial_Number(iolink_master):

    systemcommand = 2

    resetprod_name = iolink_master.write(130, systemcommand)

 

    num1 = 4

    Name1 = 'Serial Number'

    Index1 = 21

    SubIndex1 = 0

    ER1 ='12345678'

 

    prod_name1 = iolink_master.read(Index1)

    # prod_name = iolink_master.read("Product Name")

    Rname1 = prod_name1.rstrip(" ")

 

    if ER1 == Rname1:

        result1 = "Passed"

    else:

        result1 = "Failed"

    Subsave().savetoexcel1(path, num1, Name1, Index1,SubIndex1, ER1, Rname1,result1,Sdf)# save all the data in excel

    assert Rname1 == ER1

 

@pytest.mark.test_id(15566)   #7

def test_Vendor_Text(iolink_master):

    systemcommand = 2

    resetprod_name = iolink_master.write(130, systemcommand)

 

    num1 = 5

    Name1 = 'Vendor Text'

    Index1 = 17

    SubIndex1 = 0

    ER1 = 'www.sick.com'

 

    prod_name1 = iolink_master.read(Index1)

    # prod_name = iolink_master.read("Product Name")

    Rname1 = prod_name1.rstrip(" ")

 

    if ER1 == Rname1:

        result1 = "Passed"

    else:

        result1 = "Failed"

 

    Subsave().savetoexcel1(path, num1, Name1, Index1,SubIndex1, ER1, Rname1, result1, Sdf)  # save all the data in excel

    assert Rname1 == ER1

 

@pytest.mark.test_id(15567)   #8

def test_Hardware_Version(iolink_master):

 

    systemcommand = 2

    resetprod_name = iolink_master.write(130, systemcommand)

 

    num1 = 6

    Name1 = 'Hardware Version'

    Index1 = 22

    SubIndex1 = 0

    ER1 = '0000'

 

    prod_name1 = iolink_master.read(Index1)

    # prod_name = iolink_master.read("Product Name")

    Rname1 = prod_name1.rstrip(" ")

 

    if ER1 == Rname1:

        result1 = "Passed"

    else:

        result1 = "Failed"

 

    Subsave().savetoexcel1(path, num1, Name1, Index1,SubIndex1, ER1, Rname1, result1, Sdf)  # save all the data in excel

    assert Rname1 == ER1

 

@pytest.mark.test_id(15568)  #9

def test_Software_version(iolink_master):

 

    systemcommand = 2

    resetprod_name = iolink_master.write(130, systemcommand)

 

    num1 = 7

    Name1 = 'Firmware version'

    Index1 = 23

    SubIndex1 = 0

    ER1 = '0000-0000-0000-0000'

 

    prod_name1 = iolink_master.read(Index1)

    # prod_name = iolink_master.read("Product Name")

    Rname1 = prod_name1.rstrip(" ")

 

    if ER1 == Rname1:

        result1 = "Passed"

    else:

        result1 = "Failed"

 

    Subsave().savetoexcel1(path, num1, Name1, Index1, SubIndex1, ER1, Rname1, result1,Sdf)  # save all the data in excel

    assert Rname1 == ER1

 

@pytest.mark.test_id(15570)   #10

def test_Application_Specific_Tag(iolink_master):

 

    systemcommand = 2

    resetprod_name = iolink_master.write(130, systemcommand)

 

    num1 = 8

    Name1 = 'Application Specific Tag Read'

    Index1 = 24

    SubIndex1 = 0

    ER1 = '***'

 

    num2 = 9

    Name2 = 'Application Specific Tag Write'

    Index2 = 24

    SubIndex2 = 0

    ER2 = '***'

 

    prod_name1 = iolink_master.read(Index1)

    prod_name2 = iolink_master.write('***', Index2)

    prod_name2 = iolink_master.read(Index2)

    Rname1 = prod_name1.rstrip(" ")

 

    if ER1 == Rname1:

        result1 = "Passed"

    else:

        result1 = "Failed"

 

    if ER2 == prod_name2:

        result2 = "Passed"

    else:

        result2 = "Failed"

 

    Subsave().savetoexcel1(path, num1, Name1, Index1, SubIndex1, ER1, Rname1, result1,Sdf)  # save all the data in excel

    Subsave().savetoexcel2(path, num2, Name2, Index2, SubIndex2, str(ER2), str(prod_name2), result2, Sdf)

    assert Rname1 == ER1

    assert prod_name1 == ER2

 

# @pytest.mark.test_id(15570)  #11

def test_Function_Tag(iolink_master):

 

    systemcommand = 2

    resetprod_name = iolink_master.write(130, systemcommand)

 

    num1 = 10

    Name1 = 'Function Tag Read'

    Index1 = 25

    SubIndex1 = 0

    ER1 = '***'

 

    num2 = 11

    Name2 = 'Function Tag Write'

    Index2 = 24

    SubIndex2 = 0

    ER2 = '***'

 

    prod_name1 = iolink_master.read(Index1)

    prod_name2 = iolink_master.write('***', Index2)

    prod_name2 = iolink_master.read(Index2)

    Rname1 = prod_name1.rstrip(" ")

 

    if ER1 == Rname1:

        result1 = "Passed"

    else:

        result1 = "Failed"

 

    if ER2 == prod_name2:

        result2 = "Passed"

    else:

        result2 = "Failed"

 

    Subsave().savetoexcel1(path, num1, Name1, Index1, SubIndex1, ER1, Rname1, result1,Sdf)  # save all the data in excel

    Subsave().savetoexcel2(path, num2, Name2, Index2, SubIndex2, str(ER2), str(prod_name2), result2, Sdf)

    assert Rname1 == ER1

    assert prod_name2 == ER2

 

# @pytest.mark.test_id(15570)  #12

def test_Location_Tag(iolink_master):

 

    systemcommand = 2

    resetprod_name = iolink_master.write(130, systemcommand)

 

    num1 = 12

    Name1 = 'Location Tag Read'

    Index1 = 26

    SubIndex1 = 0

    ER1 = '***'

 

    num2 = 13

    Name2 = 'Location Tag Write'

    Index2 = 26

    SubIndex2 = 0

    ER2 = '***'

 

    prod_name1 = iolink_master.read(Index1)

    prod_name2 = iolink_master.write('***', Index2)

    prod_name2 = iolink_master.read(Index2)

    # prod_name = iolink_master.read("Product Name")

    Rname1 = prod_name1.rstrip(" ")

 

    if ER1 == Rname1:

        result1 = "Passed"

    else:

        result1 = "Failed"

 

    if ER2 == prod_name2:

        result2 = "Passed"

    else:

        result2 = "Failed"

 

    Subsave().savetoexcel1(path, num1, Name1, Index1, SubIndex1, ER1, Rname1, result1,Sdf)  # save all the data in excel

    Subsave().savetoexcel2(path, num2, Name2, Index2, SubIndex2, str(ER2), str(prod_name2), result2, Sdf)

    assert Rname1 == ER1

    assert prod_name2 == ER2

 

@pytest.mark.test_id(17898)   #13

def test_Q1_Save_Restore(iolink_master):

 

    systemcommand = 2

    resetprod_name = iolink_master.write(130, systemcommand)

 

    num1 = 14                                     # which row to save the data

    Name1 = 'Q1 Save and Restore'                 # Name of the testcase

    Index1 =  2                                   # IO index

    SubIndex1 = 0

    SPIndex = 62

    SP1SubIndex = 1

    SP2SubIndex = 2

    ER1 = { 1 : 1500, 2 : 4990}

 

    SP1prod_name = iolink_master.write(1500, SPIndex, SP1SubIndex)

    SP2prod_name = iolink_master.write(4990, SPIndex, SP2SubIndex)

 

    Saveprod_name = iolink_master.write(192, Index1)         #save

    time.sleep(1)

 

    SP1prod_name = iolink_master.write(390, SPIndex, SP1SubIndex)

    SP2prod_name = iolink_master.write(4976, SPIndex, SP2SubIndex)

 

    Restoreprod_name = iolink_master.write(193, Index1)     #restore

    time.sleep(1)

 

    prod_name1 = iolink_master.read(SPIndex)

 

    print(prod_name1 )

 

    if ER1 == prod_name1:

        result1 = "Passed"

    else:

        result1 = "Failed"

    Subsave().savetoexcel1(path, num1, Name1, Index1, SubIndex1, str(ER1), str(prod_name1), result1, Sdf)

    assert prod_name1 == ER1

 

time.sleep(3)

 

# @pytest.mark.test_id()    #14

def test_Process_Data(iolink_master):

    systemcommand = 2

    resetprod_name = iolink_master.write(130, systemcommand)

 

    num1 = 15                               # which row to save the data

    Name1 = 'Process Data Distance'         # Name of the testcase

    Index1 = 40                             # IO index

    SubIndex1 = 0

    ER1 = {'3360<DIST<3390'}

 

    num2 = 16

    Name2 = 'Process Data 2'

    Index2 = 40

    SubIndex2 = 0

    ER2 = (2, 0)

 

    num4 = 17

    Name4 = 'Process Data Null'

    ER4 = (3, False)

 

    num5 = 18

    Name5 = 'Process Data Scale'

    ER5 = (4, False)

 

    motor_turn.Teach_Turn(num1=33)

    dict1 = iolink_master.read(Index1)   #Dictionary1

    dict2 = iolink_master.read(Index2)   #Dictionary2

    dict1 = list(dict1.items())          #convert the dictionary into array/list

    prod_name1 = dict1[0]                # extract the required data (distance value)

    prod_name1 = prod_name1[1]           # output = (1, distance value) , extract only the distance value from the list so that

                                              # so that i can do create a range of distance and make comparision

    dict2 = list(dict2.items())          # convert the dictionary into array/list

    prod_name2 = dict2[1]                # extract the second data

    prod_name4 = dict2[2]                # extract the Null data

    prod_name5 = dict2[3]                # extract the Scale data

    time.sleep(3)

 

    motor_turn.finalposition()

 

    if prod_name1 > 3360 and prod_name1 < 3390:

        result1 = "Passed"

    else:

        result1 = "Failed"

 

    if ER2 == prod_name2:

        result2 = "Passed"

    else:

        result2 = "Failed"

 

    if ER4 == prod_name4:

        result4 = "Passed"

    else:

        result4 = "Failed"

 

    if ER5 == prod_name5:

        result5 = "Passed"

    else:

        result5 = "Failed"

    Subsave().savetoexcel1(path, num1, Name1, Index1, SubIndex1, str(ER1), str(prod_name1), result1, Sdf)

    Subsave().savetoexcel1(path, num2, Name2, Index2, SubIndex2, str(ER2), str(prod_name2), result2, Sdf)

    Subsave().savetoexcel1(path, num4, Name4, Index2, SubIndex2, str(ER4), str(prod_name4), result4, Sdf)

    Subsave().savetoexcel1(path, num5, Name5, Index2, SubIndex2, str(ER5), str(prod_name5), result5, Sdf)

    assert prod_name1 > 3360 and prod_name1 < 3390

    assert prod_name2 == ER2

    assert prod_name4 == ER4

    assert prod_name5 == ER5

 

print("=======================SICK Device Specific =============================================")

print("=======================Continue with Q1 swtiching mode =============================================")

@pytest.mark.test_id(17835)   #15

def test_Q1_WindowMode_Hysteresis_Active_High(iolink_master):

 

    systemcommand = 2

    resetprod_name = iolink_master.write(130, systemcommand)

    time.sleep(2)

 

    num1 = 19                                        #row in excel

    Name1 = 'Q1 Window Mode Hysteresis Active High'  # test case name

    Index1 = 61                                      # IO link index

    SubIndex1 = 0

    num3 = 0

    ER1 = {1: 0, 2: 2, 3: 130}                       #Expected result for test harness

    ERFirst = 'Q1: 23, Q2: 0'                        #Expected result for Led light status

    ERSecond = 'Q1: 0, Q2: 0'

    ERThird =  'Q1: 23, Q2: 0'

    ERFourth =  'Q1: 0, Q2: 0'

 

 

    SPIndex = 60                                    #IO Link for Q1 SP

    SP1SubIndex = 1

    SP2SubIndex = 2

 

    LogicIndex = 1

    HystSubIndex = 3

    FuncModeIndex = 2

 

    SP1prod_name = iolink_master.write(240, SPIndex, SP1SubIndex)

    SP2prod_name = iolink_master.write(340, SPIndex, SP2SubIndex)

    # Funprod_name = iolink_master.write(2, Index1, FuncModeIndex)

    # Logicprod_name = iolink_master.write(0, Index1, LogicIndex)

    Hystprod_name = iolink_master.write(130, Index1, HystSubIndex)       #set hysteresis

    prod_name1 = iolink_master.read(Index1)

 

    time.sleep(0.6)

    Saveprod_name = iolink_master.write(192, systemcommand)  # save

    time.sleep(1)

 

    DEACTIVATE_PSU()

    sleep(3)

    ACTIVATE_PSU()

    sleep(3)

    digitalnum1, digitalnum2, digitalnum3, digitalnum4 = motor_turn.Q1PNP(num1=38, num2=56, num3=30, num4=0)  # set angles for motor to turn

    sleep(5)

 

    if ER1 == prod_name1:      # for excel record so i dont need to compare one by one

        result1 = 'Passed'

    else:

        result1 = 'Failed'

 

    if  ERFirst == digitalnum1:

        outcomeFirst = "Passed"

    else:

        outcomeFirst = "Failed"

 

    if  ERSecond == digitalnum2:

        outcomeSecond = "Passed"

    else:

        outcomeSecond = "Failed"

 

    if  ERThird == digitalnum3:

        outcomeThird = "Passed"

    else:

        outcomeThird = "Failed"

 

    if  ERFourth == digitalnum4:

        outcomeFourth = "Passed"

    else:

        outcomeFourth = "Failed"

 

    Subsave().savetoexcel1(path, num1, Name1, Index1, SubIndex1, str(ER1), str(prod_name1), result1,Sdf)  # save all the data in excel

    Subsave().savetoexcelQs(path,num3, Name1, Index1, ERFirst, digitalnum1, outcomeFirst, ERSecond, digitalnum2, outcomeSecond,

                  ERThird,digitalnum3, outcomeThird, ERFourth, digitalnum4, outcomeFourth, Sdf2)        # save led light voltage result

 

    SEQUENCE_CQ()

 

    assert prod_name1 == ER1

    assert digitalnum1 == 'Q1: 23, Q2: 0'

    assert digitalnum2 == 'Q1: 0, Q2: 0'

    assert digitalnum3 == 'Q1: 23, Q2: 0'

    assert digitalnum4 == 'Q1: 0, Q2: 0'

time.sleep(3)

 

@pytest.mark.test_id(17828)  #16

def test_Q1_WindowMode_Hysteresis_Active_Low(iolink_master):

 

    systemcommand = 2

    resetprod_name = iolink_master.write(130, systemcommand)

 

    num1 = 20                                      #which row to save in excel

    Name1 = 'Q1 Window Mode Hysteresis Active Low' #test case name

    Index1 = 61                                    #io link index that will print on excel

    SubIndex1 = 0

    ER1 = {1:1, 2:2, 3:130}                        #expected result that will print on excel

    num3 = 1                                       #which row to save in excel and different sheet

    ERFirst = 'Q1: 0, Q2: 0'                       # expected result to save in excel

    ERSecond = 'Q1: 23, Q2: 0'

    ERThird = 'Q1: 0, Q2: 0'

    ERFourth ='Q1: 23, Q2: 0'

 

    SPIndex = 60

    SP1SubIndex = 1

    SP2SubIndex = 2

 

    HystSubIndex = 3

    LogicIndex = 1

 

    SP1prod_name = iolink_master.write(240, SPIndex, SP1SubIndex)   #set distance

    SP2prod_name = iolink_master.write(340, SPIndex, SP2SubIndex)

    Logicprod_name = iolink_master.write(1, Index1, LogicIndex)     #set Active low

    Hystprod_name = iolink_master.write(130, Index1, HystSubIndex)  #set hysteresis value

    prod_name1 = iolink_master.read(Index1)                         # receive output

 

    time.sleep(0.6)

    Saveprod_name = iolink_master.write(192, systemcommand)         #save information

    time.sleep(1)

 

    DEACTIVATE_PSU()                                               #disconnect the device

    sleep(3)

    ACTIVATE_PSU()                                                 #connect to relay set up

    sleep(3)

    digitalnum1, digitalnum2, digitalnum3, digitalnum4 = motor_turn.Q1PNP(num1=38, num2=56, num3=30, num4=0)  #set angle for motor to turn

    sleep(5)

 

    if ER1 == prod_name1:

        result1 = 'Passed'

    else:

        result1 = 'Failed'

 

    if  ERFirst == digitalnum1:

        outcomeFirst = "Passed"

    else:

        outcomeFirst = "Failed"

 

    if  ERSecond == digitalnum2:

        outcomeSecond = "Passed"

    else:

        outcomeSecond = "Failed"

 

    if  ERThird == digitalnum3:

        outcomeThird = "Passed"

    else:

        outcomeThird = "Failed"

 

    if  ERFourth == digitalnum4:

        outcomeFourth = "Passed"

    else:

        outcomeFourth = "Failed"

 

    Subsave().savetoexcel1(path, num1, Name1, Index1, SubIndex1, str(ER1), str(prod_name1), result1, Sdf)  # save result in excel

    Subsave().savetoexcelQs(path, num3, Name1, Index1, ERFirst, digitalnum1, outcomeFirst, ERSecond, digitalnum2,

                            outcomeSecond,

                            ERThird, digitalnum3, outcomeThird, ERFourth, digitalnum4, outcomeFourth, Sdf2)  #save led voltage result in excel

    SEQUENCE_CQ()                      #re-connect back to device

 

    assert prod_name1 == ER1           # to do comparision ( actual output result compare with expected result)

    assert digitalnum1 == 'Q1: 0, Q2: 0'

    assert digitalnum2 == 'Q1: 23, Q2: 0'

    assert digitalnum3 == 'Q1: 0, Q2: 0'

   assert digitalnum4 == 'Q1: 23, Q2: 0'

time.sleep(3)

 

@pytest.mark.test_id(17840) #17

def test_Q1_OffsetMode_Hysteresis_Active_Low(iolink_master):

 

    systemcommand = 2

    resetprod_name = iolink_master.write(130, systemcommand)

 

    num1 = 21

    Name1 = 'Q1 OffSet Hysteresis Active Low'

    Index1 = 61

    SubIndex1 = 0

    ER1 = {1: 1, 2: 128, 3: 110}

    num3 = 2

    ERFirst = 'Q1: 23, Q2: 0'

    ERSecond ='Q1: 0, Q2: 0'

    ERThird = 'Q1: 23, Q2: 0'

    ERFourth ='Q1: 0, Q2: 0'

 

    SP1Index = 60

    SP1SubIndex = 1

 

    LogicIndex = 1

    FuncModeIndex = 2

    HystSubIndex = 3

 

    OffsetIndex = 4371

    # Q2outputswitching = 121

    #

    # q2switching = iolink_master.write(0, Q2outputswitching)  # Q2 Deactivated

    # time.sleep(1)

    # Saveprod_name = iolink_master.write(192, systemcommand)  # save

    # time.sleep(2)

 

    FuncModeprod_name = iolink_master.write(128, Index1, FuncModeIndex)  # change to offset mode

    Logicprod_name = iolink_master.write(1, Index1, LogicIndex)  # set logic to active low

    SP1prod_name = iolink_master.write(300, SP1Index, SP1SubIndex)  # set value for SP1

    OffSetprod_name = iolink_master.write(30, OffsetIndex)  # set value for offset

    Hystprod_name = iolink_master.write(110, Index1, HystSubIndex)  # set hysteresis

    prod_name1 = iolink_master.read(Index1)

 

    time.sleep(0.6)

    Saveprod_name = iolink_master.write(192, systemcommand)  # save

    time.sleep(1)

 

    DEACTIVATE_PSU()

    sleep(3)

    ACTIVATE_PSU()

    sleep(3)

    digitalnum1, digitalnum2, digitalnum3, digitalnum4 = motor_turn.Q1PNP(num1=30, num2=56, num3=26, num4=0)

    sleep(5)

 

    if ER1 == prod_name1:

        result1 = 'Passed'

    else:

        result1 = 'Failed'

 

    if ERFirst == digitalnum1:

        outcomeFirst = "Passed"

    else:

        outcomeFirst = "Failed"

 

    if  ERSecond == digitalnum2:

        outcomeSecond = "Passed"

    else:

        outcomeSecond = "Failed"

 

    if  ERThird == digitalnum3:

        outcomeThird = "Passed"

    else:

        outcomeThird = "Failed"

 

    if  ERFourth == digitalnum4:

        outcomeFourth = "Passed"

    else:

        outcomeFourth = "Failed"

 

    Subsave().savetoexcel1(path, num1, Name1, Index1, SubIndex1, str(ER1), str(prod_name1), result1,Sdf)  # save all the data in excel

    Subsave().savetoexcelQs(path,num3, Name1, Index1, ERFirst, digitalnum1, outcomeFirst, ERSecond, digitalnum2, outcomeSecond,

                  ERThird,digitalnum3, outcomeThird, ERFourth, digitalnum4, outcomeFourth, Sdf2)

 

    SEQUENCE_CQ()

 

    assert prod_name1 == ER1

    assert digitalnum1 == 'Q1: 23, Q2: 0'

    assert digitalnum2 == 'Q1: 0, Q2: 0'

    assert digitalnum3 == 'Q1: 23, Q2: 0'

    assert digitalnum4 == 'Q1: 0, Q2: 0'

time.sleep(3)

 

@pytest.mark.test_id(17839) #18

def test_Q1_OffsetMode_Hysteresis_Active_High(iolink_master):

 

    systemcommand = 2

    resetprod_name = iolink_master.write(130, systemcommand)

 

    num1 = 22

    Name1 = 'Q1 OffSet Hysteresis Active High'

    Index1 = 61

    SubIndex1 = 0

    ER1 = {1: 0, 2: 128, 3: 110}

    num3 = 3

    ERFirst = 'Q1: 0, Q2: 0'

    ERSecond ='Q1: 23, Q2: 0'

    ERThird = 'Q1: 0, Q2: 0'

    ERFourth ='Q1: 23, Q2: 0'

 

    SP1Index = 60

    SP1SubIndex = 1

 

    LogicIndex = 1

    FuncModeIndex = 2

    HystSubIndex = 3

 

    OffsetIndex = 4371

 

    FuncModeprod_name = iolink_master.write(128, Index1, FuncModeIndex)  # change to offset mode

    # Logicprod_name = iolink_master.write(1, Index1, LogicIndex)  # set logic to active low

    SP1prod_name = iolink_master.write(300, SP1Index, SP1SubIndex)  # set value for SP1

    OffSetprod_name = iolink_master.write(30, OffsetIndex)  # set value for offset

    Hystprod_name = iolink_master.write(110, Index1, HystSubIndex)  # set hysteresis

    prod_name1 = iolink_master.read(Index1)

 

    time.sleep(0.6)

    Saveprod_name = iolink_master.write(192, systemcommand)  # save

    time.sleep(1)

 

    DEACTIVATE_PSU()

    sleep(3)

    ACTIVATE_PSU()

    sleep(3)

    digitalnum1, digitalnum2, digitalnum3, digitalnum4 = motor_turn.Q1PNP(num1=30, num2=55, num3=26, num4=0)

    sleep(5)

 

    if ER1 == prod_name1:

        result1 = 'Passed'

    else:

        result1 = 'Failed'

 

    if ERFirst == digitalnum1:

        outcomeFirst = "Passed"

    else:

        outcomeFirst = "Failed"

 

    if  ERSecond == digitalnum2:

        outcomeSecond = "Passed"

    else:

        outcomeSecond = "Failed"

 

    if  ERThird == digitalnum3:

        outcomeThird = "Passed"

    else:

        outcomeThird = "Failed"

 

    if  ERFourth == digitalnum4:

        outcomeFourth = "Passed"

    else:

        outcomeFourth = "Failed"

 

    Subsave().savetoexcel1(path, num1, Name1, Index1, SubIndex1, str(ER1), str(prod_name1), result1,Sdf)  # save all the data in excel

    Subsave().savetoexcelQs(path,num3, Name1, Index1, ERFirst, digitalnum1, outcomeFirst, ERSecond, digitalnum2, outcomeSecond,

                  ERThird,digitalnum3, outcomeThird, ERFourth, digitalnum4, outcomeFourth, Sdf2)

 

    SEQUENCE_CQ()

 

    assert prod_name1 == ER1

    assert digitalnum1 == 'Q1: 0, Q2: 0'

    assert digitalnum2 == 'Q1: 23, Q2: 0'

    assert digitalnum3 == 'Q1: 0, Q2: 0'

    assert digitalnum4 == 'Q1: 23, Q2: 0'

time.sleep(3)

 

@pytest.mark.test_id(17850)  #19

def test_Q1_Single_Hysteresis_Active_Low(iolink_master):

 

    systemcommand = 2

    resetprod_name = iolink_master.write(130, systemcommand)

 

    num1 = 23

    Name1 = 'Q1 Single Hysteresis Active Low'

    Index1 = 61

    SubIndex1 = 0

    ER1 = {1: 1, 2: 1, 3: 20}

    num3 = 4

    ERFirst = 'Q1: 0, Q2: 0'

    ERSecond = 'Q1: 23, Q2: 0'

    ERThird = 'Q1: 23, Q2: 0'

    ERFourth = 'Q1: 0, Q2: 0'

 

    SP1Index = 60

    SP1SubIndex = 1

 

    LogicIndex = 1

    FuncModeIndex = 2

    HystSubIndex = 3

 

    FuncModeprod_name = iolink_master.write(1, Index1, FuncModeIndex)  # change to single

    Logicprod_name = iolink_master.write(1, Index1, LogicIndex)  # set logic to active low

    SP1prod_name = iolink_master.write(410, SP1Index, SP1SubIndex)  # set value for SP1

    Hystprod_name = iolink_master.write(20, Index1, HystSubIndex)  # set hysteresis

    prod_name1 = iolink_master.read(Index1)

    time.sleep(0.6)

 

    Saveprod_name = iolink_master.write(192, systemcommand)  # save

    time.sleep(1)

 

    DEACTIVATE_PSU()

    sleep(3)

    ACTIVATE_PSU()

    sleep(3)

 

    digitalnum1,digitalnum2,digitalnum3,digitalnum4 =motor_turn.Q1PNP(num1=32, num2=55, num3=49,num4=0)   #30,52,22

    # time.sleep(0.6)

    sleep(5)

 

    if ER1 == prod_name1:

        result1 = 'Passed'

    else:

        result1 = 'Failed'

 

    if ERFirst == digitalnum1:

        outcomeFirst = "Passed"

    else:

        outcomeFirst = "Failed"

 

    if ERSecond == digitalnum2:

        outcomeSecond = "Passed"

    else:

        outcomeSecond = "Failed"

 

    if ERThird == digitalnum3:

        outcomeThird = "Passed"

    else:

        outcomeThird = "Failed"

 

    if ERFourth == digitalnum4:

        outcomeFourth = "Passed"

    else:

        outcomeFourth = "Failed"

 

    Subsave().savetoexcel1(path, num1, Name1, Index1, SubIndex1, str(ER1), str(prod_name1), result1, Sdf)

    Subsave().savetoexcelQs(path, num3, Name1, Index1, ERFirst, digitalnum1, outcomeFirst, ERSecond, digitalnum2,

                            outcomeSecond,

                            ERThird, digitalnum3, outcomeThird, ERFourth, digitalnum4, outcomeFourth, Sdf2)

 

    SEQUENCE_CQ()               #CONNECT BACK TO DEVICE

 

    assert prod_name1 == ER1

    assert digitalnum1 == 'Q1: 0, Q2: 0'

    assert digitalnum2 == 'Q1: 23, Q2: 0'

    assert digitalnum3 == 'Q1: 23, Q2: 0'

    assert digitalnum4 == 'Q1: 0, Q2: 0'

time.sleep(3)

 

@pytest.mark.test_id(17849)  #20

def test_Q1_Single_Hysteresis_Active_High(iolink_master):

 

    systemcommand = 2

    resetprod_name = iolink_master.write(130, systemcommand)

 

    num1 = 24

    Name1 = 'Q1 Single Hysteresis Active High'

    Index1 = 61

    SubIndex1 = 0

    ER1 = {1: 0, 2: 1, 3: 20}

    num3 = 5

    ERFirst = 'Q1: 23, Q2: 0'

    ERSecond = 'Q1: 0, Q2: 0'

    ERThird = 'Q1: 0, Q2: 0'

    ERFourth = 'Q1: 23, Q2: 0'

 

    SP1Index = 60

    SP1SubIndex = 1

 

    LogicIndex = 1

    FuncModeIndex = 2

    HystSubIndex = 3

    # Q2outputswitching = 121

    #

    # q2switching = iolink_master.write(0, Q2outputswitching)  # Q2 Deactivated

    # time.sleep(1)

    # Saveprod_name = iolink_master.write(192, systemcommand)  # save

    # time.sleep(2)

 

    FuncModeprod_name = iolink_master.write(1, Index1, FuncModeIndex)  # change to single

    # Logicprod_name = iolink_master.write(1, Index1, LogicIndex)  # set logic to active low

    SP1prod_name = iolink_master.write(410, SP1Index, SP1SubIndex)  # set value for SP1

    Hystprod_name = iolink_master.write(20, Index1, HystSubIndex)  # set hysteresis

    prod_name1 = iolink_master.read(Index1)

    time.sleep(0.6)

 

    Saveprod_name = iolink_master.write(192, systemcommand)  # save

    time.sleep(1)

 

    DEACTIVATE_PSU()

    sleep(3)

    ACTIVATE_PSU()

    sleep(3)

 

    digitalnum1,digitalnum2,digitalnum3,digitalnum4 =motor_turn.Q1PNP(num1=32, num2=55, num3=49,num4=0)   #30,52,22

    # time.sleep(0.6)

    sleep(5)

 

    if ER1 == prod_name1:

        result1 = 'Passed'

    else:

        result1 = 'Failed'

 

    if ERFirst == digitalnum1:

        outcomeFirst = "Passed"

    else:

        outcomeFirst = "Failed"

 

    if ERSecond == digitalnum2:

        outcomeSecond = "Passed"

    else:

        outcomeSecond = "Failed"

 

    if ERThird == digitalnum3:

        outcomeThird = "Passed"

    else:

        outcomeThird = "Failed"

 

    if ERFourth == digitalnum4:

        outcomeFourth = "Passed"

    else:

        outcomeFourth = "Failed"

 

    Subsave().savetoexcel1(path, num1, Name1, Index1, SubIndex1, str(ER1), str(prod_name1), result1, Sdf)

    Subsave().savetoexcelQs(path, num3, Name1, Index1, ERFirst, digitalnum1, outcomeFirst, ERSecond, digitalnum2,

                            outcomeSecond,

                            ERThird, digitalnum3, outcomeThird, ERFourth, digitalnum4, outcomeFourth, Sdf2)

 

    SEQUENCE_CQ()               #CONNECT BACK TO DEVICE

 

    assert prod_name1 == ER1

    assert digitalnum1 == 'Q1: 23, Q2: 0'

    assert digitalnum2 == 'Q1: 0, Q2: 0'

    assert digitalnum3 == 'Q1: 0, Q2: 0'

    assert digitalnum4 == 'Q1: 23, Q2: 0'

time.sleep(3)

 

@pytest.mark.test_id(17827)  #21

def test_Q1Reset_WindowMode_DefaultSetting(iolink_master):

 

    systemcommand = 2

    resetprod_name = iolink_master.write(130, systemcommand)

 

    num1 = 25

    Name1 = 'Q1 Window Mode Default Values'

    Index1 = 60

    SubIndex1 = 0

    ER1 = {1: 1000, 2: 5000}

 

    num2 = 26

    Name2 = 'Q1 Window Default Switching'

    Index2 = 61

    SubIndex2 = '1:lOGIC','2:Function','3:Hysteresis'

    ER2 = {1:0, 2:2, 3:0}

 

    prod_name1 = iolink_master.read(Index1)

    prod_name2 = iolink_master.read(Index2)

 

    if ER1 == prod_name1:                 # for excel record so i dont need to compare one by one

        result1 = 'Passed'

    else:

        result1 = 'Failed'

 

    if ER2 == prod_name2:

        result2 = 'Passed'

    else:

        result2 = 'Failed'

 

    Subsave().savetoexcel1(path, num1, Name1, Index1, SubIndex1, str(ER1), str(prod_name1), result1,  Sdf)  # save all the data in excel

    Subsave().savetoexcel2(path, num2, Name2, Index2, SubIndex2, str(ER2), str(prod_name2), result2, Sdf)

    assert prod_name1 == ER1

    assert prod_name2 == ER2

time.sleep(3)

 

@pytest.mark.test_id(17837)  #22

def test_Q1_Offset_Default(iolink_master):

 

    systemcommand = 2

    resetprod_name = iolink_master.write(130, systemcommand)

    time.sleep(2)

 

    num1 = 27

    Name1 = 'Q1 Window Mode Offset Default'

    Index1 = 4371

    SubIndex1 = 0

    ER1 = 40

 

    num2 = 28

    Name2 = 'Q1 Window Mode Switching Default'

    Index2 = 61

    SubIndex2 = 0

    FuncIndex = 2

    ER2 = {1:0, 2:2, 3:0}

    prod_name1 = iolink_master.read(Index1)

    prod_name2 = iolink_master.read(Index2)

 

    if ER1 == prod_name1:

        result1 = 'Passed'

    else:

        result1 = 'Failed'

 

    if ER2 == prod_name2:

        result2 = 'Passed'

    else:

        result2 = 'Failed'

 

    Subsave().savetoexcel1(path, num1, Name1, Index1, SubIndex1, str(ER1), str(prod_name1), result1,Sdf)

    Subsave().savetoexcel2(path, num2, Name2, Index2, SubIndex2, str(ER2), str(prod_name2), result2, Sdf)

    assert prod_name1 == ER1

    assert prod_name2 == ER2

time.sleep(3)

 

# @pytest.mark.test_id(17863)  #23

def test_Q1_Offset_Default_Active_Low(iolink_master):

    systemcommand = 2

    resetprod_name = iolink_master.write(130, systemcommand)

 

    num1 = 29

    Name1 = 'Q1 Offset Default Active Low'

    Index1 = 4371

    SubIndex1 = 0

    ER1 = 40

 

    num2 = 30

    Name2 = 'Q1 Default Active Low Switching'

    Index2 = 61

    SubIndex2 = 0

    ER2 = {1: 1, 2: 128, 3: 0}

    num3 = 6

    ERFirst = 'Q1: 23, Q2: 0'

    ERSecond = 'Q1: 0, Q2: 0'

    ERThird = 'Q1: 23, Q2: 0'

    ERFourth = 'Q1: 0, Q2: 0'

 

    SPIndex = 60

    SP1Index = 1

 

    LogicIndex = 1

    FuncModeIndex = 2

    HystSubIndex = 3

 

    FuncModeprod_name = iolink_master.write(128, Index2, FuncModeIndex)  # change to offset mode

    Logicprod_name = iolink_master.write(1, Index2, LogicIndex)  # set logic to active low

    SP1prod_name = iolink_master.write(300, SPIndex, SP1Index)  # set value for SP1

    # Hystprod_name = iolink_master.write(0, Index1, HystSubIndex)      # set hysteresis

    prod_name1 = iolink_master.read(Index1)  # read default offset

    prod_name2 = iolink_master.read(Index2)

    time.sleep(0.6)

    Saveprod_name = iolink_master.write(192, systemcommand)  # save

    time.sleep(1)

 

    DEACTIVATE_PSU()

    sleep(3)

    ACTIVATE_PSU()

    sleep(3)

    digitalnum1, digitalnum2, digitalnum3, digitalnum4 = motor_turn.Q1PNP(num1=21, num2=46, num3=30,num4=0)  # 30,52,22

 

    sleep(5)

 

    if ER1 == prod_name1:

        result1 = 'Passed'

    else:

        result1 = 'Failed'

 

    if ER2 == prod_name2:

        result2 = 'Passed'

    else:

        result2 = 'Failed'

 

    if ERFirst == digitalnum1:

        outcomeFirst = "Passed"

    else:

        outcomeFirst = "Failed"

 

    if ERSecond == digitalnum2:

        outcomeSecond = "Passed"

    else:

        outcomeSecond = "Failed"

 

    if ERThird == digitalnum3:

        outcomeThird = "Passed"

    else:

        outcomeThird = "Failed"

 

    if ERFourth == digitalnum4:

        outcomeFourth = "Passed"

    else:

        outcomeFourth = "Failed"

 

    Subsave().savetoexcel1(path, num1, Name1, Index1, SubIndex1, str(ER1), str(prod_name1), result1, Sdf)

    Subsave().savetoexcel2(path, num2, Name2, Index2, SubIndex2, str(ER2), str(prod_name2), result2, Sdf)

    Subsave().savetoexcelQs(path, num3, Name1, Index1, ERFirst, digitalnum1, outcomeFirst, ERSecond, digitalnum2,

                            outcomeSecond,

                            ERThird, digitalnum3, outcomeThird, ERFourth, digitalnum4, outcomeFourth, Sdf2)

 

    SEQUENCE_CQ()  # CONNECT BACK TO DEVICE

 

    assert prod_name1 == ER1

    assert prod_name2 == ER2

    assert digitalnum1 == 'Q1: 23, Q2: 0'

    assert digitalnum2 == 'Q1: 0, Q2: 0'

    assert digitalnum3 == 'Q1: 23, Q2: 0'

    assert digitalnum4 == 'Q1: 0, Q2: 0'

time.sleep(3)

 

# @pytest.mark.test_id(17863)  # 24

def test_Q1_Offset_Default_Active_High(iolink_master):

    systemcommand = 2

    resetprod_name = iolink_master.write(130, systemcommand)

 

    num1 = 31

    Name1 = 'Q1 Offset Default Active High'

    Index1 = 4371

    SubIndex1 = 0

    ER1 = 40

 

    num2 = 32

    Name2 = 'Q1 Default Active High Switching'

    Index2 = 61

    SubIndex2 = 0

    ER2 = {1: 0, 2: 128, 3: 0}

    num3 = 7

    ERFirst = 'Q1: 0, Q2: 0'

    ERSecond = 'Q1: 23, Q2: 0'

    ERThird = 'Q1: 0, Q2: 0'

    ERFourth = 'Q1: 23, Q2: 0'

 

    SPIndex = 60

    SP1Index = 1

 

    LogicIndex = 1

    FuncModeIndex = 2

    HystSubIndex = 3

 

    FuncModeprod_name = iolink_master.write(128, Index2, FuncModeIndex)  # change to offset mode

    Logicprod_name = iolink_master.write(0, Index2, LogicIndex)  # set logic to active high

    SP1prod_name = iolink_master.write(300, SPIndex, SP1Index)  # set value for SP1

    # Hystprod_name = iolink_master.write(0, Index1, HystSubIndex)      # set hysteresis

    prod_name1 = iolink_master.read(Index1)  # read default offset

    prod_name2 = iolink_master.read(Index2)

    time.sleep(0.6)

    Saveprod_name = iolink_master.write(192, systemcommand)  # save

    time.sleep(1)

 

    DEACTIVATE_PSU()

    sleep(3)

    ACTIVATE_PSU()

    sleep(3)

    digitalnum1, digitalnum2, digitalnum3, digitalnum4 = motor_turn.Q1PNP(num1=21, num2=46, num3=30,num4=0)   # 30,52,22

 

    sleep(5)

 

    if ER1 == prod_name1:

        result1 = 'Passed'

    else:

        result1 = 'Failed'

 

    if ER2 == prod_name2:

        result2 = 'Passed'

    else:

        result2 = 'Failed'

 

    if ERFirst == digitalnum1:

        outcomeFirst = "Passed"

    else:

        outcomeFirst = "Failed"

 

    if ERSecond == digitalnum2:

        outcomeSecond = "Passed"

    else:

        outcomeSecond = "Failed"

 

    if ERThird == digitalnum3:

        outcomeThird = "Passed"

    else:

        outcomeThird = "Failed"

 

    if ERFourth == digitalnum4:

        outcomeFourth = "Passed"

    else:

        outcomeFourth = "Failed"

 

    Subsave().savetoexcel1(path, num1, Name1, Index1, SubIndex1, str(ER1), str(prod_name1), result1, Sdf)

    Subsave().savetoexcel2(path, num2, Name2, Index2, SubIndex2, str(ER2), str(prod_name2), result2, Sdf)

    Subsave().savetoexcelQs(path, num3, Name1, Index1, ERFirst, digitalnum1, outcomeFirst, ERSecond, digitalnum2,

                            outcomeSecond,

                            ERThird, digitalnum3, outcomeThird, ERFourth, digitalnum4, outcomeFourth, Sdf2)

 

    SEQUENCE_CQ()  # CONNECT BACK TO DEVICE

 

    assert prod_name1 == ER1

    assert prod_name2 == ER2

    assert digitalnum1 == 'Q1: 0, Q2: 0'

    assert digitalnum2 == 'Q1: 23, Q2: 0'

    assert digitalnum3 == 'Q1: 0, Q2: 0'

    assert digitalnum4 == 'Q1: 23, Q2: 0'

time.sleep(3)

 

print("=======================Continue with Q2 swtiching mode =============================================")

@pytest.mark.test_id(17858)  #25

def test_Q2_WindowMode_Hysteresis_Active_High(iolink_master):

 

    systemcommand = 2

    resetprod_name = iolink_master.write(130, systemcommand)

 

    num1 = 33

    Name1 = 'Q2 Window Mode Hysteresis Active High'

    Index1 = 63

    SubIndex1 = 0

    ER1 = {1: 0, 2: 2, 3: 130}

    num3 = 8

    ERFirst = 'Q1: 0, Q2: 23'

    ERSecond = 'Q1: 0, Q2: 0'

    ERThird = 'Q1: 0, Q2: 23'

    ERFourth = 'Q1: 0, Q2: 0'

 

    SPIndex = 62

    SP1SubIndex = 1

    SP2SubIndex = 2

 

    LogicIndex = 1

    FuncModeIndex = 2

    HystSubIndex = 3

    # Q2outputswitching = 121

    #

    # q2switching = iolink_master.write(34, Q2outputswitching)   #switch to digital from analogue

    # time.sleep(1)

    # Saveprod_name = iolink_master.write(192, systemcommand)  # save

    # time.sleep(2)

    Funprod_name = iolink_master.write(2, Index1, FuncModeIndex)

    Logicprod_name = iolink_master.write(0, Index1, LogicIndex)

    SP1prod_name = iolink_master.write(240, SPIndex, SP1SubIndex)

    SP2prod_name = iolink_master.write(340, SPIndex, SP2SubIndex)

    Hystprod_name = iolink_master.write(130, Index1, HystSubIndex)

    prod_name1 = iolink_master.read(Index1)

 

    Saveprod_name = iolink_master.write(192, systemcommand)  # save

    time.sleep(1)

 

    DEACTIVATE_PSU()

    sleep(3)

    ACTIVATE_PSU()

    sleep(3)

    digital2num1, digital2num2,digital2num3, digital2num4 = motor_turn.Q2PNP(num1=38, num2=56, num3=30, num4=0)  # 30,52,22

    sleep(5)

 

 

    if ER1 == prod_name1:                 # for excel record so i dont need to compare one by one

        result1 = 'Passed'

    else:

        result1 = 'Failed'

 

    if ERFirst == digital2num1:

        outcomeFirst = "Passed"

    else:

        outcomeFirst = "Failed"

 

    if ERSecond == digital2num2:

        outcomeSecond = "Passed"

    else:

        outcomeSecond = "Failed"

 

    if ERThird == digital2num3:

        outcomeThird = "Passed"

    else:

        outcomeThird = "Failed"

 

    if ERFourth == digital2num4:

        outcomeFourth = "Passed"

    else:

        outcomeFourth = "Failed"

 

    Subsave().savetoexcel1(path, num1, Name1, Index1, SubIndex1, str(ER1), str(prod_name1), result1, Sdf)

    Subsave().savetoexcelQs(path, num3, Name1, Index1, ERFirst, digital2num1, outcomeFirst, ERSecond, digital2num2,

                            outcomeSecond,

                            ERThird, digital2num3, outcomeThird, ERFourth, digital2num4, outcomeFourth, Sdf2)

 

    SEQUENCE_CQ()

 

    assert prod_name1 == ER1

    assert digital2num1 == 'Q1: 0, Q2: 23'  # Due to Active Low, 0V is LED on, 23V is LED off

    assert digital2num2 == 'Q1: 0, Q2: 0'

    assert digital2num3 == 'Q1: 0, Q2: 23'

    assert digital2num4 == 'Q1: 0, Q2: 0'

time.sleep(3)

 

@pytest.mark.test_id(17859)  #26

def test_Q2_WindowMode_Hysteresis_Active_Low(iolink_master):

 

    systemcommand = 2

    resetprod_name = iolink_master.write(130, systemcommand)

    time.sleep(1)

 

    num1 = 34

    Name1 = 'Q2 Window Mode Hysteresis Active Low'

    Index1 = 63

    SubIndex1 = 0

    ER1 = {1:1, 2:2, 3:130}

    num3 = 9

    ERFirst = 'Q1: 0, Q2: 0'

    ERSecond ='Q1: 0, Q2: 23'

    ERThird =  'Q1: 0, Q2: 0'

    ERFourth = 'Q1: 0, Q2: 23'

 

    SPIndex = 62

    SP1SubIndex = 1

    SP2SubIndex = 2

 

    HystSubIndex = 3

    LogicIndex = 1

    FuncModeIndex=2

 

    SP1prod_name = iolink_master.write(240, SPIndex, SP1SubIndex)

    SP2prod_name = iolink_master.write(340, SPIndex, SP2SubIndex)

    Funprod_name = iolink_master.write(2, Index1, FuncModeIndex)

    Logicprod_name = iolink_master.write(1, Index1, LogicIndex)

    Hystprod_name = iolink_master.write(130, Index1, HystSubIndex)

    prod_name1 = iolink_master.read(Index1)

    time.sleep(0.6)

 

    Saveprod_name = iolink_master.write(192, systemcommand)  # save

    time.sleep(1)

 

    DEACTIVATE_PSU()

    sleep(3)

    ACTIVATE_PSU()

    sleep(3)

    digital2num1, digital2num2,digital2num3, digital2num4 = motor_turn.Q2PNP(num1=38, num2=56, num3=30, num4=0)  # 30,52,22

    sleep(5)

 

    if ER1 == prod_name1:

        result1 = 'Passed'

    else:

        result1 = 'Failed'

 

    if ERFirst == digital2num1:

        outcomeFirst = "Passed"

    else:

        outcomeFirst = "Failed"

 

    if ERSecond == digital2num2:

        outcomeSecond = "Passed"

    else:

        outcomeSecond = "Failed"

 

    if ERThird == digital2num3:

        outcomeThird = "Passed"

    else:

        outcomeThird = "Failed"

 

    if ERFourth == digital2num4:

        outcomeFourth = "Passed"

    else:

        outcomeFourth = "Failed"

 

    Subsave().savetoexcel1(path, num1, Name1, Index1, SubIndex1, str(ER1), str(prod_name1), result1, Sdf)

    Subsave().savetoexcelQs(path, num3, Name1, Index1, ERFirst, digital2num1, outcomeFirst, ERSecond, digital2num2,

                            outcomeSecond,

                            ERThird, digital2num3, outcomeThird, ERFourth, digital2num4, outcomeFourth, Sdf2)

    SEQUENCE_CQ()

 

    assert prod_name1 == ER1

    assert digital2num1 == 'Q1: 0, Q2: 0'

    assert digital2num2 == 'Q1: 0, Q2: 23'

    assert digital2num3 == 'Q1: 0, Q2: 0'

    assert digital2num4 == 'Q1: 0, Q2: 23'

time.sleep(3)

 

@pytest.mark.test_id(17861)  #28

def test_Q2_OffsetMode_Hysteresis_Active_High(iolink_master):

 

    systemcommand = 2

    resetprod_name = iolink_master.write(130, systemcommand)

    time.sleep(1)

 

    num1 = 35

    Name1 = 'Q2 OffSet Hysteresis Active High'

    Index1 = 63

    SubIndex1 = 0

    ER1 = {1: 0, 2: 128, 3: 110}

    num3 = 10

    ERFirst = 'Q1: 0, Q2: 0'

    ERSecond = 'Q1: 0, Q2: 23'

    ERThird = 'Q1: 0, Q2: 0'

    ERFourth = 'Q1: 0, Q2: 23'

 

    SP1Index = 62

    SP1SubIndex = 1

 

    LogicIndex = 1

    FuncModeIndex = 2

    HystSubIndex = 3

 

    OffsetIndex = 4372

    FuncModeprod_name = iolink_master.write(128,Index1, FuncModeIndex)         #change to offset mode

    time.sleep(1)

    Logicprod_name = iolink_master.write(0, Index1, LogicIndex)                # set logic to active high

    time.sleep(1)

    SP1prod_name = iolink_master.write(300, SP1Index, SP1SubIndex)             # set value for SP1

    time.sleep(1)

    OffSetprod_name = iolink_master.write(30, OffsetIndex)                    # set value for offset

    time.sleep(1)

    Hystprod_name = iolink_master.write(110, Index1, HystSubIndex)              # set hysteresis

    time.sleep(1)

    prod_name1 = iolink_master.read(Index1)

    time.sleep(1)

 

    DEACTIVATE_PSU()

    sleep(3)

    ACTIVATE_PSU()

    sleep(3)

 

    digital2num1, digital2num2,digital2num3, digital2num4 = motor_turn.Q2PNP(num1=29, num2=56, num3=26, num4=0)  # 30,52,22

    sleep(5)

 

    if ER1 == prod_name1:

        result1 = 'Passed'

    else:

        result1 = 'Failed'

 

    if ERFirst == digital2num1:

        outcomeFirst = "Passed"

    else:

        outcomeFirst = "Failed"

 

    if ERSecond == digital2num2:

        outcomeSecond = "Passed"

    else:

        outcomeSecond = "Failed"

 

    if ERThird == digital2num3:

        outcomeThird = "Passed"

    else:

        outcomeThird = "Failed"

 

    if ERFourth == digital2num4:

        outcomeFourth = "Passed"

    else:

        outcomeFourth = "Failed"

 

    Subsave().savetoexcel1(path, num1, Name1, Index1, SubIndex1, str(ER1), str(prod_name1), result1, Sdf)

    Subsave().savetoexcelQs(path, num3, Name1, Index1, ERFirst, digital2num1, outcomeFirst, ERSecond, digital2num2,

                            outcomeSecond,

                            ERThird, digital2num3, outcomeThird, ERFourth, digital2num4, outcomeFourth, Sdf2)

 

    SEQUENCE_CQ()

 

    assert prod_name1 == ER1

    assert digital2num1 == 'Q1: 0, Q2: 0'

    assert digital2num2 == 'Q1: 0, Q2: 23'

    assert digital2num3 == 'Q1: 0, Q2: 0'

    assert digital2num4 == 'Q1: 0, Q2: 23'

time.sleep(3)

 

@pytest.mark.test_id(17862)  #27

def test_Q2_OffsetMode_Hysteresis_Active_Low(iolink_master):

 

    systemcommand = 2

    resetprod_name = iolink_master.write(130, systemcommand)

    time.sleep(1)

 

   num1 = 36

    Name1 = 'Q2 OffSet Hysteresis Active Low'

    Index1 = 63

    SubIndex1 = 0

    ER1 = {1: 1, 2: 128, 3: 110}

    num3 = 11

    ERFirst = 'Q1: 0, Q2: 23'

    ERSecond ='Q1: 0, Q2: 0'

    ERThird = 'Q1: 0, Q2: 23'

    ERFourth = 'Q1: 0, Q2: 0'

 

    SP1Index = 62

    SP1SubIndex = 1

 

    LogicIndex = 1

    FuncModeIndex = 2

    HystSubIndex = 3

 

    OffsetIndex = 4372

    FuncModeprod_name = iolink_master.write(128, Index1, FuncModeIndex)  # change to offset mode

    Logicprod_name = iolink_master.write(1, Index1, LogicIndex)  # set logic to active low

    SP1prod_name = iolink_master.write(300, SP1Index, SP1SubIndex)  # set value for SP1

    OffSetprod_name = iolink_master.write(30, OffsetIndex)  # set value for offset

    Hystprod_name = iolink_master.write(110, Index1, HystSubIndex)  # set hysteresis

    prod_name1 = iolink_master.read(Index1)

    time.sleep(1)

 

    DEACTIVATE_PSU()

    sleep(3)

    ACTIVATE_PSU()

    sleep(3)

 

    digital2num1, digital2num2,digital2num3, digital2num4 = motor_turn.Q2PNP(num1=30, num2=56, num3=26, num4=0)  # 29,52,22

    sleep(5)

    if ER1 == prod_name1:

        result1 = 'Passed'

    else:

        result1 = 'Failed'

 

    if ERFirst == digital2num1:

        outcomeFirst = "Passed"

    else:

        outcomeFirst = "Failed"

 

    if ERSecond == digital2num2:

        outcomeSecond = "Passed"

    else:

        outcomeSecond = "Failed"

 

    if ERThird == digital2num3:

        outcomeThird = "Passed"

    else:

        outcomeThird = "Failed"

 

    if ERFourth == digital2num4:

        outcomeFourth = "Passed"

    else:

        outcomeFourth = "Failed"

 

    Subsave().savetoexcel1(path, num1, Name1, Index1, SubIndex1, str(ER1), str(prod_name1), result1, Sdf)

    Subsave().savetoexcelQs(path, num3, Name1, Index1, ERFirst, digital2num1, outcomeFirst, ERSecond, digital2num2,

                            outcomeSecond,

                            ERThird, digital2num3, outcomeThird, ERFourth, digital2num4, outcomeFourth, Sdf2)

    SEQUENCE_CQ()

 

    assert prod_name1 == ER1

    assert digital2num1 == 'Q1: 0, Q2: 23'

    assert digital2num2 == 'Q1: 0, Q2: 0'

    assert digital2num3 == 'Q1: 0, Q2: 23'

    assert digital2num4 == 'Q1: 0, Q2: 0'

time.sleep(3)

 

@pytest.mark.test_id(17864)  #29

def test_Q2_Single_Hysteresis_Active_Low(iolink_master):

 

    systemcommand = 2

    resetprod_name = iolink_master.write(130,  systemcommand)

 

    num1 = 37

    Name1 = 'Q2 Single Hysteresis Active Low'

    Index1 = 63

    SubIndex1 = 0

    ER1 = {1: 1, 2: 1, 3:20}

    num3 = 12

    ERFirst =  'Q1: 0, Q2: 0'

    ERSecond = 'Q1: 0, Q2: 23'

    ERThird = 'Q1: 0, Q2: 23'

    ERFourth = 'Q1: 0, Q2: 0'

 

    SP1Index = 62

    SP1SubIndex = 1

 

    LogicIndex = 1

    FuncModeIndex = 2

    HystSubIndex = 3

 

    FuncModeprod_name = iolink_master.write(1, Index1, FuncModeIndex)  # change to single mode

    Logicprod_name = iolink_master.write(1, Index1, LogicIndex)  # set logic to active low

    SP1prod_name = iolink_master.write(410, SP1Index, SP1SubIndex)  # set value for SP1

    Hystprod_name = iolink_master.write(20, Index1, HystSubIndex)  # set hysteresis

    prod_name1 = iolink_master.read(Index1)

    time.sleep(0.6)

 

    Saveprod_name = iolink_master.write(192, systemcommand)  # save

    time.sleep(1)

 

    DEACTIVATE_PSU()

    sleep(3)

    ACTIVATE_PSU()

    sleep(3)

 

    digital2num1, digital2num2, digital2num3, digital2num4 = motor_turn.Q2PNP(num1=32, num2=55, num3=49,num4=0)  # 30,52,22

    sleep(5)

 

    if ER1 == prod_name1:

        result1 = 'Passed'

    else:

        result1 = 'Failed'

 

    if ERFirst == digital2num1:

        outcomeFirst = "Passed"

    else:

        outcomeFirst = "Failed"

 

    if ERSecond == digital2num2:

        outcomeSecond = "Passed"

    else:

        outcomeSecond = "Failed"

 

    if ERThird == digital2num3:

        outcomeThird = "Passed"

    else:

        outcomeThird = "Failed"

 

    if ERFourth == digital2num4:

        outcomeFourth = "Passed"

    else:

        outcomeFourth = "Failed"

 

    Subsave().savetoexcel1(path, num1, Name1, Index1, SubIndex1, str(ER1), str(prod_name1), result1, Sdf)

    Subsave().savetoexcelQs(path, num3, Name1, Index1, ERFirst, digital2num1, outcomeFirst, ERSecond, digital2num2,

                            outcomeSecond,

                            ERThird, digital2num3, outcomeThird, ERFourth, digital2num4, outcomeFourth, Sdf2)

 

 

    SEQUENCE_CQ()  # CONNECT BACK TO DEVICE

 

    assert prod_name1 == ER1

    assert digital2num1 == 'Q1: 0, Q2: 0'

    assert digital2num2 == 'Q1: 0, Q2: 23'

    assert digital2num3 == 'Q1: 0, Q2: 23'

    assert digital2num4 == 'Q1: 0, Q2: 0'

time.sleep(3)

 

@pytest.mark.test_id(17863)  #30

def test_Q2_Single_Hysteresis_Active_High(iolink_master):

 

    systemcommand = 2

    resetprod_name = iolink_master.write(130, systemcommand)

 

    num1 = 38

    Name1 = 'Q2 Single Hysteresis Active High'

    Index1 = 63

    SubIndex1 = 0

    ER1 = {1: 0, 2: 1, 3: 20}

    num3 = 13

    ERFirst = 'Q1: 0, Q2: 23'

    ERSecond = 'Q1: 0, Q2: 0'

    ERThird = 'Q1: 0, Q2: 0'

    ERFourth = 'Q1: 0, Q2: 23'

 

    SP1Index = 62

    SP1SubIndex = 1

 

    LogicIndex = 1

    FuncModeIndex = 2

    HystSubIndex = 3

    # Q2outputswitching = 121

    #

    # q2switching = iolink_master.write(34, Q2outputswitching)  # switch to digital from analogue

    # time.sleep(1)

    # Saveprod_name = iolink_master.write(192, systemcommand)  # save

    # time.sleep(2)

    FuncModeprod_name = iolink_master.write(1, Index1, FuncModeIndex)  # change to Single mode

    Logicprod_name = iolink_master.write(0, Index1, LogicIndex)        # set logic to active high

    SP1prod_name = iolink_master.write(410, SP1Index, SP1SubIndex)     # set value for SP1

    Hystprod_name = iolink_master.write(20, Index1, HystSubIndex)      # set hysteresis

    prod_name1 = iolink_master.read(Index1)

    time.sleep(0.6)

    Saveprod_name = iolink_master.write(192, systemcommand)  # save

    time.sleep(1)

 

    DEACTIVATE_PSU()

    sleep(3)

    ACTIVATE_PSU()

    sleep(3)

    digital2num1, digital2num2,digital2num3,digital2num4=motor_turn.Q2PNP(num1=32, num2=55, num3=49, num4=0)   #30,52,22

 

    sleep(5)

 

    if ER1 == prod_name1:

        result1 = 'Passed'

    else:

        result1 = 'Failed'

 

    if ERFirst == digital2num1:

        outcomeFirst = "Passed"

    else:

        outcomeFirst = "Failed"

 

    if ERSecond == digital2num2:

        outcomeSecond = "Passed"

    else:

        outcomeSecond = "Failed"

 

    if ERThird == digital2num3:

        outcomeThird = "Passed"

    else:

        outcomeThird = "Failed"

 

    if ERFourth == digital2num4:

        outcomeFourth = "Passed"

    else:

        outcomeFourth = "Failed"

 

    Subsave().savetoexcel1(path, num1, Name1, Index1, SubIndex1, str(ER1), str(prod_name1), result1, Sdf)

    Subsave().savetoexcelQs(path, num3, Name1, Index1, ERFirst, digital2num1, outcomeFirst, ERSecond, digital2num2,

                            outcomeSecond,

                            ERThird, digital2num3, outcomeThird, ERFourth, digital2num4, outcomeFourth, Sdf2)

 

    SEQUENCE_CQ()  # CONNECT BACK TO DEVICE

 

    assert prod_name1 == ER1

    assert digital2num1 == 'Q1: 0, Q2: 23'

    assert digital2num2 == 'Q1: 0, Q2: 0'

    assert digital2num3 == 'Q1: 0, Q2: 0'

    assert digital2num4 == 'Q1: 0, Q2: 23'

time.sleep(3)

 

@pytest.mark.test_id(17857)  #31

def test_Q2_WindowMode_Default(iolink_master):

 

    systemcommand = 2

    resetprod_name = iolink_master.write(130, systemcommand)

    time.sleep(1)

 

    num1 = 39

    Name1 = 'Q2 Window Mode Default Values'

    Index1 = 62

    SubIndex1 = 0

    ER1 = {1: 1000, 2: 5000}

 

    num2 = 40

    Name2 = 'Q2 Window Default Switching'

    Index2 = 63

    SubIndex2 = '1:lOGIC','2:Function','3:Hysteresis'

    ER2 = {1:0, 2:2, 3:0}

 

    # Q2outputswitching = 121

    #

    # q2switching = iolink_master.write(34, Q2outputswitching)  # switch to digital from analogue

    prod_name1 = iolink_master.read(Index1)

    prod_name2 = iolink_master.read(Index2)

 

    if ER1 == prod_name1:                 # for excel record so i dont need to compare one by one

        result1 = 'Passed'

    else:

        result1 = 'Failed'

 

    if ER2 == prod_name2:

        result2 = 'Passed'

    else:

        result2 = 'Failed'

 

    Subsave().savetoexcel1(path, num1, Name1, Index1, SubIndex1, str(ER1), str(prod_name1), result1,  Sdf)  # save all the data in excel

    Subsave().savetoexcel2(path, num2, Name2, Index2, SubIndex2, str(ER2), str(prod_name2), result2, Sdf)

    assert prod_name1 == ER1

    assert prod_name2 == ER2

time.sleep(3)

 

@pytest.mark.test_id(17860)  #32

def test_Q2_Offset_Default(iolink_master):

 

    systemcommand = 2

    resetprod_name = iolink_master.write(130, systemcommand)

    time.sleep(1)

 

    num1 = 41

    Name1 = 'Q2 Window Mode Offset Default'

    Index1 = 4372

    SubIndex1 = 0

    ER1 = 40

 

    num2 = 42

    Name2 = 'Q2 Window Mode Switching Default'

    Index2 = 63

    SubIndex2 = 0

    FuncIndex = 2

    ER2 = {1: 0, 2: 2, 3: 0}

 

    d1 = iolink_master.write(30 , Index1)

 

    resetprod_name2 = iolink_master.write(130, systemcommand)

 

    prod_name1 = iolink_master.read(Index1)

    prod_name2 = iolink_master.read(Index2)

 

    if ER1 == prod_name1:

        result1 = 'Passed'

    else:

        result1 = 'Failed'

 

    if ER2 == prod_name2:

        result2 = 'Passed'

    else:

        result2 = 'Failed'

 

    Subsave().savetoexcel1(path, num1, Name1, Index1, SubIndex1, str(ER1), str(prod_name1), result1, Sdf)

    Subsave().savetoexcel2(path, num2, Name2, Index2, SubIndex2, str(ER2), str(prod_name2), result2, Sdf)

    assert prod_name1 == ER1

    assert prod_name2 == ER2

    time.sleep(3)

 

# @pytest.mark.test_id(17863)  #33

def test_Q2_Offset_Default_Active_Low(iolink_master):

 

    systemcommand = 2

    resetprod_name = iolink_master.write(130, systemcommand)

 

    num1 = 43

    Name1 = 'Q2 Offset Default Active Low'

    Index1 = 4372

    SubIndex1 = 0

    ER1 = 40

 

    num2 = 44

    Name2 = 'Q2 Default Active Low Switching'

    Index2 = 63

    SubIndex2 = 0

    ER2 = {1: 1, 2: 128, 3: 0}

    num3 = 14

    ERFirst = 'Q1: 0, Q2: 23'

    ERSecond = 'Q1: 0, Q2: 0'

    ERThird = 'Q1: 0, Q2: 23'

    ERFourth = 'Q1: 0, Q2: 0'

 

    SPIndex = 62

    SP1Index = 1

 

    LogicIndex = 1

    FuncModeIndex = 2

    HystSubIndex = 3

 

    FuncModeprod_name = iolink_master.write(128, Index2, FuncModeIndex)  # change to Single mode

    Logicprod_name = iolink_master.write(1, Index2, LogicIndex)        # set logic to active low

    SP1prod_name = iolink_master.write(300, SPIndex, SP1Index)     # set value for SP1

    # Hystprod_name = iolink_master.write(0, Index1, HystSubIndex)      # set hysteresis

    prod_name1 = iolink_master.read(Index1)    #read default offset

    prod_name2 = iolink_master.read(Index2)

    time.sleep(0.6)

    Saveprod_name = iolink_master.write(192, systemcommand)  # save

    time.sleep(1)

 

    DEACTIVATE_PSU()

    sleep(3)

    ACTIVATE_PSU()

    sleep(3)

    digital2num1, digital2num2,digital2num3,digital2num4=motor_turn.Q2PNP(num1=21, num2=46, num3=30,num4=0)   #30,52,22

 

    sleep(5)

 

    if ER1 == prod_name1:

        result1 = 'Passed'

    else:

        result1 = 'Failed'

 

    if ER2 == prod_name2:

        result2 = 'Passed'

    else:

        result2 = 'Failed'

 

    if ERFirst == digital2num1:

        outcomeFirst = "Passed"

    else:

        outcomeFirst = "Failed"

 

    if ERSecond == digital2num2:

        outcomeSecond = "Passed"

    else:

        outcomeSecond = "Failed"

 

    if ERThird == digital2num3:

        outcomeThird = "Passed"

    else:

        outcomeThird = "Failed"

 

    if ERFourth == digital2num4:

        outcomeFourth = "Passed"

    else:

        outcomeFourth = "Failed"

 

    Subsave().savetoexcel1(path, num1, Name1, Index1, SubIndex1, str(ER1), str(prod_name1), result1, Sdf)

    Subsave().savetoexcel2(path, num2, Name2, Index2, SubIndex2, str(ER2), str(prod_name2), result2, Sdf)

    Subsave().savetoexcelQs(path, num3, Name1, Index1, ERFirst, digital2num1, outcomeFirst, ERSecond, digital2num2,

                            outcomeSecond,

                            ERThird, digital2num3, outcomeThird, ERFourth, digital2num4, outcomeFourth, Sdf2)

 

    SEQUENCE_CQ()  # CONNECT BACK TO DEVICE

 

    assert prod_name1 == ER1

    assert prod_name2 == ER2

    assert digital2num1 == 'Q1: 0, Q2: 23'

    assert digital2num2 == 'Q1: 0, Q2: 0'

    assert digital2num3 == 'Q1: 0, Q2: 23'

    assert digital2num4 == 'Q1: 0, Q2: 0'

time.sleep(3)

 

# @pytest.mark.test_id(17863)  #34

def test_Q2_Offset_Default_Active_High(iolink_master):

    systemcommand = 2

    resetprod_name = iolink_master.write(130, systemcommand)

 

    num1 = 45

    Name1 = 'Q2 Offset Default Active High'

    Index1 = 4372

    SubIndex1 = 0

    ER1 = 40

 

    num2 = 46

    Name2 = 'Q2 Default Active High Switching'

    Index2 = 63

    SubIndex2 = 0

    ER2 = {1: 0, 2: 128, 3: 0}

    num3 = 15

    ERFirst = 'Q1: 0, Q2: 0'

    ERSecond = 'Q1: 0, Q2: 23'

    ERThird = 'Q1: 0, Q2: 0'

    ERFourth = 'Q1: 0, Q2: 23'

 

    SPIndex = 62

    SP1Index = 1

 

    LogicIndex = 1

    FuncModeIndex = 2

    HystSubIndex = 3

 

    FuncModeprod_name = iolink_master.write(128, Index2, FuncModeIndex)  # change to offset mode

    Logicprod_name = iolink_master.write(0, Index2, LogicIndex)  # set logic to active high

    SP1prod_name = iolink_master.write(300, SPIndex, SP1Index)  # set value for SP1

    # Hystprod_name = iolink_master.write(0, Index1, HystSubIndex)      # set hysteresis

    prod_name1 = iolink_master.read(Index1)  # read default offset

    prod_name2 = iolink_master.read(Index2)

    time.sleep(0.6)

    Saveprod_name = iolink_master.write(192, systemcommand)  # save

    time.sleep(1)

 

    DEACTIVATE_PSU()

    sleep(3)

    ACTIVATE_PSU()

    sleep(3)

    digital2num1, digital2num2, digital2num3, digital2num4 = motor_turn.Q2PNP(num1=21, num2=46, num3=30,num4=0)   # 30,52,22

 

    sleep(5)

 

    if ER1 == prod_name1:

        result1 = 'Passed'

    else:

        result1 = 'Failed'

 

    if ER2 == prod_name2:

        result2 = 'Passed'

    else:

        result2 = 'Failed'

 

    if ERFirst == digital2num1:

        outcomeFirst = "Passed"

    else:

        outcomeFirst = "Failed"

 

    if ERSecond == digital2num2:

        outcomeSecond = "Passed"

    else:

        outcomeSecond = "Failed"

 

    if ERThird == digital2num3:

        outcomeThird = "Passed"

    else:

        outcomeThird = "Failed"

 

    if ERFourth == digital2num4:

        outcomeFourth = "Passed"

    else:

        outcomeFourth = "Failed"

 

    Subsave().savetoexcel1(path, num1, Name1, Index1, SubIndex1, str(ER1), str(prod_name1), result1, Sdf)

    Subsave().savetoexcel2(path, num2, Name2, Index2, SubIndex2, str(ER2), str(prod_name2), result2, Sdf)

    Subsave().savetoexcelQs(path, num3, Name1, Index1, ERFirst, digital2num1, outcomeFirst, ERSecond, digital2num2,

                            outcomeSecond,

                            ERThird, digital2num3, outcomeThird, ERFourth, digital2num4, outcomeFourth, Sdf2)

 

    SEQUENCE_CQ()  # CONNECT BACK TO DEVICE

 

    assert prod_name1 == ER1

    assert prod_name2 == ER2

    assert digital2num1 == 'Q1: 0, Q2: 0'

    assert digital2num2 == 'Q1: 0, Q2: 23'

    assert digital2num3 == 'Q1: 0, Q2: 0'

    assert digital2num4 == 'Q1: 0, Q2: 23'

time.sleep(3)

 

# @pytest.mark.test_id()  #35

def test_Q2_Pin2_output_defaultChecking(iolink_master):

 

    systemcommand = 2

    resetprod_name = iolink_master.write(130, systemcommand)

 

    num1 = 47

    Name1 = 'Pin2 Default output Checking'

    Index1 = 121

    SubIndex1 = 0

    ER1 = 34

 

    prod_name1 = iolink_master.read(Index1)  # switch to digital from analogue

    time.sleep(2)

 

    if ER1 == prod_name1:

        result1 = 'Passed'

    else:

        result1 = 'Failed'

 

    Subsave().savetoexcel1(path, num1, Name1, Index1, SubIndex1, str(ER1), str(prod_name1), result1, Sdf)

    assert prod_name1 == ER1

 

print("=======================Teach=============================================")

print("=======================Continue with Teach =============================================")

 

@pytest.mark.test_id(19409)   #36

def test_TeachQ1_Window(iolink_master):

 

    systemcommand = 2

    resetprod_name = iolink_master.write(130, systemcommand)

 

    num1 = 48                                 # which row to save the data

    Name1 = 'Teach-In Q1 Window SP2'                        # Name of the testcase

    Index1 =  60                                 # IO index

    SubIndex1 = 2

    ER1 = {1>300 or 1<350}          # Expected return result for SP2

 

    num2 = 49  # which row to save the data

    Name2 = 'Teach-In Q1 Window SP1'  # Name of the testcase

    Index2 = 60  # IO index

    SubIndex2 = 1

    ER2 = {2>400 or 2<450}         # Expected return result for SP1

 

    num4 = 50

    Name4 = 'Teach-In Q1 Window Status SP2'

    Index4 = 59

    SubIndex4 = 0

    ER4 = {1: True, 2: False, 3: 2}

 

    num5 = 51

    Name5 = 'Teach-In Q1 Window Status SP1'

    Index5 = 59

    SubIndex5 = 0

    ER5 =  {1: False, 2: True, 3: 1}          #Teacg flag SP2, Teach Flag SP1, Teach state

 

    num6= 52

    Name6 = 'Teach-In Q1 Mode'

    Index6 = 61

    SubIndex6 = 2

    ER6 = 2

 

    teachchannel = 58

    channelprod_name = iolink_master.write(1, teachchannel)

    modeprod_name = iolink_master.write(2, Index6, SubIndex6)

    time.sleep(2)

    motor_turn.Teach_Turn(num1=32)

    sp2 = iolink_master.write(66, systemcommand)

    time.sleep(4)

    prod_name4 = iolink_master.read(Index4)

    time.sleep(2)

    motor_turn.Teach_Turn(num1=50)

    sp1 = iolink_master.write(65, systemcommand)

    time.sleep(4)

    prod_name5 = iolink_master.read(Index5)

    time.sleep(2)

    motor_turn.finalposition()

 

    prod_name1 = iolink_master.read(Index1,SubIndex1)

    prod_name2 = iolink_master.read(Index2, SubIndex2)

    prod_name6 = iolink_master.read(Index6,SubIndex6)

 

    if prod_name1 > 300 and prod_name1 < 350:

        result1 = "Passed"

    else:

        result1 = "Failed"

 

    if prod_name2 >400 and prod_name2<450:

        result2 = 'Passed'

    else:

        result2 = 'Failed'

 

    if ER4 == prod_name4:

        result4 = 'Passed'

    else:

        result4 = 'Failed'

 

    if ER5 == prod_name5:

        result5 = 'Passed'

    else:

        result5 = 'Failed'

 

    if ER6 == prod_name6:

        result6 = 'Passed'

    else:

        result6 = 'Failed'

 

    Subsave().savetoexcel1(path, num1, Name1, Index1, SubIndex1, str(ER1), str(prod_name1), result1, Sdf)

    Subsave().savetoexcel2(path, num2, Name2, Index2, SubIndex2, str(ER2), str(prod_name2), result2, Sdf)

    Subsave().savetoexcel4(path, num4, Name4, Index4, SubIndex4, str(ER4), str(prod_name4), result4, Sdf)

    Subsave().savetoexcel5(path, num5, Name5, Index5, SubIndex5, str(ER5), str(prod_name5), result5, Sdf)

    Subsave().savetoexcel6(path, num6, Name6, Index6, SubIndex6, str(ER6), str(prod_name6), result6, Sdf)

    assert prod_name1 > 300 and prod_name1 < 350  # Compare the expected result with the actual result that generated by pytest

    assert prod_name2 > 400 and prod_name2 < 450

    assert prod_name4 == ER4

    assert prod_name5 == ER5

    assert prod_name6 == ER6

 

# @pytest.mark.test_id()  # 37

def test_TeachQ1_Single(iolink_master):

    systemcommand = 2

    resetprod_name = iolink_master.write(130, systemcommand)

 

    num1 = 53  # which row to save the data

    Name1 = 'Teach-In Q1 Single SP2'  # Name of the testcase

    Index1 = 60  # IO index

    SubIndex1 = 2

    ER1 = {1 > 300 or 1 < 350}  # Expected return result for SP2

 

    num2 = 54  # which row to save the data

    Name2 = 'Teach-In Q1 Single SP1'  # Name of the testcase

    Index2 = 60  # IO index

    SubIndex2 = 1

    ER2 = {2 > 400 or 2 < 450}  # Expected return result for SP1

 

    num4 = 55

    Name4 = 'Teach-In Q1 Single Status SP2'

    Index4 = 59

    SubIndex4 = 0

    ER4 = {1: True, 2: False, 3: 2}

 

    num5 = 56

    Name5 = 'Teach-In Q1 Single Status SP1'

    Index5 = 59

    SubIndex5 = 0

    ER5 = {1: False, 2: True, 3: 1}  # Teacg flag SP2, Teach Flag SP1, Teach state

 

    num6 = 57

    Name6 = 'Teach-In Q1 Mode'

    Index6 = 61

    SubIndex6 = 2

    ER6 = 1

 

    teachchannel = 58

    channelprod_name = iolink_master.write(1, teachchannel)

    modeprod_name = iolink_master.write(1, Index6, SubIndex6)

    time.sleep(2)

    motor_turn.Teach_Turn(num1=32)

    sp2 = iolink_master.write(66, systemcommand)

    time.sleep(4)

    prod_name4 = iolink_master.read(Index4)

    time.sleep(2)

    motor_turn.Teach_Turn(num1=50)

    sp1 = iolink_master.write(65, systemcommand)

    time.sleep(4)

    prod_name5 = iolink_master.read(Index5)

    time.sleep(2)

    motor_turn.finalposition()

 

    prod_name1 = iolink_master.read(Index1, SubIndex1)

    prod_name2 = iolink_master.read(Index2, SubIndex2)

    prod_name6 = iolink_master.read(Index6, SubIndex6)

 

    if prod_name1 > 300 and prod_name1 < 350:

        result1 = "Passed"

    else:

        result1 = "Failed"

 

    if prod_name2 > 400 and prod_name2 < 450:

        result2 = 'Passed'

    else:

        result2 = 'Failed'

 

    if ER4 == prod_name4:

        result4 = 'Passed'

    else:

        result4 = 'Failed'

 

    if ER5 == prod_name5:

        result5 = 'Passed'

   else:

        result5 = 'Failed'

 

    if ER6 == prod_name6:

        result6 = 'Passed'

    else:

        result6 = 'Failed'

 

    Subsave().savetoexcel1(path, num1, Name1, Index1, SubIndex1, str(ER1), str(prod_name1), result1, Sdf)

    Subsave().savetoexcel2(path, num2, Name2, Index2, SubIndex2, str(ER2), str(prod_name2), result2, Sdf)

    Subsave().savetoexcel4(path, num4, Name4, Index4, SubIndex4, str(ER4), str(prod_name4), result4, Sdf)

    Subsave().savetoexcel5(path, num5, Name5, Index5, SubIndex5, str(ER5), str(prod_name5), result5, Sdf)

    Subsave().savetoexcel6(path, num6, Name6, Index6, SubIndex6, str(ER6), str(prod_name6), result6, Sdf)

    assert prod_name1 > 300 and prod_name1 < 350  # Compare the expected result with the actual result that generated by pytest

    assert prod_name2 > 400 and prod_name2 < 450

    assert prod_name4 == ER4

    assert prod_name5 == ER5

    assert prod_name6 == ER6

 

@pytest.mark.test_id(15563)  # 38

def test_TeachQ1_Offset(iolink_master):

    systemcommand = 2

    resetprod_name = iolink_master.write(130, systemcommand)

 

    num1 = 58  # which row to save the data

    Name1 = 'Teach-In Q1 Offset SP2'  # Name of the testcase

    Index1 = 60  # IO index

    SubIndex1 = 2

    ER1 = {1 > 300 or 1 < 350}  # Expected return result for SP2

 

    num2 = 59  # which row to save the data

    Name2 = 'Teach-In Q1 Offset SP1'  # Name of the testcase

    Index2 = 60  # IO index

    SubIndex2 = 1

    ER2 = {2 > 400 or 2 < 450}  # Expected return result for SP1

 

    num4 = 60

    Name4 = 'Teach-In Q1 Offset Status SP2'

    Index4 = 59

    SubIndex4 = 0

    ER4 = {1: True, 2: False, 3: 2}

 

    num5 = 61

    Name5 = 'Teach-In Q1 Offset Status SP1'

    Index5 = 59

    SubIndex5 = 0

    ER5 = {1: False, 2: True, 3: 1}  # Teacg flag SP2, Teach Flag SP1, Teach state

 

    num6 = 62

    Name6 = 'Teach-In Q1 Mode'

    Index6 = 61

    SubIndex6 = 2

    ER6 = 128

 

    teachchannel = 58

    channelprod_name = iolink_master.write(1, teachchannel)

    modeprod_name = iolink_master.write(128, Index6, SubIndex6)

    time.sleep(2)

    motor_turn.Teach_Turn(num1=32)

    sp2 = iolink_master.write(66, systemcommand)

    time.sleep(4)

    prod_name4 = iolink_master.read(Index4)

    time.sleep(2)

    motor_turn.Teach_Turn(num1=50)

    sp1 = iolink_master.write(65, systemcommand)

    time.sleep(4)

    prod_name5 = iolink_master.read(Index5)

    time.sleep(2)

    motor_turn.finalposition()

 

    prod_name1 = iolink_master.read(Index1, SubIndex1)

    prod_name2 = iolink_master.read(Index2, SubIndex2)

    prod_name6 = iolink_master.read(Index6, SubIndex6)

 

    if prod_name1 > 300 and prod_name1 < 350:

        result1 = "Passed"

    else:

        result1 = "Failed"

 

    if prod_name2 > 400 and prod_name2 < 450:

        result2 = 'Passed'

    else:

        result2 = 'Failed'

 

    if ER4 == prod_name4:

        result4 = 'Passed'

    else:

        result4 = 'Failed'

 

    if ER5 == prod_name5:

        result5 = 'Passed'

    else:

        result5 = 'Failed'

 

    if ER6 == prod_name6:

        result6 = 'Passed'

    else:

        result6 = 'Failed'

 

    Subsave().savetoexcel1(path, num1, Name1, Index1, SubIndex1, str(ER1), str(prod_name1), result1, Sdf)

    Subsave().savetoexcel2(path, num2, Name2, Index2, SubIndex2, str(ER2), str(prod_name2), result2, Sdf)

    Subsave().savetoexcel4(path, num4, Name4, Index4, SubIndex4, str(ER4), str(prod_name4), result4, Sdf)

    Subsave().savetoexcel5(path, num5, Name5, Index5, SubIndex5, str(ER5), str(prod_name5), result5, Sdf)

    Subsave().savetoexcel6(path, num6, Name6, Index6, SubIndex6, str(ER6), str(prod_name6), result6, Sdf)

    assert prod_name1 > 300 and prod_name1 < 350  # Compare the expected result with the actual result that generated by pytest

    assert prod_name2 > 400 and prod_name2 < 450

    assert prod_name4 == ER4

    assert prod_name5 == ER5

    assert prod_name6 == ER6

 

@pytest.mark.test_id(19410)  #39

def test_TeachQ2_Window(iolink_master):

    systemcommand = 2

    resetprod_name = iolink_master.write(130, systemcommand)

 

    num1 = 63  # which row to save the data

    Name1 = 'Teach-In Q2 Window SP2'  # Name of the testcase

    Index1 = 62  # IO index

    SubIndex1 = 2

    ER1 = {1 > 300 or 1 < 350}  # Expected return result for SP2

 

    num2 = 64  # which row to save the data

    Name2 = 'Teach-In Q2 Window SP1'  # Name of the testcase

    Index2 = 62  # IO index

    SubIndex2 = 1

    ER2 = {2 > 400 or 2 < 450}  # Expected return result for SP1

 

    num4 = 65

    Name4 = 'Teach-In Q2 Window Status SP2'

    Index4 = 59

    SubIndex4 = 0

    ER4 = {1: True, 2: False, 3: 2}

 

    num5 = 66

    Name5 = 'Teach-In Q2 Window Status SP1'

    Index5 = 59

    SubIndex5 = 0

    ER5 = {1: False, 2: True, 3: 1}  # Teacg flag SP2, Teach Flag SP1, Teach state

 

    num6 = 67

    Name6 = 'Teach-In Q2 Mode'

    Index6 = 63

    SubIndex6 = 2

    ER6 = 2

 

    teachchannel = 58

    channelprod_name = iolink_master.write(2, teachchannel)

    modeprod_name = iolink_master.write(2, Index6, SubIndex6)

    time.sleep(2)

    motor_turn.Teach_Turn(num1=32)

    sp2 = iolink_master.write(66, systemcommand)

    time.sleep(4)

    prod_name4 = iolink_master.read(Index4)

    time.sleep(2)

    motor_turn.Teach_Turn(num1=50)

    sp1 = iolink_master.write(65, systemcommand)

    time.sleep(4)

    prod_name5 = iolink_master.read(Index5)

    time.sleep(2)

    motor_turn.finalposition()

 

    prod_name1 = iolink_master.read(Index1, SubIndex1)

    prod_name2 = iolink_master.read(Index2, SubIndex2)

    prod_name6 = iolink_master.read(Index6, SubIndex6)

 

    if prod_name1 > 300 and prod_name1 < 350 :

        result1 = "Passed"

    else:

        result1 = "Failed"

 

    if prod_name2 > 400 and prod_name2 < 450:

        result2 = 'Passed'

    else:

        result2 = 'Failed'

 

    if ER4 == prod_name4:

        result4 = 'Passed'

    else:

        result4 = 'Failed'

 

    if ER5 == prod_name5:

        result5 = 'Passed'

    else:

        result5 = 'Failed'

 

    if ER6 == prod_name6:

        result6 = 'Passed'

    else:

        result6 = 'Failed'

 

    Subsave().savetoexcel1(path, num1, Name1, Index1, SubIndex1, str(ER1), str(prod_name1), result1, Sdf)

    Subsave().savetoexcel2(path, num2, Name2, Index2, SubIndex2, str(ER2), str(prod_name2), result2, Sdf)

    Subsave().savetoexcel4(path, num4, Name4, Index4, SubIndex4, str(ER4), str(prod_name4), result4, Sdf)

    Subsave().savetoexcel5(path, num5, Name5, Index5, SubIndex5, str(ER5), str(prod_name5), result5, Sdf)

    Subsave().savetoexcel6(path, num6, Name6, Index6, SubIndex6, str(ER6), str(prod_name6), result6, Sdf)

    assert prod_name1 > 300 and prod_name1 < 350  # Compare the expected result with the actual result that generated by pytest

    assert prod_name2 > 400 and prod_name2 < 450

    assert prod_name4 == ER4

    assert prod_name5 == ER5

    assert prod_name6 == ER6

 

# @pytest.mark.test_id()  # 40

def test_TeachQ2_Single(iolink_master):

    systemcommand = 2

    resetprod_name = iolink_master.write(130, systemcommand)

 

    num1 = 68  # which row to save the data

    Name1 = 'Teach-In Q2 Single SP2'  # Name of the testcase

    Index1 = 62  # IO index

    SubIndex1 = 2

    ER1 = {1 > 300 or 1 < 350}  # Expected return result for SP2

 

    num2 = 69  # which row to save the data

    Name2 = 'Teach-In Q2 Single SP1'  # Name of the testcase

    Index2 = 62  # IO index

    SubIndex2 = 1

    ER2 = {2 > 400 or 2 < 450}  # Expected return result for SP1

 

    num4 = 70

    Name4 = 'Teach-In Q2 Single Status SP2'

    Index4 = 59

    SubIndex4 = 0

    ER4 = {1: True, 2: False, 3: 2}

 

    num5 = 71

    Name5 = 'Teach-In Q2 Single Status SP1'

    Index5 = 59

    SubIndex5 = 0

    ER5 = {1: False, 2: True, 3: 1}  # Teacg flag SP2, Teach Flag SP1, Teach state

 

    num6 = 72

    Name6 = 'Teach-In Q2 Mode'

    Index6 = 63

    SubIndex6 = 2

    ER6 = 1

 

    teachchannel = 58

    channelprod_name = iolink_master.write(2, teachchannel)

    modeprod_name = iolink_master.write(1, Index6, SubIndex6)

    time.sleep(2)

    motor_turn.Teach_Turn(num1=32)

    sp2 = iolink_master.write(66, systemcommand)

    time.sleep(4)

    prod_name4 = iolink_master.read(Index4)

    time.sleep(2)

    motor_turn.Teach_Turn(num1=50)

    sp1 = iolink_master.write(65, systemcommand)

    time.sleep(4)

    prod_name5 = iolink_master.read(Index5)

    time.sleep(2)

    motor_turn.finalposition()

 

    prod_name1 = iolink_master.read(Index1, SubIndex1)

    prod_name2 = iolink_master.read(Index2, SubIndex2)

    prod_name6 = iolink_master.read(Index6, SubIndex6)

 

    if prod_name1 > 300 and prod_name1 < 350:

        result1 = "Passed"

    else:

        result1 = "Failed"

 

    if prod_name2 > 400 and prod_name2 < 450:

        result2 = 'Passed'

    else:

        result2 = 'Failed'

 

    if ER4 == prod_name4:

        result4 = 'Passed'

    else:

        result4 = 'Failed'

 

    if ER5 == prod_name5:

        result5 = 'Passed'

    else:

        result5 = 'Failed'

 

    if ER6 == prod_name6:

        result6 = 'Passed'

    else:

        result6 = 'Failed'

 

    Subsave().savetoexcel1(path, num1, Name1, Index1, SubIndex1, str(ER1), str(prod_name1), result1, Sdf)

    Subsave().savetoexcel2(path, num2, Name2, Index2, SubIndex2, str(ER2), str(prod_name2), result2, Sdf)

    Subsave().savetoexcel4(path, num4, Name4, Index4, SubIndex4, str(ER4), str(prod_name4), result4, Sdf)

    Subsave().savetoexcel5(path, num5, Name5, Index5, SubIndex5, str(ER5), str(prod_name5), result5, Sdf)

    Subsave().savetoexcel6(path, num6, Name6, Index6, SubIndex6, str(ER6), str(prod_name6), result6, Sdf)

    assert prod_name1 > 300 and prod_name1 < 350  # Compare the expected result with the actual result that generated by pytest

    assert prod_name2 > 400 and prod_name2 < 450

    assert prod_name4 == ER4

    assert prod_name5 == ER5

    assert prod_name6 == ER6

 

# @pytest.mark.test_id()  # 41

def test_TeachQ2_Offset(iolink_master):

    systemcommand = 2

    resetprod_name = iolink_master.write(130, systemcommand)

 

    num1 = 73  # which row to save the data

    Name1 = 'Teach-In Q2 Offset SP2'  # Name of the testcase

    Index1 = 62  # IO index

    SubIndex1 = 2

    ER1 = {1 > 300 or 1 < 350}  # Expected return result for SP2

 

    num2 = 74  # which row to save the data

    Name2 = 'Teach-In Q2 Offset SP1'  # Name of the testcase

    Index2 = 62  # IO index

    SubIndex2 = 1

    ER2 = {2 > 400 or 2 < 450}  # Expected return result for SP1

 

    num4 = 75

    Name4 = 'Teach-In Q2 Offset Status SP2'

    Index4 = 59

    SubIndex4 = 0

    ER4 = {1: True, 2: False, 3: 2}

 

    num5 = 76

    Name5 = 'Teach-In Q2 Offset Status SP1'

    Index5 = 59

    SubIndex5 = 0

    ER5 = {1: False, 2: True, 3: 1}  # Teacg flag SP2, Teach Flag SP1, Teach state

 

    num6 = 77

    Name6 = 'Teach-In Q2 Mode'

    Index6 = 63

    SubIndex6 = 2

    ER6 = 128

 

    teachchannel = 58

    channelprod_name = iolink_master.write(2, teachchannel)

    modeprod_name = iolink_master.write(128, Index6, SubIndex6)

    time.sleep(2)

    motor_turn.Teach_Turn(num1=32)

    sp2 = iolink_master.write(66, systemcommand)

    time.sleep(4)

    prod_name4 = iolink_master.read(Index4)

    time.sleep(2)

    motor_turn.Teach_Turn(num1=50)

    sp1 = iolink_master.write(65, systemcommand)

    time.sleep(4)

    prod_name5 = iolink_master.read(Index5)

    time.sleep(2)

    motor_turn.finalposition()

 

    prod_name1 = iolink_master.read(Index1, SubIndex1)

    prod_name2 = iolink_master.read(Index2, SubIndex2)

    prod_name6 = iolink_master.read(Index6, SubIndex6)

 

    if prod_name1 > 300 and prod_name1 < 350:

        result1 = "Passed"

    else:

        result1 = "Failed"

 

    if prod_name2 > 400 and prod_name2 < 450:

        result2 = 'Passed'

    else:

        result2 = 'Failed'

 

    if ER4 == prod_name4:

        result4 = 'Passed'

    else:

        result4 = 'Failed'

 

    if ER5 == prod_name5:

        result5 = 'Passed'

    else:

        result5 = 'Failed'

 

    if ER6 == prod_name6:

        result6 = 'Passed'

    else:

        result6 = 'Failed'

 

    Subsave().savetoexcel1(path, num1, Name1, Index1, SubIndex1, str(ER1), str(prod_name1), result1, Sdf)

    Subsave().savetoexcel2(path, num2, Name2, Index2, SubIndex2, str(ER2), str(prod_name2), result2, Sdf)

    Subsave().savetoexcel4(path, num4, Name4, Index4, SubIndex4, str(ER4), str(prod_name4), result4, Sdf)

    Subsave().savetoexcel5(path, num5, Name5, Index5, SubIndex5, str(ER5), str(prod_name5), result5, Sdf)

    Subsave().savetoexcel6(path, num6, Name6, Index6, SubIndex6, str(ER6), str(prod_name6), result6, Sdf)

    assert prod_name1 > 300 and prod_name1 < 350  # Compare the expected result with the actual result that generated by pytest

    assert prod_name2 > 400 and prod_name2 < 450

    assert prod_name4 == ER4

    assert prod_name5 == ER5

    assert prod_name6 == ER6

 

@pytest.mark.test_id(19411)  #42

def test_TeachQa(iolink_master):

 

    systemcommand = 2

    resetprod_name = iolink_master.write(130, systemcommand)

 

    num1 = 78                                    # which row to save the data

    Name1 = 'Teach-In Qa SP1'                        # Name of the testcase

    Index1 =  160                                 # IO index

    SubIndex1 = 1

    ER1 = {1>310 or 1<350}          # Expected return result for SP1

 

    num2 = 79

    Name2 = 'Teach-In Qa Status'

    Index2 = 59

    SubIndex2 = 0

    ER2 = {1: True, 2: False, 3: 1}

 

 

    teachchannel = 58

    channelprod_name = iolink_master.write(3, teachchannel)

    time.sleep(2)

    motor_turn.Teach_Turn(num1=31)

    sp1 = iolink_master.write(65, systemcommand)

    time.sleep(4)

    prod_name2 = iolink_master.read(Index2)

    time.sleep(2)

    motor_turn.finalposition()

 

    prod_name1 = iolink_master.read(Index1,SubIndex1)

 

 

    if  prod_name1 >310 and prod_name1<350:

        result1 = "Passed"

    else:

        result1 = "Failed"

 

    if ER2 == prod_name2:

        result2 = 'Passed'

    else:

        result2 = 'Failed'

 

    Subsave().savetoexcel1(path, num1, Name1, Index1, SubIndex1, str(ER1), str(prod_name1), result1, Sdf)

    Subsave().savetoexcel2(path, num2, Name2, Index2, SubIndex2, str(ER2), str(prod_name2), result2, Sdf)

    assert prod_name1 >310 and prod_name1<350     #Compare the expected result with the actual result that generated by pytest

    assert prod_name2 == ER2

 

print("=======================Continue with SICK Device Specific Identities Checking=============================================")

# @pytest.mark.test_id(15570)  #43

def test_Device_Specific_Tag(iolink_master):

    systemcommand = 2

    resetprod_name = iolink_master.write(130, systemcommand)

 

    num1 = 80

    Name1 = 'Device Specific Tag Read'

    Index1 = 64

    SubIndex1 = 0

    ER1 = '***'

 

    num2 = 81

    Name2 = 'Device Specific Tag Write'

    Index2 = 64

    SubIndex2 = 0

    ER2 = '***'

 

    prod_name1 = iolink_master.read(Index1)

    prod_name2 = iolink_master.write('***', Index2)

    prod_name2 = iolink_master.read(Index2)

    # prod_name = iolink_master.read("Product Name")

    Rname1 = prod_name1.rstrip(" ")

 

    if ER1 == Rname1:

        result1 = "Passed"

    else:

        result1 = "Failed"

 

    if ER2 == prod_name2:

        result2 = "Passed"

    else:

        result2 = "Failed"

 

    Subsave().savetoexcel1(path, num1, Name1, Index1, SubIndex1, ER1, Rname1, result1,

                           Sdf)  # save all the data in excel

    Subsave().savetoexcel2(path, num2, Name2, Index2, SubIndex2, str(ER2), str(prod_name2), result2, Sdf)

    assert Rname1 == ER1

    assert prod_name2 == ER2

 

@pytest.mark.test_id(15570)  #44

def test_User_Tag1(iolink_master):

 

    systemcommand = 2

    resetprod_name = iolink_master.write(130, systemcommand)

 

    num1 = 82

    Name1 = 'User Tag1 Read'

    Index1 = 84

    SubIndex1 = 0

    ER1 = '***'

 

    num2 = 83

    Name2 = 'User Tag1 Write'

    Index2 = 84

    SubIndex2 = 0

    ER2 = '***'

 

    prod_name1 = iolink_master.read(Index1)

    prod_name2 = iolink_master.write('***', Index2)

    time.sleep(3)

    prod_name2 = iolink_master.read(Index2)

    time.sleep(3)

    # prod_name = iolink_master.read("Product Name")

    # Rname1 = prod_name1.rstrip(" ")

 

    if ER1 == prod_name1:

        result1 = "Passed"

    else:

        result1 = "Failed"

 

    if ER2 == prod_name2:

        result2 = "Passed"

    else:

        result2 = "Failed"

 

    Subsave().savetoexcel1(path, num1, Name1, Index1, SubIndex1, ER1, str(prod_name1), result1,

                           Sdf)  # save all the data in excel

    Subsave().savetoexcel2(path, num2, Name2, Index2, SubIndex2, str(ER2), str(prod_name2), result2, Sdf)

    assert prod_name1 == ER1

    assert prod_name2 == ER2

 

# @pytest.mark.test_id(15570)  #45

def test_User_Tag2(iolink_master):

    systemcommand = 2

    resetprod_name = iolink_master.write(130, systemcommand)

 

    num1 = 84

    Name1 = 'User Tag2 Read'

    Index1 = 85

    SubIndex1 = 0

    ER1 = '***'

 

    num2 = 85

    Name2 = 'User Tag2 Write'

    Index2 = 85

    SubIndex2 = 0

    ER2 = '***'

 

    prod_name1 = iolink_master.read(Index1)

    prod_name2 = iolink_master.write('***', Index2)

    time.sleep(3)

    prod_name2 = iolink_master.read(Index2)

    time.sleep(3)

    # prod_name = iolink_master.read("Product Name")

    # Rname1 = prod_name1.rstrip(" ")

 

    if ER1 == prod_name1:

        result1 = "Passed"

    else:

        result1 = "Failed"

 

    if ER2 == prod_name2:

        result2 = "Passed"

    else:

        result2 = "Failed"

 

    Subsave().savetoexcel1(path, num1, Name1, Index1, SubIndex1, ER1, str(prod_name1), result1,

                           Sdf)  # save all the data in excel

    Subsave().savetoexcel2(path, num2, Name2, Index2, SubIndex2, str(ER2), str(prod_name2), result2, Sdf)

    assert prod_name1 == ER1

    assert prod_name2 == ER2

 

# @pytest.mark.test_id()   #46

def test_SenderConfig_Laser_ON(iolink_master):

    systemcommand = 2

    resetprod_name = iolink_master.write(130, systemcommand)

 

    num1 = 86

    Name1 = "Sender Configuration"

    Index1 = 97

    SubIndex1 = 0

    ER1 = 0

 

    num2 = 87  # which row to save the data

    Name2 = 'Sender Config Laser ON Q1 SP1'  # Name of the testcase

    Index2 = 109  # IO index

    SubIndex2 = 0

    ER2 = ('3230<DIST2<3310')

 

 

    laserOnprod_name = iolink_master.write(0, Index1)

    time.sleep(2)

    motor_turn.Teach_Turn(num1=32)

    prod_name2 = iolink_master.read(Index2)   # READ the index and it wil produce data in dixtionary

    prod_name2 = list(prod_name2.items())     # convert the dictionary into array/list

    prod_name2 = prod_name2[0]                # extract the required data (distacne value)

    prod_name2 = prod_name2[1]                # output = (1, distance value) , extract only the distance value from the list so that

                                              # so that i can do create a range of distance and make comparision

 

    time.sleep(1)

    motor_turn.finalposition()

 

    prod_name1 = iolink_master.read(Index1)

 

    if ER1 == prod_name1:

        result1 = "Passed"

    else:

        result1 = "Failed"

 

    if prod_name2 > 3230 and prod_name2 < 3310:     # expected range of distance, +/- 0.003meter

        result2 = "Passed"

    else:

        result2 = "Failed"

 

    Subsave().savetoexcel1(path, num1, Name1, Index1, SubIndex1, str(ER1), str(prod_name1), result1, Sdf)

    Subsave().savetoexcel2(path, num2, Name2, Index2, SubIndex2, str(ER2), str(prod_name2), result2, Sdf)

 

    assert prod_name1 == ER1

    assert prod_name2 > 3230 and prod_name2 < 3310     #compare the actual distaance with the expected range of dist.

                                                    # test case pass if the actual distance is captured within the expected range of dist

 

# @pytest.mark.test_id()   #47

def test_SenderConfig_Laser_OFF(iolink_master):

 

    systemcommand = 2

    resetprod_name = iolink_master.write(130, systemcommand)

 

    num1 = 88

    Name1 = "Sender Configuration"

    Index1 = 97

    SubIndex1 = 0

    ER1 = 1

 

    num2 = 89  # which row to save the data

    Name2 = 'Sender Config Laser Off Q1 SP1'  # Name of the testcase

    Index2 = 109  # IO index

    SubIndex2 = 0

    ER2 = {'920<DIST2<1000'}

 

    laserOFFprod_name = iolink_master.write(1, Index1)      #LASER OFF

    time.sleep(2)

    motor_turn.Teach_Turn(num1=30)

    prod_name2 = iolink_master.read(Index2)

    prod_name2 = list(prod_name2.items())

    prod_name2 = prod_name2[0]

    prod_name2 = prod_name2[1]

    time.sleep(8)

    motor_turn.finalposition()

 

    prod_name1 = iolink_master.read(Index1)

 

    if ER1 == prod_name1:

        result1 = "Passed"

    else:

        result1 = "Failed"

 

    if prod_name2 > 920 and prod_name2 < 1000:

        result2 = "Passed"

    else:

        result2 = "Failed"

 

    Subsave().savetoexcel1(path, num1, Name1, Index1, SubIndex1, str(ER1), str(prod_name1), result1, Sdf)

    Subsave().savetoexcel2(path, num2, Name2, Index2, SubIndex2, str(ER2), str(prod_name2), result2, Sdf)

    assert prod_name1 == ER1  # Compare the expected result with the actual result that generated by pytest

    assert prod_name2 > 920 and prod_name2 < 1000

 

# @pytest.mark.test_id(15570)  #48

def test_SICK_Profile_Version(iolink_master):

    systemcommand = 2

    resetprod_name = iolink_master.write(130, systemcommand)

 

    num1 = 90

    Name1 = 'SICK Profile Version'

    Index1 = 205

    SubIndex1 = 0

    ER1 = '1.01'

 

    prod_name1 = iolink_master.read(Index1)

 

    # prod_name = iolink_master.read("Product Name")

    Rname1 = prod_name1.rstrip(" ")

 

    if ER1 == Rname1:

        result1 = "Passed"

    else:

        result1 = "Failed"

 

    Subsave().savetoexcel1(path, num1, Name1, Index1, SubIndex1, ER1, Rname1, result1,

                           Sdf)  # save all the data in excel

 

    assert Rname1 == ER1

 

# @pytest.mark.test_id(15570)  #49

def test_Display_Language(iolink_master):

    systemcommand = 2

    resetprod_name = iolink_master.write(130, systemcommand)

 

    num1 = 91

    Name1 = 'Display Default Language'

    Index1 = 234

    SubIndex1 = 2

    ER1 = 1

 

    num2 = 92

    Name2 = 'Display Language German'

    Index2 = 234

    SubIndex2 = 2

    ER2 = 2

 

    num4 = 93

    Name4 = 'Display Language English'

    Index4 = 234

    SubIndex4 = 2

    ER4 = 1

 

    prod_name1 = iolink_master.read(Index1, SubIndex2)

    prod_name2 = iolink_master.write(2, Index2, SubIndex2)      #write german

    prod_name2 = iolink_master.read(Index2, SubIndex2)

    prod_name4 = iolink_master.write(1, Index4, SubIndex4)      #write english

    prod_name4 = iolink_master.read(Index4,SubIndex4)

 

    if ER1 == prod_name1:

        result1 = "Passed"

    else:

        result1 = "Failed"

 

    if ER2 == prod_name2:

        result2 = "Passed"

    else:

        result2 = "Failed"

 

    if ER4 == prod_name4:

        result4 = "Passed"

    else:

        result4 = "Failed"

 

    Subsave().savetoexcel1(path, num1, Name1, Index1, SubIndex1, ER1, str(prod_name1), result1,

                           Sdf)  # save all the data in excel

    Subsave().savetoexcel2(path, num2, Name2, Index2, SubIndex2, str(ER2), str(prod_name2), result2, Sdf)

    Subsave().savetoexcel4(path, num4, Name4, Index4, SubIndex4, str(ER4), str(prod_name4), result4, Sdf)

    assert prod_name1 == ER1

    assert prod_name2 == ER2

    assert prod_name4 == ER4

 

# @pytest.mark.test_id(15570)  #50

def test_Find_Me(iolink_master):

    systemcommand = 2

    resetprod_name = iolink_master.write(130, systemcommand)

 

    num1 = 94

    Name1 = 'Find Me Default'

    Index1 = 204

    SubIndex1 = 0

    ER1 = 0

 

    num2 = 95

    Name2 = 'Find Me On'

    Index2 = 204

    SubIndex2 = 0

    ER2 = 1

 

    num4 = 96

    Name4 = 'Find Me Off'

    Index4 = 204

    SubIndex4 = 0

    ER4 = 0

 

    prod_name1 = iolink_master.read(Index1, SubIndex2)

    prod_name2 = iolink_master.write(1, Index2, SubIndex2)

    prod_name2 = iolink_master.read(Index2, SubIndex2)

    prod_name4 = iolink_master.write(0, Index4, SubIndex4)

    prod_name4 = iolink_master.read(Index4,SubIndex4)

 

    if ER1 == prod_name1:

        result1 = "Passed"

    else:

        result1 = "Failed"

 

    if ER2 == prod_name2:

        result2 = "Passed"

    else:

        result2 = "Failed"

 

    if ER4 == prod_name4:

        result4 = "Passed"

    else:

        result4 = "Failed"

 

    Subsave().savetoexcel1(path, num1, Name1, Index1, SubIndex1, ER1, str(prod_name1), result1,

                           Sdf)  # save all the data in excel

    Subsave().savetoexcel2(path, num2, Name2, Index2, SubIndex2, str(ER2), str(prod_name2), result2, Sdf)

    Subsave().savetoexcel4(path, num4, Name4, Index4, SubIndex4, str(ER4), str(prod_name4), result4, Sdf)

    assert prod_name1 == ER1

    assert prod_name2 == ER2

    assert prod_name4 == ER4

 

# @pytest.mark.test_id(15570)  #51

def test_Cycle_Time(iolink_master):

    systemcommand = 2

    resetprod_name = iolink_master.write(130, systemcommand)

 

    num1 = 97

    Name1 = 'Cycle Time Default'

    Index1 = 4368

    SubIndex1 = 0

    ER1 = 33

 

    num2 = 98

    Name2 = '50ms Cycle Time'

    Index2 = 4368

    SubIndex2 = 0

    ER2 = 50

 

    num4 = 99

    Name4 = '100ms Cycle Time'

    Index4 = 4368

    SubIndex4 = 0

    ER4 = 100

 

    num5 = 100

    Name5 = '200ms Cycle Time'

    Index5 = 4368

    SubIndex5 = 0

    ER5 = 200

 

    num6 = 101

    Name6 = '3000ms Cycle Time'

    Index6 = 4368

    SubIndex6 = 0

    ER6 = 3000

 

    prod_name1 = iolink_master.read(Index1, SubIndex2)

    prod_name2 = iolink_master.write(50, Index2)

    prod_name2 = iolink_master.read(Index2)

    prod_name4 = iolink_master.write(100, Index4)

    prod_name4 = iolink_master.read(Index4)

    prod_name5 = iolink_master.write(200, Index5)

    prod_name5 = iolink_master.read(Index5)

    prod_name6 = iolink_master.write(3000,Index6)

    prod_name6 = iolink_master.read(Index6)

 

    if ER1 == prod_name1:

        result1 = "Passed"

    else:

        result1 = "Failed"

 

    if ER2 == prod_name2:

        result2 = "Passed"

    else:

        result2 = "Failed"

 

    if ER4 == prod_name4:

        result4 = "Passed"

    else:

        result4 = "Failed"

 

    if ER5 == prod_name5:

        result5 = 'Passed'

    else:

        result5 = 'Failed'

 

    if ER6 == prod_name6:

        result6 = 'Passed'

    else:

        result6 = 'Failed'

 

    Subsave().savetoexcel1(path, num1, Name1, Index1, SubIndex1, str(ER1), str(prod_name1), result1, Sdf)

    Subsave().savetoexcel2(path, num2, Name2, Index2, SubIndex2, str(ER2), str(prod_name2), result2, Sdf)

    Subsave().savetoexcel4(path, num4, Name4, Index4, SubIndex4, str(ER4), str(prod_name4), result4, Sdf)

    Subsave().savetoexcel5(path, num5, Name5, Index5, SubIndex5, str(ER5), str(prod_name5), result5, Sdf)

    Subsave().savetoexcel6(path, num6, Name6, Index6, SubIndex6, str(ER6), str(prod_name6), result6, Sdf)

 

    assert prod_name1 == ER1

    assert prod_name2 == ER2

    assert prod_name4 == ER4

    assert prod_name5 == ER5

    assert prod_name6 == ER6

 

# @pytest.mark.test_id(15570)  #52

def test_33ms_CycleTime(iolink_master):

    systemcommand = 2

    resetprod_name = iolink_master.write(130, systemcommand)

 

    num1 = 102

    Name1 = '33ms Cycle Time'

    Index1 = 4368

    SubIndex1 = 0

    ER1 = 33

 

    prod_name1 = iolink_master.write(33, Index1)

    prod_name1 = iolink_master.read(Index1)

 

    if ER1 == prod_name1:

        result1 = "Passed"

    else:

        result1 = "Failed"

 

    Subsave().savetoexcel1(path, num1, Name1, Index1, SubIndex1, str(ER1), str(prod_name1), result1, Sdf)

 

    assert prod_name1 == ER1

 

# @pytest.mark.test_id(15570)  #53

def test_Firmware_Verification(iolink_master):

    systemcommand = 2

    resetprod_name = iolink_master.write(130, systemcommand)

 

    num1 = 103

    Name1 = 'Firmware Verification'

    Index1 = 4534

    SubIndex1 = 0

    ER1 = {1: '0000-0000-0000-0000', 2: '2015/01/01 00:00:00'}

 

    prod_name1 = iolink_master.read(Index1)

 

    if ER1 == prod_name1:

        result1 = "Passed"

    else:

        result1 = "Failed"

 

    Subsave().savetoexcel1(path, num1, Name1, Index1, SubIndex1, str(ER1), str(prod_name1), result1, Sdf)

 

    assert prod_name1 == ER1

 

 

print("=======================Continue Pin5 MF Function =============================================")

#

# # @pytest.mark.test_id(15497)

# def test_deactivate_Input(iolink_master):

#     SEQUENCE_IN_LOAD()

#     systemcommand = 2

#     resetprod_name = iolink_master.write(130, systemcommand)

#

#     num1 = 73                                     # which row to save the data

#     Name1 = 'Deactivate Input'                    # Name of the testcase

#     Index1 =  122                                 # IO index

#     SubIndex1 = 0

#     ER1 = 0                               # Expected return result

#

#     prod_name1 = iolink_master.write(0,Index1)       #for the IO link index

#

#     if ER1 == prod_name1:

#         result1 = "Passed"

#     else:

#         result1 = "Failed"

#

#     Subsave().savetoexcel1(path, num1, Name1, Index1, SubIndex1, ER1,  prod_name1, result1 , Sdf)  # save all the data in excel

#     assert  prod_name1 == ER1

#

# # @pytest.mark.test_id(15497)

# def test_SenderOff_Input(iolink_master):

#     SEQUENCE_IN_LOAD()

#

#     systemcommand = 2

#     resetprod_name = iolink_master.write(130, systemcommand)

#

#     num1 = 74                                     # which row to save the data

#     Name1 = 'SenderOff Input'                        # Name of the testcase

#     Index1 =  122                                 # IO index

#     SubIndex1 = 0

#     ER1 = 16                             # Expected return result

#

#     prod_name1 = iolink_master.write(16,Index1)       #for the IO link index

#

#     if ER1 == prod_name1:

#         result1 = "Passed"

#     else:

#         result1 = "Failed"

#

#     Subsave().savetoexcel1(path, num1, Name1, Index1, SubIndex1, ER1,  prod_name1, result1 , Sdf)  # save all the data in excel

#     assert  prod_name1 == ER1

#

# # @pytest.mark.test_id(15497)

# def test_Dist_Preset_Input(iolink_master):

#     SEQUENCE_IN_LOAD()

#

#     systemcommand = 2

#     resetprod_name = iolink_master.write(130, systemcommand)

#

#     num1 = 75                                     # which row to save the data

#     Name1 = 'Distance Preset Input'                        # Name of the testcase

#     Index1 =  122                                 # IO index

#     SubIndex1 = 0

#     ER1 = 17                             # Expected return result

#

#     prod_name1 = iolink_master.write(17,Index1)       #for the IO link index

#

#     if ER1 == prod_name1:

#         result1 = "Passed"

#     else:

#         result1 = "Failed"

#

#     Subsave().savetoexcel1(path, num1, Name1, Index1, SubIndex1, ER1,  prod_name1, result1 , Sdf)  # save all the data in excel

#     assert  prod_name1 == ER1

#

# # @pytest.mark.test_id(15497)

# def test_Pin5_Default_Input(iolink_master):

#     SEQUENCE_IN_LOAD()

#

#     systemcommand = 2

#     resetprod_name = iolink_master.write(130, systemcommand)

#

#     num1 = 76                                     # which row to save the data

#     Name1 = 'Pin5 Default Input'                        # Name of the testcase

#     Index1 =  122                                 # IO index

#     SubIndex1 = 0

#     ER1 = 0                             # Expected return result

#

#     prod_name1 = iolink_master.read(Index1)       #for the IO link index

#

#     if ER1 == prod_name1:

#         result1 = "Passed"

#     else:

#         result1 = "Failed"

#

#     Subsave().savetoexcel1(path, num1, Name1, Index1, SubIndex1, ER1,  prod_name1, result1 , Sdf)  # save all the data in excel

