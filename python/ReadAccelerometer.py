# coding: latin-1

# Load the XLoBorg library
import XLoBorg
import time
import json
from shutil import copyfile

# Tell the library to disable diagnostic printouts
XLoBorg.printFunction = XLoBorg.NoPrint

# Start the XLoBorg module (sets up devices)
XLoBorg.Init()

#Grab initial value and store to use later in comparrison
initialValue = XLoBorg.ReadAccelerometer()

firstInitialValue = round(initialValue[0],0)
secondInitialValue = round(initialValue[1],0)
thirdInitialValue = round(initialValue[2],0)


# Read and display the raw magnetometer readings

while(1):
        #print 'X = %+01.4f G, Y = %+01.4f G, Z = %+01.4f G' % XLoBorg.ReadAccelerometer()
        time.sleep(0.8)
        q = []
#       print type(XLoBorg.ReadAccelerometer())
        assignData = XLoBorg.ReadAccelerometer() #Assign data to an array
#       print "---------------------------"
#       print assignData[0] #This is the first value
#       print assignData[1] #Second value
#       print assignData[2] #Third value
#       print "-------------------------------"
#       print firstInitialValue
#       print "+---------------------------"

        if firstInitialValue != round(assignData[0],0):
                global firstInitialValue
                print "-----1------"
                print firstInitialValue
                print round(assignData[0],0)
                print "------------"
                firstInitialValue = round(assignData[0],0)
                copyfile("data.json", "/var/www/html/socketTest/tiltDetection.json")

        elif secondInitialValue != round(assignData[1],0):
                global secondInitialValue
                print "Not equal anymore 2"
                secondInitialValue = round(assignData[1],0)
                copyfile("data.json", "/var/www/html/socketTest/tiltDetection.json")

        elif thirdInitialValue != round(assignData[2],0):
                global thirdInitialValue
                print "Not equal anymore 3"
                thirdInitialValue = round(assignData[2],0)
                copyfile("data.json", "/var/www/html/socketTest/tiltDetection.json")


#       print '%+01.2f G' % XLoBorg.ReadAccelerometer()

# These few lines can handle json nicely to customise the file contents if needed later on
#       q.append({"x" : assignData[0], "y" : assignData[1], "z" : assignData[2]})
#       print json.dumps(q,indent=4)
#       fout = open("data.json", 'w')
#       json.dump(q,fout,indent=4)
#       fout.close()