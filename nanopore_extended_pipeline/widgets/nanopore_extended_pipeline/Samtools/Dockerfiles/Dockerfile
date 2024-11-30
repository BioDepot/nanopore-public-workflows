# Use a base image with the desired Linux distribution
FROM ubuntu:24.04
ARG SAMTOOLS_VERSION=1.15.1

# Install required dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    wget \
    zlib1g-dev \
    libbz2-dev \
    liblzma-dev \
    libcurl3-dev \
    ncurses-dev \
    bc \
    && apt-get clean && apt-get purge

# Download and extract Samtools
RUN wget https://github.com/samtools/samtools/releases/download/1.15.1/samtools-${SAMTOOLS_VERSION}.tar.bz2 && \
    tar -xjf samtools-${SAMTOOLS_VERSION}.tar.bz2 && \
    rm samtools-${SAMTOOLS_VERSION}.tar.bz2

# Build and install Samtools
# WORKDIR /samtools-${SAMTOOLS_VERSION}
RUN cd /samtools-${SAMTOOLS_VERSION} && \
    ./configure && \
    make && \
    make install

# # Set the entrypoint to Samtools
# ENTRYPOINT ["samtools"]