@@ -1,18 +1,13 @@
import os, platform,time
import os, platform
try:
   import requests
    import requests
except:
   os.system('pip2 install requests')
from time import sleep
    os.system('pip install requests')
os.system('git pull')
import requests
bit = platform.architecture()[0]
if bit == '64bit':
    from Aking import readline___Public_Xml
    print("\n Congratulations! Your device supported!\n")
    time.sleep(3)
    from pc import readline___Public_Xml
    readline___Public_Xml()
elif bit == '32bit':
    from f32 import readline___Public_Xml
    print("\n Congratulations! Your device supported!\n")
    time.sleep(3)
    exit()
    print("\x1b[1;91mOpps Sorry Brother Your Mobile Not Support This Tools")
