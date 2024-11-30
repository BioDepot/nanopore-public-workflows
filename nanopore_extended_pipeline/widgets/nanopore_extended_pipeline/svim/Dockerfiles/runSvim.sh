#!/bin/bash

shopt -s extglob
inputArgs=("$@")
svim alignment ${inputArgs[@]} $outputDir $inputFile $reference

# Filter out "chrUn" and "random" chromosomes
cat "${outputDir}/variants.vcf" | grep \"^#\" | grep -v chrUn | grep -v random > "${outputDir}/sv_svim_notPhased_filtered.vcf"
cat "${outputDir}/variants.vcf" | grep -v \"^#\" | grep -v chrUn | grep -v random >> "${outputDir}/sv_svim_notPhased_filtered.vcf"