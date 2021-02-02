FROM python:3.6

WORKDIR /home/jovyan

USER root

RUN pip install jupyter  jupyterlab
COPY kubectl /usr/bin/kubectl

ARG NB_USER=jovyan
EXPOSE 8888

ENV NB_USER $NB_USER
ENV NB_UID=1000
ENV HOME /home/$NB_USER
ENV NB_PREFIX /

CMD ["sh", "-c", "jupyter lab --notebook-dir=/home/jovyan --ip=0.0.0.0 --no-browser --allow-root --port=8888 --LabApp.token='' --LabApp.password='' --LabApp.allow_origin='*' --LabApp.base_url=${NB_PREFIX}"]

