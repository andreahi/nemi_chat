### Prerequisite for local dev
Linux:  
pip install --upgrade https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-1.8.0-cp35-cp35m-linux_x86_64.whl

Mac:  
pip install --upgrade https://storage.googleapis.com/tensorflow/mac/cpu/tensorflow-1.8.0-py3-none-any.whl


pip install -r requirements.txt
python -m spacy download xx_ent_wiki_sm
python -m spacy link xx_ent_wiki_sm xx


### Building and running with Docker
docker build -t nemi .

docker run -p5005:5005 nemi
