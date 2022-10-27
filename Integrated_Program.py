import os, glob, msvcrt, time
from win32com.client import Dispatch

srcbasedir = "D://6. Catur/Laser_Marking/Dummy"
targetbasedir = "C://Users/18035131/Desktop/LM_desktopdummy"


while True:

    flag= [0,0]
    barcode = ""
    while True:
        flag_item = msvcrt.kbhit()
        if(msvcrt.kbhit()):
            letter = msvcrt.getwch()
            barcode += letter
        flag.append(flag_item)
        flag.pop(0)
        if(flag[0]>flag[1]):
            break
        #print(flag)
        time.sleep(.02)
        
    #TODO INSERT STRING READ barcode program
    
    print(barcode)
    if(barcode[0] == "M"):
        L1 = "1"
        L2 = "A"
        L3 = "a"
        
    elif(barcode[0] == "4"):
        L1 = "2"
        L2 = "B"
        L3 = "c"
    
    else:
        L1 = "0"
        L2 = "0"
        L3 = "0"
        
    #sample barcode
    #MN000753A4
    #4549734446624
    ####
    
    src_path = "{}/{}/{}/{}.txt".format(srcbasedir, L1,L2,L3)
    
    #target path 
    target_path = os.path.join(targetbasedir,"{}_{}_{}.lnk".format(L1,L2,L3))
    
    #Process
    files = glob.glob(targetbasedir+"/*.lnk")
    for f in files:
        os.remove(f)
    ws = Dispatch('wscript.Shell')
    scut = ws.CreateShortCut(target_path)
    scut.Targetpath = src_path
    scut.Arguments = '-m idlelib.idle'
    scut.Save()