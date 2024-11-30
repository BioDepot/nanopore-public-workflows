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

class OWCramino(OWBwBWidget):
    name = "Cramino"
    description = "Cramino QC"
    priority = 10
    icon = getIconName(__file__,"cramino.png")
    want_main_area = False
    docker_image_name = "quay.io/biocontainers/cramino"
    docker_image_tag = "0.14.1--h5076881_0"
    inputs = [("bamFile",str,"handleInputsbamFile")]
    pset=functools.partial(settings.Setting,schema_only=True)
    runMode=pset(0)
    exportGraphics=pset(False)
    runTriggers=pset([])
    triggerReady=pset({})
    inputConnectionsStore=pset({})
    optionsChecked=pset({})
    bamFile=pset([])
    threads=pset(None)
    outputDir=pset(None)
    def __init__(self):
        super().__init__(self.docker_image_name, self.docker_image_tag)
        with open(getJsonName(__file__,"Cramino")) as f:
            self.data=jsonpickle.decode(f.read())
            f.close()
        self.initVolumes()
        self.inputConnections = ConnectionDict(self.inputConnectionsStore)
        self.drawGUI()
    def handleInputsbamFile(self, value, *args):
        if args and len(args) > 0: 
            self.handleInputs("bamFile", value, args[0][0], test=args[0][3])
        else:
            self.handleInputs("inputFile", value, None, False)
