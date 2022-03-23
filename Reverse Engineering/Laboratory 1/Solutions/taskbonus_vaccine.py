import win32event, time

mutex = win32event.CreateMutex(None, True, "WEBLAUNCHASSIST_MUTEX")
# try to acquire the mutex 
result = win32event.WaitForSingleObject(mutex, 0)
if result == win32event.WAIT_OBJECT_0:
  print("Acquired the mutex, going to sleep for a minute")	
  time.sleep(60)
  win32event.ReleaseMutex(mutex)
else:
  print("Something went wrong; you maybe already infected or another instance of this program is running")
mutex.Close()
