from subprocess import Popen, PIPE

process = Popen(['dir'], stdout=PIPE, shell=True)
stdout, stderr = process.communicate()