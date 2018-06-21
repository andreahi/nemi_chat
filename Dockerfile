FROM amd64/python:3.5.5-jessie
USER root
ADD nemi_bot /
ADD requirements.txt /
WORKDIR /
RUN export LD_RUN_PATH=/usr/local/lib
RUN yum install -y graphviz
RUN yum install -y libgraphviz-dev
RUN pip install --upgrade https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-1.8.0-cp36-cp36m-linux_x86_64.whl
RUN pip install -r requirements.txt
RUN python -m spacy download xx_ent_wiki_sm
RUN python -m spacy link xx_ent_wiki_sm xx
CMD [ "python", "run_server.py" ]
