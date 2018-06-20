### Space install:

python3 -m spacy download en_core_web_md
python3 -m spacy link en_core_web_md en


xx_ent_wiki_sm


### Starting docker

docker build -t nemi .
docker run -p5005:5005 nemi
