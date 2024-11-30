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

class OWLongphase_phase(OWBwBWidget):
    name = "Longphase_phase"
    description = "Longphase phase"
    priority = 10
    icon = getIconName(__file__,"longphase.png")
    want_main_area = False
    docker_image_name = "quay.io/biocontainers/longphase"
    docker_image_tag = "1.7.3--hf5e1c6e_0"
    inputs = [("snpFile",str,"handleInputssnpFile"),("bamFile",str,"handleInputsbamFile"),("reference",str,"handleInputsreference"),("svFile",str,"handleInputssvFile")]
    pset=functools.partial(settings.Setting,schema_only=True)
    runMode=pset(0)
    exportGraphics=pset(False)
    runTriggers=pset([])
    triggerReady=pset({})
    inputConnectionsStore=pset({})
    optionsChecked=pset({})
    snpFile=pset([])
    bamFile=pset([])
    reference=pset(None)
    ont=pset(False)
    pb=pset(False)
    threads=pset(None)
    svFile=pset([])
    outPrefix=pset("phasing_result")
    def __init__(self):
        super().__init__(self.docker_image_name, self.docker_image_tag)
        with open(getJsonName(__file__,"Longphase_phase")) as f:
            self.data=jsonpickle.decode(f.read())
            f.close()
        self.initVolumes()
        self.inputConnections = ConnectionDict(self.inputConnectionsStore)
        self.drawGUI()
    def handleInputssnpFile(self, value, *args):
        if args and len(args) > 0: 
            self.handleInputs("snpFile", value, args[0][0], test=args[0][3])
        else:
            self.handleInputs("inputFile", value, None, False)
    def handleInputsbamFile(self, value, *args):
        if args and len(args) > 0: 
            self.handleInputs("bamFile", value, args[0][0], test=args[0][3])
        else:
            self.handleInputs("inputFile", value, None, False)
    def handleInputsreference(self, value, *args):
        if args and len(args) > 0: 
            self.handleInputs("reference", value, args[0][0], test=args[0][3])
        else:
            self.handleInputs("inputFile", value, None, False)
    def handleInputssvFile(self, value, *args):
        if args and len(args) > 0: 
            self.handleInputs("svFile", value, args[0][0], test=args[0][3])
        else:
            self.handleInputs("inputFile", value, None, False)
