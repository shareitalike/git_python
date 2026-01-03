#os.path.exists()

import os
filename = "practice2.txt"

if os.path.exists (filename):
    print("file exists")
else:
    print("file does not exist")
