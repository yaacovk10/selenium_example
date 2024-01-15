# import win32com.client as comclt
# import time

# wsh = comclt.Dispatch("WScript.Shell")
# success = wsh.AppActivate("C:\\Windows\\System32\\notepad.exe")

# if not success:
#     print("Failed to activate Notepad.")
    
# time.sleep(10)
# wsh.SendKeys("Yaacov")  # send the keys you want


# # Wait for a short while to ensure Notepad processes the previous SendKeys
# import time

# time.sleep(5)


# # Send the Save As command (Alt + F + A)
# wsh.SendKeys("%FA")


# # Wait for a short while to ensure the Save As dialog appears
# time.sleep(3)


# # Type the filename you want to save (e.g., "example.txt")
# filename = "yaacov.txt"
# wsh.SendKeys(filename)


# # Send the Enter key to confirm the file name and save
# wsh.SendKeys("~")


import win32com.client
import time

notepad = win32com.client.Dispatch("WScript.Shell")

notepad.Run("notepad.exe")

notepad.AppActivate("C:\\Windows\\System32\\notepad.exe")
time.sleep(5)
notepad.SendKeys("Yaacov")