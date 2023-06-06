# Use an official Python runtime as a parent image
FROM continuumio/miniconda3

RUN apt-get --allow-releaseinfo-change update
RUN apt-get install -y build-essential 

RUN mkdir /tmp/hicomp
COPY ./ /tmp/hicomp/
RUN pip install /tmp/hicomp

RUN rm -rf /tmp/hicomp

ENTRYPOINT ["/opt/conda/bin/hicompcmd.py"]

CMD ["--help"]
