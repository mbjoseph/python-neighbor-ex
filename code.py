import arcpy, numpy
import os
from arcpy import env
from arcpy.sa import *
import sys
# in code baraye test 2 ke shamel chand ta raster kochak bud ok hast
import numpy as np
from time import clock
start = clock()

sys.path.append(r"C:\Program Files (x86)\Arcgis\Desktop10.3\arcpy")

sys.path.append(r"C:\Program Files (x86)\Arcgis\Desktop10.3\Bin")

env.overwriteOutput=True
#
#env.overwriteOutput = True
arcpy.CheckOutExtension("Spatial")

arcpy.env.workspace = r"C:\Colorado University\Fire point-Emily\2013\otherpoints"
OutData=r"C:\Colorado University\Fire point-Emily\2013\otherpoints"
#if arcpy.Exists( "x5.tif"):
#         arcpy.Delete_management ("x5.tif")

#inputData= r"C:\test\large\Large_raster1.tif"
Tempo=9
Spatio=3
#path= r"C:\test\large"
#arcpy.env.workspace = r"C:\Colorado University\Fall 2015\Fire Project\Adam\MCD64_2007\extractedby10000m"
#if arcpy.Exists( "aa.tif"):
#         arcpy.Delete_management ("aa.tif")
         
         
         
def RasterToArr( path, infile):
    arcpy.CheckOutExtension("Spatial")
    arcpy.env.workspace = path
    arcpy.env.overwriteOutput = 1
    ftc = arcpy.sa.Raster(infile)
    ftc.height 
    ftc.width 
    cellSize = ftc.meanCellHeight
    llpnt = ftc.extent.lowerLeft
    spref = ftc.spatialReference
    myArr = arcpy.RasterToNumPyArray(ftc).astype(float)
    return myArr,llpnt,cellSize,spref



def arrToRaster(resArray,llpnt,cellSize,spref,name1,name2,a): 
    finalRast = arcpy.NumPyArrayToRaster(resArray,llpnt,cellSize,cellSize)
    arcpy.DefineProjection_management(finalRast,spref)
#    arcpy.env._environments=OutData
#    finalRast.save('T'+str(name1)+'_S'+str(name2)+"_"+str(a)) # T means temporal criteria and S means Spatial criteria
#    finalRast.save('T'+str(name1)+'_S'+str(name2)+"_"+str(a))
    finalRast2 = SetNull(finalRast, finalRast, "VALUE < 1") 
    finalRast2.save('T'+str(name1)+'_S'+str(name2)+"_"+str(a))
    return finalRast2
# *********************************


 

