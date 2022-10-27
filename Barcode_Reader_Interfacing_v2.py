import keyboard, time
# from pynput import keyboard

#Type 1: Harus pakai spasi

# a = list(keyboard.get_typed_strings(keyboard.record(until='space')))
# print(a[0])
# print("OK")


#Type 2: gapakai spasi tapi fixed len

# def on_release_callback(e):
    # barcodeholder.append(e.name)
    ## print(barcodeholder)
    
    
# while True:
    # barcodeholder = []
    # keyboard.on_release(on_release_callback)
    # while True:
        ##print(len(barcodeholder))
        # if (len(barcodeholder) >= 9):
            # keyboard.unhook_all()
            # break
        # else:
            # pass
        # time.sleep(.1)
    ## print(barcodeholder)
    
####################### 
#Type 3: unlimited len, based on timeout after detect for first time

def on_release_callback(e):
    barcodeholder.append(e.name)
    
while True:
    barcodeholder = []
    keyboard.on_release(on_release_callback)
    while True:
        if (len(barcodeholder) != 0):
            time.sleep(2)
            keyboard.unhook_all()
            break
        else:
            pass
        time.sleep(.1)
    print(barcodeholder)
    

# def on_release_callback(e):
    # barcodeholder.append(e.name)
    # global insidecallback
    # insidecallback = 1
    ## print(barcodeholder)
    
# while True:
    # barcodeholder = []
    # pastbarcodeholder = []
    # keyboard.on_release(on_release_callback)
    # flag = [0,0]
    
    # while True:
       # insidecallback = 0
        #if ():
        # #   keyboard.unhook_all()
         ##   break
       # #else:
       ##     pass
       ## insidecallback = 0
        # print(insidecallback)
        # time.sleep(1)
    # print(barcodeholder)
    
    

