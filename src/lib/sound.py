#!/usr/bin/env python3
import os
from pathlib import Path
import platform
class Sound(object):
    def __init__(self, path):
        if platform.system() in ["Linux", "Darwin"]:
            self.bin = "mpg123"
        else:
            self.bin = Path(" ../bin/mpg123")

        self.path = Path(path)


    def play(self):
        os.system(f'{self.bin}  -g100 {self.path} &')


