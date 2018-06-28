from tkinter import *
import superscroll
import vertSuperscroll ##Module containing the widget allowing a vertical scrollbar.
from create_table import *
from entry_mods import *
from check_if_good import *
from CBS_mods import *
from CBS_radio import *
from set_data import *

def create_agent_page(main, allEditButtons, allCheckLabels, allFrames, editScrollingArea, allBevDict, 
                      stimDict, allFillButtons, agentNames, allCircleTableBoxes, 
                      allLambdaTableBoxes, allCircleScrollingArea, allLambdaScrollingArea, 
                      allCircleGridFrame, allLambdaGridFrame, allTextBoxCBSFrame, 
                      allTitleCBS, allFormatCBS,allEntriesCBS, allAgentCBS, allTextBoxCBS, 
                      allRadioButtons, allConcreteScrollingArea, moreThanOneAgent, 
                      generatedTables, generatedCBS, allCBSTabContents, allTableTabContents, edit_icon):
    
    editScrollingAreaTemp = vertSuperscroll.Scrolling_Area(main)
    editScrollingAreaTemp.pack(expand = 1, fill=BOTH, pady = (0, 80))

    for i in range(len(agentNames)):
        editFrame = Frame(editScrollingAreaTemp.innerframe, pady = 20, highlightbackground = "black", highlightcolor = "black", highlightthickness = 1)
        editLabel = Label(editFrame, text = agentNames[i], justify = LEFT, font = ("Times", 16), padx = 15)
        completeLabel = Label(editFrame)
        editButton = Button(editFrame, image = edit_icon, border = 0, highlightthickness = 0,
                                  command = lambda boxIndex=i: edit_agent_specs(main, allEditButtons, editScrollingArea, allBevDict, stimDict, 
                                                                                allFillButtons, agentNames, allCircleTableBoxes, allLambdaTableBoxes, 
                                                                                allCircleScrollingArea, allLambdaScrollingArea, allCircleGridFrame, 
                                                                                allLambdaGridFrame, allTextBoxCBSFrame, allTitleCBS, allFormatCBS, 
                                                                                allEntriesCBS, allAgentCBS, allFrames, allTextBoxCBS, allRadioButtons,
                                                                                allConcreteScrollingArea, moreThanOneAgent, generatedTables, generatedCBS, 
                                                                                boxIndex, allCBSTabContents, allTableTabContents)) 

        if allEditButtons[i] == None:
            allEditButtons[i] = editButton, False
        else:
            allEditButtons[i] = editButton, allEditButtons[i][1]

            completeLabel.config(image = allCheckLabels[i].cget("image"))
            
        
        allCheckLabels[i] = completeLabel
        editLabel.pack(side = LEFT, anchor = N)
        editButton.pack(side = RIGHT, anchor = N, padx = 20)
        completeLabel.pack(side = RIGHT, anchor = N)
        editFrame.pack(anchor = W, fill = X)
        editScrollingArea[0] = editScrollingAreaTemp  
    

def edit_agent_specs(main, allEditButtons, editScrollingArea, allBevDict, stimDict, 
                     allFillButtons, agentNames, allCircleTableBoxes, allLambdaTableBoxes, 
                     allCircleScrollingArea, allLambdaScrollingArea, allCircleGridFrame, 
                     allLambdaGridFrame, allTextBoxCBSFrame, allTitleCBS, allFormatCBS, allEntriesCBS, 
                     allAgentCBS, allFrames, allTextBoxCBS, allRadioButtons, allConcreteScrollingArea, 
                     moreThanOneAgent, generatedTables, generatedCBS, boxIndex, 
                     allCBSTabContents, allTableTabContents):
    global editAgent      
   
    allEditButtons[boxIndex][0].config(state = DISABLED)
    allEditButtons[boxIndex] = allEditButtons[boxIndex][0], True 
    
    if generatedCBS[boxIndex] == False:
        editAgent = Toplevel() ##Creating new window to edit agent specs
        editAgent.resizable(width = False, height = False) 
        allFrames[boxIndex] = editAgent ##Store specific frame according to index.
        
        ##Collect screen (monitor) width and height to position the window in the center. 
        screenWidth = editAgent.winfo_screenwidth() 
        screenHeight = editAgent.winfo_screenheight()       
        
        windowSize = int(screenHeight/2.16) ##Dimension of the window is about half that of the screen height.
        
        editAgent.geometry('%dx%d' % (windowSize, windowSize))

        editAgent.protocol("WM_DELETE_WINDOW", lambda: close_edit(boxIndex, allEditButtons, allFrames)) ##Give a command to the X button of the window.
        
        editButtonsFrame = Frame(editAgent) ##Making the save and cancel button
        
        saveButton = Button(editButtonsFrame, text = "Done", command = lambda: close_edit(boxIndex, allEditButtons, allFrames), highlightthickness = 0)

        saveButton.pack(side = RIGHT, anchor = S)
        #cancelButton = Button(editButtonsFrame, text = "Clear", highlightthickness = 0)
        #cancelButton.pack(side = LEFT, anchor = S)
        editButtonsFrame.pack(side = BOTTOM, fill = X)
        
        editTabs = ttk.Notebook(editAgent) ##Create Tabs to switch from tables to CBS
        CBSTab = Frame(editTabs)
        tableTab = Frame(editTabs)
        
        ##Add tabs to frame
        editTabs.add(CBSTab, text = "Concrete Behaviours")
        editTabs.add(tableTab, text = "Tables") 
        
        editTabs.pack(expand = 1, fill = BOTH)    
    else:
        
        editAgent = allFrames[boxIndex]
        editAgent.protocol("WM_DELETE_WINDOW", lambda boxIndex = boxIndex: close_edit(boxIndex, allEditButtons, allFrames))
        allFrames[boxIndex].winfo_children()[0].winfo_children()[0].config(command = lambda: close_edit(boxIndex, allEditButtons, allFrames))
        
        CBSTab = allFrames[boxIndex].winfo_children()[1].winfo_children()[0]
        tableTab = allFrames[boxIndex].winfo_children()[1].winfo_children()[1]


    """CBS Editing"""
    
    set_CBS_data(CBSTab, agentNames, allBevDict, allAgentCBS, allTextBoxCBSFrame, 
                 allFrames, allTitleCBS, allFormatCBS, allRadioButtons, 
                 allConcreteScrollingArea, allEntriesCBS, allTextBoxCBS, 
                 generatedCBS, moreThanOneAgent, boxIndex, allCBSTabContents)
    
    
    """Table Editing"""

    set_table_data(tableTab, allBevDict, stimDict, allFillButtons, allCircleTableBoxes, 
                   allLambdaTableBoxes, allCircleScrollingArea, 
                   allLambdaScrollingArea, allCircleGridFrame, allLambdaGridFrame, 
                   generatedTables, moreThanOneAgent, boxIndex, allTableTabContents)  

def close_edit(boxIndex, allEditButtons, allFrames):
    """ (tkinter.Tk) -> (none)
      
      Destroys the editAgent window 
    
    """

    allFrames[boxIndex].withdraw()

    allEditButtons[boxIndex][0].config(state = NORMAL)


