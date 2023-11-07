FROM continuumio/miniconda3:23.9.0-0

# Use yaml file to install packages needed in "INSnet" environment
ADD environment.yml /tmp/environment.yml
RUN conda env create -f /tmp/environment.yml

# Copy INSnet scripts and set workdir to the INSnetfolder
COPY INSnet/ /INSnet
WORKDIR /INSnet

# Activate our environment and add environment's bin directory to path
RUN echo "source activate INSnet" > ~/.bashrc
ENV PATH /opt/conda/envs/INSnet/bin:$PATH
