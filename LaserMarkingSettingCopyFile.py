import os, glob
from win32com.client import Dispatch


#source path
basedir = "D:"
base_folder = "6. Catur/Laser_Marking/Dummy"



top_level = "2"
mid_level = "B"
bottom_level = "a"

src_path = "{directory}{separator}{base_folder}/{L1}/{L2}/{L3}.txt".format(directory=basedir ,separator=os.sep, base_folder=base_folder,L1=top_level,L2=mid_level,L3=bottom_level) 

#target path 
target_desktop_path = "C:{}Users/18035131/Desktop/LM_desktopdummy".format(os.sep)
target_path = os.path.join(target_desktop_path,"{}_{}_{}.lnk".format(top_level,mid_level,bottom_level))


#Process

files = glob.glob(target_desktop_path+"/*.lnk")
for f in files:
    os.remove(f)

ws = Dispatch('wscript.Shell')
scut = ws.CreateShortCut(target_path)
scut.Targetpath = src_path
scut.Arguments = '-m idlelib.idle'
scut.Save()