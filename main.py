
import os
import subprocess
import time
import signal

os.chdir(os.getcwd()+'/jpm_module_1')

process = subprocess.Popen(['python', 'server3.py'], cwd=os.getcwd(), preexec_fn=os.setsid)

time.sleep(.300)

process2 = subprocess.Popen(['python', 'client3.py'], cwd=os.getcwd(), preexec_fn=os.setsid)
process2.wait()
os.killpg(os.getpgid(process.pid), signal.SIGTERM)

print("UNIT TEST RESULTS BELOW...")
process2 = subprocess.Popen(['python', 'client_test.py'], cwd=os.getcwd(), preexec_fn=os.setsid)
process2.wait()