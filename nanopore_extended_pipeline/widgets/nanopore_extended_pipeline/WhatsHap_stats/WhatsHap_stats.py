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

class OWWhatsHap_stats(OWBwBWidget):
    name = "WhatsHap_stats"
    description = "WhatsHap Stats print phasing statistics from VCF"
    priority = 10
    icon = getIconName(__file__,"whatshap_logo.png")
    want_main_area = False
    docker_image_name = "biodepot/clair3"
    docker_image_tag = "v1.0.8_whatshap_stats"
    inputs = [("vcf",str,"handleInputsvcf"),("gtf",str,"handleInputsgtf")]
    pset=functools.partial(settings.Setting,schema_only=True)
    runMode=pset(0)
    exportGraphics=pset(False)
    runTriggers=pset([])
    triggerReady=pset({})
    inputConnectionsStore=pset({})
    optionsChecked=pset({})
    vcf=pset([])
    gtf=pset([])
    onlySnvs=pset(False)
    chr=pset(None)
    def __init__(self):
        super().__init__(self.docker_image_name, self.docker_image_tag)
        with open(getJsonName(__file__,"WhatsHap_stats")) as f:
            self.data=jsonpickle.decode(f.read())
            f.close()
        self.initVolumes()
        self.inputConnections = ConnectionDict(self.inputConnectionsStore)
        self.drawGUI()
    def handleInputsvcf(self, value, *args):
        if args and len(args) > 0: 
            self.handleInputs("vcf", value, args[0][0], test=args[0][3])
        else:
            self.handleInputs("inputFile", value, None, False)
    def handleInputsgtf(self, value, *args):
        if args and len(args) > 0: 
            self.handleInputs("gtf", value, args[0][0], test=args[0][3])
        else:
            self.handleInputs("inputFile", value, None, False)
