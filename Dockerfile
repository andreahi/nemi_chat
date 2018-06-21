FROM amd64/python:3.5.5-jessie
ADD nemi_bot /usr/share
ADD requirements.txt /usr/share
WORKDIR /usr/share/
RUN chmod -R g+rwx /usr/share/
RUN pip install --upgrade https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-1.8.0-cp35-cp35m-linux_x86_64.whl
RUN pip install -r requirements.txt
RUN python -m spacy download xx_ent_wiki_sm
RUN python -m spacy link xx_ent_wiki_sm xx
CMD [ "python", "run_server.py" ]