def my_func(curRow, curCol, i, step1=1, step2=2, step3=3):
#def my_func(curRow, curCol, i, step1=1):

    if i == 0:
        return curRow - step1, curCol - step1
    if i == 1:
        return curRow - step1, curCol
    if i == 2:
        return curRow - step1, curCol+1
    if i == 3:
        return curRow , curCol+step1
    if i == 4:
        return curRow+step1 , curCol+step1
    if i == 5:
        return curRow+step1 , curCol
    if i == 6:
        return curRow+step1 , curCol-step1
    if i == 7:
        return curRow , curCol-step1
  
    if i == 8:

        return curRow-step2 , curCol-step2

    if i == 9:

        return curRow - step1, curCol - step2

    if i == 10:

        return curRow, curCol-step2

    if i == 11:

        return curRow + step1, curCol-step2

    if i == 12:

        return curRow + step2 , curCol-step2

    if i == 13:

        return curRow+step2 , curCol-step1

    if i == 14:

        return curRow+step2 , curCol

    if i == 15:

        return curRow+step2 , curCol+step1

    if i == 16:

        return curRow+step2 , curCol+step2

    if i == 17:
        return curRow+step1 , curCol+step2
    if i == 18:

        return curRow , curCol+step2

    if i == 19:
        return curRow-step1 , curCol+step2

    if i == 20:

        return curRow-step2 , curCol+step2

    if i == 21:

        return curRow-step2 , curCol+step1

    if i == 22:

        return curRow-step2 , curCol
   
    if i == 23:

        return curRow-step2 , curCol-step1

    if i == 24:

        return curRow - step3, curCol - step3

    if i == 25:

        return curRow - step3, curCol-step2

    if i == 26:

        return curRow - step3, curCol-step1

    if i == 27:

        return curRow-step3 , curCol

    if i == 28:

        return curRow-step3 , curCol+step1

    if i == 29:

        return curRow-step3 , curCol+step2

    if i == 30:

        return curRow-step3 , curCol+step3

    if i == 31:

        return curRow-step2 , curCol+step3
   
    if i == 32:

        return curRow-step1 , curCol+step3

    if i == 33:

        return curRow , curCol +step3

    if i == 34:

        return curRow+step1, curCol+step3

    if i == 35:

        return curRow + step2, curCol+step3

    if i == 36:

        return curRow + step3 , curCol+step3

    if i == 37:

        return curRow+step3 , curCol+step2

    if i == 38:

        return curRow+step3 , curCol+step1

    if i == 39:

        return curRow+step3, curCol

    if i == 40:

        return curRow+step3 , curCol-step1
   
    if i == 41:

        return curRow+step3 , curCol-step2
    if i == 42:

        return curRow+step3 , curCol-step3

    if i == 43:

        return curRow+step2 , curCol-step3

    if i == 44:

        return curRow+step1 , curCol-step3

    if i == 45:

        return curRow , curCol-step3

    if i == 46:

        return curRow-step1 , curCol-step3
   
    if i == 47:

        return curRow-step2 , curCol-step3
        
    


       
def main_fun(curRow, curCol, rstArray, outArray, fireClass, Spatio):
    
   if Spatio==3:
#    if Spatio==1:    # if user 3 for patial paratemers
       try: # this try handle the out of index problem

        value = [0]*49
#        value = [0]*9

        value[0] = rstArray.item(curRow, curCol)
        value[1] = rstArray.item(curRow-1, curCol-1)
        value[2] = rstArray.item(curRow-1, curCol)
        value[3] = rstArray.item(curRow-1, curCol+1)
        value[4] = rstArray.item(curRow, curCol+1)
        value[5] = rstArray.item(curRow+1, curCol+1)
        value[6] = rstArray.item(curRow+1, curCol)
        value[7] = rstArray.item(curRow+1, curCol-1)
        value[8] = rstArray.item(curRow, curCol-1)
        value[9] = rstArray.item(curRow-2, curCol-2)
        value[10] = rstArray.item(curRow-1, curCol-2)
        value[11] = rstArray.item(curRow, curCol-2)
        value[12] = rstArray.item(curRow+1, curCol-2)
        value[13] = rstArray.item(curRow+2, curCol-2)
        value[14] = rstArray.item(curRow+2, curCol-1)
        value[15] = rstArray.item(curRow+2, curCol)
        value[16] = rstArray.item(curRow+2, curCol+1)
        value[17] = rstArray.item(curRow+2, curCol+2)
        value[18] = rstArray.item(curRow+1, curCol+2)
        value[19] = rstArray.item(curRow, curCol+2)
        value[20] = rstArray.item(curRow-1, curCol+2)
        value[21] = rstArray.item(curRow-2, curCol+2)
        value[22] = rstArray.item(curRow-2, curCol+1)
        value[23] = rstArray.item(curRow-2, curCol)
        value[24] = rstArray.item(curRow-2, curCol-1)
        value[25] = rstArray.item(curRow-3, curCol-3)
        value[26] = rstArray.item(curRow-3, curCol-2)
        value[27] = rstArray.item(curRow-3, curCol-1)
        value[28] = rstArray.item(curRow-3, curCol)
        value[29] = rstArray.item(curRow-3, curCol+1)
        value[30] = rstArray.item(curRow-3, curCol+2)
        value[31] = rstArray.item(curRow-3, curCol+3)
        value[32] = rstArray.item(curRow-2, curCol+3)
        value[33] = rstArray.item(curRow-1, curCol+3)
        value[34] = rstArray.item(curRow, curCol+3)
        value[35] = rstArray.item(curRow+1, curCol+3)
        value[36] = rstArray.item(curRow+2, curCol+3)
        value[37] = rstArray.item(curRow+3, curCol+3)
        value[38] = rstArray.item(curRow+3, curCol+2)
        value[39] = rstArray.item(curRow+3, curCol+1)
        value[40] = rstArray.item(curRow+3, curCol)
        value[41] = rstArray.item(curRow+3, curCol-1)
        value[42] = rstArray.item(curRow+3, curCol-2)
        value[43] = rstArray.item(curRow+3, curCol-3)
        value[44] = rstArray.item(curRow+2, curCol-3)
        value[45] = rstArray.item(curRow+1, curCol-3)
        value[46] = rstArray.item(curRow, curCol-3)
        value[47] = rstArray.item(curRow-1, curCol-3)
        value[48] = rstArray.item(curRow-2, curCol-3)

        
