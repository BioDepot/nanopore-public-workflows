FROM biodepot/dorado:0.5.3__ubuntu-22.04
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y samtools && apt-get clean -y && apt-get autoclean -y && apt-get autoremove -y && rm -rf /var/lib/apt/lists/*   
COPY runDorado.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/runDorado.sh