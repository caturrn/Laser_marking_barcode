import os, glob, msvcrt, time
from win32com.client import Dispatch
import keyboard


#Declare Variable
barcodeholder = []
srcbasedir = "D://6. Catur/Laser_Marking/Dummy"
targetbasedir = "C://Users/18035131/Desktop/LM_desktopdummy"
    
    
def on_release_callback(e):
    barcodeholder.append(e.name)

#main loop
while True:
    barcodeholder = []
    keyboard.on_release(on_release_callback)
    while True:
        if (len(barcodeholder) != 0):
            time.sleep(.3)
            keyboard.unhook_all()
            break
        else:
            pass
        time.sleep(.1)
    keyboard.unhook_all()
    barcode = ''.join(barcodeholder)
    print(barcode)
    
    
    #TODO INSERT STRING READ barcode program
    #sample barcode 5641062-1 3275082-0
   
    if(barcode[0] == "5"):
        L1 = "1"
        L2 = "A"
        L3 = "a"
        
    elif(barcode[0] == "3"):
        L1 = "2"
        L2 = "B"
        L3 = "c"
    
    else:
        L1 = "0"
        L2 = "0"
        L3 = "0"
    
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
