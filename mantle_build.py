#coding=utf-8
import os
import subprocess
import sys

path = os.path.join(os.path.abspath('.'))

file = open('Cartfile', 'w')
file.write('github "Mantle/Mantle"')
file.close()

command = 'carthage update --platform iOS'
subprocess.check_output(command, shell=True)

sys.stdout.write('Pass!\n')
print '==========',path