#        

       except IndexError:

             pass

       b=[0]*48 # 48 because the number of numbering pixels is 48 for entering 3 as a spatial input
#       b=[0]*8
       changeX=[]

       changeY=[]

       for temp in range(0,48):
#       for temp in range(0,8):    

           b[temp]=abs(value[0]-value[temp+1])
           
           try:
               if np.all(b[temp] <= int (Tempo)) and np.all(outArray [my_func(curRow,curCol,temp)] == 0) and np.all(rstArray[my_func(curRow,curCol,temp)] != 0):
               #if np.all(b[temp] <= int (Tempo)) and np.all(outArray [my_func(curRow,curCol,temp)] == 0):
                   outArray[my_func(curRow,curCol,temp)] = fireClass
                   changeX.append(my_func(curRow,curCol,temp)[0])
                   changeY.append(my_func(curRow,curCol,temp)[1])
           except IndexError:
               #import pdb
               #pdb.set_trace()
               pass
           
    
       return outArray, changeX, changeY         
###################################################################################### I need a environment: where is my input rasters
#arcpy.env.workspace = r"C:\test\1227"
#r2=[]       
rasterlist=arcpy.ListRasters("p*","TIF")
#sorted(rasterlist)
#print rasterlist
fireClass = 18266
for a in rasterlist:
     #arcpy.env._environments=OutData
     rast= arcpy.sa.Raster(a)
##################################################################################### I need a output envronment to save each raster after they are really a RASTER!
     rast.save(a)
     [rstArray,llpnt,cellSize,spref]=RasterToArr(OutData,a) 
     outArray = np.zeros(rstArray.shape)
     rows, cols = (rstArray.shape)   
     changeX = []
     changeY = [] 


     if int(Spatio)==3:

      for rowNum in xrange(rows):
        for colNum in xrange(cols):
           
              
              if outArray [rowNum,colNum] == 0 and rstArray [rowNum,colNum] != 0 and  rstArray [rowNum,colNum] != None: 
                  outArray, changeX, changeY = main_fun(rowNum, colNum, rstArray, outArray, fireClass,int(Spatio)) 
                  if len(changeX) == 0:
                      outArray [rowNum, colNum] = fireClass
                  else:
                      outArray [rowNum, colNum] = fireClass
                      while len(changeX) != 0:
                          tempX = []
                          tempY = []
                          curRow = changeX[0]
                          curCol = changeY[0]
                          outArray, tempX, tempY = main_fun(curRow, curCol, rstArray, outArray, fireClass,int(Spatio))
                          if len(tempX) !=0 and rstArray [rowNum,colNum] >0:
                              for k in range(len(tempX)):
                                changeX.append(tempX[k])
                                changeY.append(tempY[k])
                          changeX.pop(0)
                          changeY.pop(0)

                  fireClass = fireClass + 1
      arrToRaster(outArray,llpnt,cellSize,spref,Tempo,Spatio, str(a))  
#      if arcpy.Exists( "x5.tif"):
#         arcpy.Delete_management ("x5.tif")          
print round (time.clock()-start,2),'second'