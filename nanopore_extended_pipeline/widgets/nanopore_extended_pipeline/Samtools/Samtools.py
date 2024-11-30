import os
import glob
import sys
import functools
import jsonpickle
from collections import OrderedDict
from Orange.widgets import widget, gui, settings
import Orange.data
from Orange.data.io import FileFormat
from DockerClient import DockerClient
from BwBase import OWBwBWidget, ConnectionDict, BwbGuiElements, getIconName, getJsonName
from PyQt5 import QtWidgets, QtGui

class OWSamtools(OWBwBWidget):
    name = "Samtools"
    description = "Samtools v1.15.1"
    priority = 1
    icon = getIconName(__file__,"samtools.png")
    want_main_area = False
    docker_image_name = "brycenofu/samtools"
    docker_image_tag = "1.15.1__ubuntu_24.04"
    inputs = [("Trigger",str,"handleInputsTrigger"),("bamInputDir",str,"handleInputsbamInputDir"),("fastqOutputDir",str,"handleInputsfastqOutputDir")]
    outputs = [("fastqOutputDir",str)]
    pset=functools.partial(settings.Setting,schema_only=True)
    runMode=pset(0)
    exportGraphics=pset(False)
    runTriggers=pset([])
    triggerReady=pset({})
    inputConnectionsStore=pset({})
    optionsChecked=pset({})
    bamInputDir=pset({})
    fastqOutputDir=pset(None)
    threads=pset(None)
    taglist=pset(None)
    def __init__(self):
        super().__init__(self.docker_image_name, self.docker_image_tag)
        with open(getJsonName(__file__,"Samtools")) as f:
            self.data=jsonpickle.decode(f.read())
            f.close()
        self.initVolumes()
        self.inputConnections = ConnectionDict(self.inputConnectionsStore)
        self.drawGUI()
    def handleInputsTrigger(self, value, *args):
        if args and len(args) > 0: 
            self.handleInputs("Trigger", value, args[0][0], test=args[0][3])
        else:
            self.handleInputs("inputFile", value, None, False)
    def handleInputsbamInputDir(self, value, *args):
        if args and len(args) > 0: 
            self.handleInputs("bamInputDir", value, args[0][0], test=args[0][3])
        else:
            self.handleInputs("inputFile", value, None, False)
    def handleInputsfastqOutputDir(self, value, *args):
        if args and len(args) > 0: 
            self.handleInputs("fastqOutputDir", value, args[0][0], test=args[0][3])
        else:
            self.handleInputs("inputFile", value, None, False)
    def handleOutputs(self):
        outputValue=None
        if hasattr(self,"fastqOutputDir"):
            outputValue=getattr(self,"fastqOutputDir")
        self.send("fastqOutputDir", outputValue)
