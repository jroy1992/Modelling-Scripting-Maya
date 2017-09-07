# userInterface.py

"""
======================================
A user interface to genrate staricase
======================================
"""
import maya.cmds as cmds
import functools

# Creating the interface window by setting the number of columns required, their lengths and placing them in order        
myWindow = cmds.window(title = 'Build Stairs', sizeable = True, resizeToFitChildren = True)
cmds.rowColumnLayout(numberOfColumns = 3, columnWidth = [(1,100), (2,60), (3,65)], columnOffset = [(1,'right',3)])

# Setting up names of the fields and cells for user input
cmds.text(label = 'Number of stairs ')
#  Specifing that the field 'Number of stairs' accepts only integer inputs
numberOfStairs = cmds.intField(minValue = 1, value = 10)
cmds.separator(height = 10, style = 'none')

# Adding spaces between the subsequent rows
cmds.separator(height = 10, style = 'none')
cmds.separator(height = 10, style = 'none')
cmds.separator(height = 10, style = 'none')

cmds.text(label = 'Size of each step')
cmds.separator(height = 10, style = 'none')
cmds.separator(height = 10, style = 'none')

cmds.text(label = 'Width ')
width = cmds.intField(minValue = 1, value = 2)
cmds.separator(height = 10, style = 'none')

cmds.text(label = 'Height')
height = cmds.intField(minValue = 1, value = 2)
cmds.separator(height = 10, style = 'none')

cmds.text(label = 'Depth')
depth = cmds.intField(minValue = 1, value = 2)
cmds.separator(height = 10, style = 'none')

cmds.separator(height = 10, style = 'none')
cmds.separator(height = 10, style = 'none')
cmds.separator(height = 10, style = 'none')

"""
applyCallback() function implements the command to print the stairs according to the user specifications.
It accepts four parameters: number of stairs the user wants to print, width, height and depth of the steps. 
It then passes the parameters to the function Stairs() where the actual generation of staircase takes place.  
"""

def applyCallback(pnumberOfStairs, pwidth, pheight, pdepth, *pArgs):
    noStairs = cmds.intField(pnumberOfStairs, query = True, value = True)
    w = cmds.intField(pwidth, query = True, value = True)
    h = cmds.intField(pheight, query = True, value = True)
    d = cmds.intField(pdepth, query = True, value = True)
    
    print 'stairs: %s' % (noStairs)
    print 'width: %s' % (w)
    print 'depth: %s' % (h)
    print 'height: %s' % (d)
    
    Stairs(noStairs, w, d, h)
    
cmds.separator(height = 10, style = 'none')

# Apply button on the interface to send a call to applyCallback function
cmds.button(label = 'Apply', command = functools.partial(applyCallback,numberOfStairs, width, height, depth))

"""
cancelCallback() function to delete the user interface window.
As soon as Cancel button is clicked, the UI window will be deleted.
"""

def cancelCallback(*pArgs):
    if cmds.window(myWindow, exists = True):
        cmds.deleteUI(myWindow)

cmds.button(label = 'Cancel', command = "cancelCallback()")

cmds.separator(height = 10, style = 'none')
cmds.separator(height = 10, style = 'none')
cmds.separator(height = 10, style = 'none')

cmds.showWindow(myWindow)

"""
The function Stairs() is activated by the call from applyCallback().
It accepts four inputs: the number of steps in a stair and width, height and depth of each step. 
"""
def Stairs(numberOfStairs, width, depth, height):
    
    steps = []
    for i in range(1,numberOfStairs):
        # make a step
        stair = cmds.polyCube(d = depth, h = height, w = width, name = "stair")
        steps.append(stair[0])
        # move the ith step with respect to height and depth (i-1)th step
        cmds.move(0, i*height, i*depth)
    # script is out of the chain and going to group all the steps.
    stepGRP = cmds.group(steps,name = "stepGroup")