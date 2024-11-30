#!/bin/bash
shopt -s extglob
inputArgs=("$@")

# Put the output .tsv file in the same directory as the .vcf.gz file
BASENAME=$(basename "$VCFINPUT" .vcf.gz)
DIRNAME=$(dirname "$VCFINPUT" .vcf.gz)
TSV="whatshap_${BASENAME}.clair3.phased.phasing_stats.tsv"

# Run the whatshap stats command
echo whatshap stats --tsv "${DIRNAME}/${TSV}" "${inputArgs}" "${VCFINPUT}"
eval whatshap stats --tsv "${DIRNAME}/${TSV}" "${inputArgs}" "${VCFINPUT}"