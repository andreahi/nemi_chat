### Spacy install:

python3 -m spacy download xx_ent_wiki_sm
python3 -m spacy link xx_ent_wiki_sm xx


### Starting docker

docker build -t nemi .
docker run -p5005:5005 nemi
