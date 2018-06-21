import subprocess
import time
import os


Device_1 = raw_input('Enter First Device Serial Number: ')

Device_2 = raw_input("Enter Second Device Serial Number: ")

if(os.path.isdir('C:\\FeaturePhone_testing')==True):

##    os.mkdir('D:\\FeaturePhone_testing')

##    os.mkdir('C:\\FeaturePhone_testing\\Device')
##
##    os.mkdir('C:\\FeaturePhone_testing\\Device')
    pass


else:
    
    os.mkdir('C:\\FeaturePhone_testing')

    os.mkdir('C:\\FeaturePhone_testing\\Device')

    os.mkdir('C:\\FeaturePhone_testing\\Device')


i = 1

while True: 

    while True:        

        Device_1_log = open('C:\\FeaturePhone_testing\\Device\\'+str(Device_1)+'_'+ str(i)+'.txt','w')

        Device_2_log = open('C:\\FeaturePhone_testing\\Device\\'+str(Device_2)+'_'+str(i)+'.txt','w')
            
        process_1 = subprocess.Popen(['adb','logcat',str(Device_1),'-s'],shell =False,stdout=Device_1_log)

        process_2 = subprocess.Popen(['adb','logact',str(Device_2),'-s'],shell=False,stdout=Device_2_log)       

        if process_1.poll() is None:

            print('Device_1 Log is running...')

            time.sleep(6)

            process_1.kill()

            print('Device_1 Log Finished.')           
    
        else:
            print('Device_1 Log is not running')

        if process_2.poll() is None:

            print('Device_2 Log is running...')

            time.sleep(6)

            process_2.kill()

            print('Device_2 Log Finished.')
            
        else:
            
            print('Device_2 Log is not running.')           

            
        break

    i = i+1
    
    Device_1_log.close()

    Device_2_log.close()
    

