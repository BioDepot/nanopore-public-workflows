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

class OWvep(OWBwBWidget):
    name = "vep"
    description = "Ensembl Variant Event Predictor annotate SNVs"
    priority = 10
    icon = getIconName(__file__,"vep.jpg")
    want_main_area = False
    docker_image_name = "ensemblorg/ensembl-vep"
    docker_image_tag = "release_111.0"
    inputs = [("vcfFile",str,"handleInputsvcfFile"),("Trigger",str,"handleInputsTrigger")]
    outputs = [("outputFile",str)]
    pset=functools.partial(settings.Setting,schema_only=True)
    runMode=pset(0)
    exportGraphics=pset(False)
    runTriggers=pset([])
    triggerReady=pset({})
    inputConnectionsStore=pset({})
    optionsChecked=pset({})
    forceOverwrite=pset(False)
    vcfFile=pset([])
    vcfOutEnable=pset(False)
    bufferSize=pset(5000)
    species=pset("homo_sapiens")
    fork=pset(None)
    outputFile=pset([])
    cache=pset(False)
    mergedCache=pset(False)
    offline=pset(False)
    dirCache=pset(None)
    canonical=pset(False)
    symbol=pset(False)
    numbers=pset(False)
    assembly=pset("GRCh38")
    useGivenRef=pset(False)
    pickAllele=pset(False)
    domains=pset(False)
    pubmed=pset(False)
    genePhenotype=pset(False)
    sift=pset("b")
    polyphen=pset("b")
    regulatory=pset(False)
    totalLength=pset(False)
    af=pset(False)
    maxAf=pset(False)
    afLkg=pset(False)
    customMultiAllelic=pset(False)
    dirPlugins=pset([])
    plugin=pset("--plugin SpliceVault ")
    customAnnotation=pset("--plugin SpliceVault ")
    def __init__(self):
        super().__init__(self.docker_image_name, self.docker_image_tag)
        with open(getJsonName(__file__,"vep")) as f:
            self.data=jsonpickle.decode(f.read())
            f.close()
        self.initVolumes()
        self.inputConnections = ConnectionDict(self.inputConnectionsStore)
        self.drawGUI()
    def handleInputsvcfFile(self, value, *args):
        if args and len(args) > 0: 
            self.handleInputs("vcfFile", value, args[0][0], test=args[0][3])
        else:
            self.handleInputs("inputFile", value, None, False)
    def handleInputsTrigger(self, value, *args):
        if args and len(args) > 0: 
            self.handleInputs("Trigger", value, args[0][0], test=args[0][3])
        else:
            self.handleInputs("inputFile", value, None, False)
    def handleOutputs(self):
        outputValue=None
        if hasattr(self,"outputFile"):
            outputValue=getattr(self,"outputFile")
        self.send("outputFile", outputValue)
