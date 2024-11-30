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

class OWNanoPlot(OWBwBWidget):
    name = "NanoPlot"
    description = "NanoPlot QC"
    priority = 1
    icon = getIconName(__file__,"NanoPlot.png")
    want_main_area = False
    docker_image_name = "quay.io/biocontainers/nanoplot"
    docker_image_tag = "1.43.0--pyhdfd78af_1"
    inputs = [("Trigger",str,"handleInputsTrigger"),("fastq",str,"handleInputsfastq"),("fastqRich",str,"handleInputsfastqRich"),("fasta",str,"handleInputsfasta"),("summary",str,"handleInputssummary"),("bam",str,"handleInputsbam"),("ubam",str,"handleInputsubam"),("outputDir",str,"handleInputsoutputDir")]
    pset=functools.partial(settings.Setting,schema_only=True)
    runMode=pset(0)
    exportGraphics=pset(False)
    runTriggers=pset([])
    triggerReady=pset({})
    inputConnectionsStore=pset({})
    optionsChecked=pset({})
    fastq=pset([])
    fastqRich=pset([])
    fasta=pset([])
    summary=pset([])
    bam=pset([])
    ubam=pset([])
    outputDir=pset(None)
    prefix=pset([])
    verbose=pset(False)
    threads=pset(None)
    infoInReport=pset(False)
    maxLength=pset(None)
    minLength=pset(None)
    dropOutliers=pset(False)
    downsample=pset(None)
    logLength=pset(False)
    percentQual=pset(False)
    alength=pset(False)
    minqual=pset(None)
    barcoded=pset(False)
    huge=pset(False)
    def __init__(self):
        super().__init__(self.docker_image_name, self.docker_image_tag)
        with open(getJsonName(__file__,"NanoPlot")) as f:
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
    def handleInputsfastq(self, value, *args):
        if args and len(args) > 0: 
            self.handleInputs("fastq", value, args[0][0], test=args[0][3])
        else:
            self.handleInputs("inputFile", value, None, False)
    def handleInputsfastqRich(self, value, *args):
        if args and len(args) > 0: 
            self.handleInputs("fastqRich", value, args[0][0], test=args[0][3])
        else:
            self.handleInputs("inputFile", value, None, False)
    def handleInputsfasta(self, value, *args):
        if args and len(args) > 0: 
            self.handleInputs("fasta", value, args[0][0], test=args[0][3])
        else:
            self.handleInputs("inputFile", value, None, False)
    def handleInputssummary(self, value, *args):
        if args and len(args) > 0: 
            self.handleInputs("summary", value, args[0][0], test=args[0][3])
        else:
            self.handleInputs("inputFile", value, None, False)
    def handleInputsbam(self, value, *args):
        if args and len(args) > 0: 
            self.handleInputs("bam", value, args[0][0], test=args[0][3])
        else:
            self.handleInputs("inputFile", value, None, False)
    def handleInputsubam(self, value, *args):
        if args and len(args) > 0: 
            self.handleInputs("ubam", value, args[0][0], test=args[0][3])
        else:
            self.handleInputs("inputFile", value, None, False)
    def handleInputsoutputDir(self, value, *args):
        if args and len(args) > 0: 
            self.handleInputs("outputDir", value, args[0][0], test=args[0][3])
        else:
            self.handleInputs("inputFile", value, None, False)
