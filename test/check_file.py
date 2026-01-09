#os.path.exists()
from pathlib import Path
import os
filename = "practice2.txt"
file_name = Path(r"D:\git_python\test")

if file_name.exists():
    print("file exists")
else:
    print("file does not exist")

if os.path.exists (filename):
    print("file exists")
else:
    print("file does not exist")
