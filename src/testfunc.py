import subprocess
import sys

# abc = "/Users/jeffjhzhang/Documents/PdfBkGenerator/src/testapp.py"

# subprocess.call(["open","-R",abc])
def revealinFinder(self,file):
    
    s=sys.platform.lower()
    if s.startswith("linux"):
        pass
    elif s=="darwin": 
        #mac
        param=["open","-R",file]
        subprocess.call(param)
    elif s=="win32":
        #windows
        param=["explorer", "/select, ", file]
        subprocess.call(param)
        #It's very very very important to add comma(,) after parameter '/select'
        # subprocess.call(["explorer", "/select, ", file]) # OK
        # subprocess.Popen(["explorer", "/select, ", file]) #OK
        # Qprocess.startDetached("explorer /select, \"{}\"".format (file))#OK
    
print(sys.platform)