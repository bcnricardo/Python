#Executes a root macro with 2 parameters: root -b -q 'runDiLep.cxx("input.txt","outputHists.root")'
import os
import subprocess
inputFile = 'input.txt';
outputFile = 'outputHists.root';
analysisCommand = 'runDiLep.cxx("' + inputFile + '","' + outputFile+ '")';
pythonCommand = """'""" + analysisCommand + """'""";
shellCommand = "root -b -q" + ' ' + pythonCommand;
os.system(shellCommand);
