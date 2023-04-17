"""Provides a scripting component.
    Inputs:
        x: The x script variable
        y: The y script variable
    Output:
        a: The a output variable"""

__author__ = "Dor"
__version__ = "2021.03.14"

import rhinoscriptsyntax as rs
import scriptcontext as sc
import Rhino as rh
import math

# set scriptcontext.doc to Rhino.ActiveDoc
sc.doc = rh.RhinoDoc.ActiveDoc

### claculate number of new units

listLen = len(floorArea)

core = 45
if floorNum > 10:
    core = 125

buildingTotalArea =[]
netAreas = []
newUnitsNum = []

for i in range(listLen):
    area = floorNum*floorArea[i]
    buildingTotalArea.append(area)

mmdList = []



for i in range(len(buildingTotalArea)):
    
    ### very ugly code
    plot_objs = rs.ObjectsByLayer("H0010A")
    building_center_pt = ghdoc.Objects.FindGeometry(buildings[0]).GetBoundingBox(True).Center
    for plot_obj in plot_objs:
        if rs.PointInPlanarClosedCurve(building_center_pt, plot_obj):
            oldUnitsNum[i] = int(rs.GetUserText(plot_obj, "NUM_APTS_C"))
    ### very ugly code


    mmd = oldUnitsNum[i]*12
    mmdList.append(mmd)
    net = int(buildingTotalArea[i])-(floorNum*core)-mmdList[i]
    netAreas.append(net)


for i in range(listLen):
    num = netAreas[i]/unitAverageSize 
    newUnitsNum.append(int(num))

##############################################################################

### claculta income

salePrice = 25000
averagePrice = unitAverageSize*salePrice

income =[]

for i in range(listLen):
    totalPrice = newUnitsNum[i]*averagePrice
    income.append(totalPrice)

##############################################################################

### calculate outcome

buildingTime = 24
rent = 6000
housingCost = []

for i in range(listLen):
    ### very ugly code
    plot_objs = rs.ObjectsByLayer("H0010A")
    building_center_pt = ghdoc.Objects.FindGeometry(buildings[0]).GetBoundingBox(True).Center
    for plot_obj in plot_objs:
        if rs.PointInPlanarClosedCurve(building_center_pt, plot_obj):
            oldUnitsNum[i] = int(rs.GetUserText(plot_obj, "NUM_APTS_C"))             
    ### very ugly code
    
    cost = oldUnitsNum[i]*buildingTime*rent
    housingCost.append(cost)
    #print len(oldUnitsNum)

outcome = []
resedntialCost = []
basementCost =[]
buildingCost = []

#resedntialCost
for i in range(listLen):
    cost = buildingTotalArea[i]*5500
    resedntialCost.append(cost)
#basementCost
for i in range(listLen):
    cost = newUnitsNum[i]*45*3000
    basementCost.append(cost)
#buildingCost
for i in range(listLen):
    cost = resedntialCost[i] + basementCost[i]
    buildingCost.append(cost)

#outcome
for i in range(listLen):
    cost = (buildingCost[i]*1.3)+housingCost[i]
    outcome.append(int(cost))

#(( buildingTotalArea*5500 + newUnitsNum*45*3000 ) *1.3 + housingCost


##############################################################################

### test profit

Pass = []
Fail =[]

for i in range(listLen):
    
    profit = round(income[i]/outcome[i],2)
    
    
    if income[i]/outcome[i] > 1.2:
        
        Pass.append(buildings[i])
    else:
        
        Fail.append(buildings[i])