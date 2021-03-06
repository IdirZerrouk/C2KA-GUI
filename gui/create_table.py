"""Imported modules."""
from tkinter import * ##Import the tkinter module to allow construction of the GUI interface.

"""Functions which recreate the table"""
##create_table() is called when table is first created.
def create_table(bevDict, stimDict, circleGridFrame, lambdaGridFrame):
  """ (dict, dict, tkinter.Frame, tkinter.Frame) -> (dict, dict)
    
    Creates circle and lambda tables and stores the entry
    boxes in the dictionaries.
  
  """    
  ##Generate data structures for the table boxes.
  circleTableBoxes = {}
  lambdaTableBoxes = {}   
  
  ##Generate labels for the behaviours.
  for i in range(1, len(bevDict) + 1): ##Rows.
    bevLabel = Label(circleGridFrame, text = bevDict[i])
    bevLabel.grid(row = i, column = 0)
    circleTableBoxes[i, 0] = bevLabel
    bevLabel = Label(lambdaGridFrame, text = bevDict[i])
    bevLabel.grid(row = i, column = 0)  
    lambdaTableBoxes[i, 0] = bevLabel
  
  ##Generate labels for the stimuli.
  for j in range(1, len(stimDict) + 1): ##Columns.
    stimLabel = Label(circleGridFrame, text = stimDict[j])
    stimLabel.grid(row = 0, column = j)  
    circleTableBoxes[0, j] = stimLabel
    stimLabel = Label(lambdaGridFrame, text = stimDict[j])
    stimLabel.grid(row = 0, column = j)   
    lambdaTableBoxes[0, j] = stimLabel
  
  ##Generate the entry boxes.
  for i in range(1, len(bevDict) + 1): ##Rows.
    for j in range(1, len(stimDict) + 1): ##Columns.
      circleTableEntry = Entry(circleGridFrame)
      lambdaTableEntry = Entry(lambdaGridFrame)
      circleTableEntry.grid(row=i, column=j)
      lambdaTableEntry.grid(row=i, column=j)
      circleTableBoxes[i, j] = circleTableEntry
      lambdaTableBoxes[i, j] = lambdaTableEntry
   
  return circleTableBoxes, lambdaTableBoxes 

##recreate_table() is called when table was already generated.
def recreate_table(bevDict, stimDict, circleTableBoxes, lambdaTableBoxes, 
                   circleGridFrame, lambdaGridFrame):
  """ (dict, dict, dict, dict, tkinter.Frame, tkinter.Frame) -> (dict, dict)
    
    Recreates circle and lambda tables and stores the entry
    boxes in the dictionaries.
  
  """    
 ##Generate labels for the behaviours.
  for i in range(1, len(bevDict) + 1): ##Rows.
    bevLabel = Label(circleGridFrame, text = bevDict[i])
    bevLabel.grid(row = i, column = 0)
    
    circleTableBoxes[i, 0] = bevLabel
    
    bevLabel = Label(lambdaGridFrame, text = bevDict[i])
    bevLabel.grid(row = i, column = 0)  
    
    lambdaTableBoxes[i, 0] = bevLabel
  
  ##Generate labels for the stimuli.
  for j in range(1, len(stimDict) + 1): ##Columns.
    stimLabel = Label(circleGridFrame, text = stimDict[j])
    stimLabel.grid(row = 0, column = j)  
    
    circleTableBoxes[0, j] = stimLabel
    
    stimLabel = Label(lambdaGridFrame, text = stimDict[j])
    stimLabel.grid(row = 0, column = j)   
    
    lambdaTableBoxes[0, j] = stimLabel
  
  ##Re-generate the table with the modifications brought by fix_grids()
  for i in range(1, len(bevDict) + 1): ##Rows
    for j in range(1, len(stimDict) + 1): ##Columns
      circleTableEntry = Entry(circleGridFrame)
      lambdaTableEntry = Entry(lambdaGridFrame)
 
      circleTableEntry.grid(row=i, column=j)
      lambdaTableEntry.grid(row=i, column=j)
      
      circleTableEntry.insert(0, circleTableBoxes[i, j].get())
      lambdaTableEntry.insert(0, lambdaTableBoxes[i, j].get())
        
      circleTableBoxes[i, j] = circleTableEntry
      lambdaTableBoxes[i, j] = lambdaTableEntry
       
  return circleTableBoxes, lambdaTableBoxes ##Return updated data structures
                                            ##to the main program.