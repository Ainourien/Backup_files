import os
from pathlib import Path
import backup_004
import importlib
import time

cwd = Path(__file__).parents[0]
os.chdir(cwd)

a = 0
while a == 0:
    importlib.reload(backup_004)
    print('trying to find unreserved files in destination folder...')
    time.sleep(5)


