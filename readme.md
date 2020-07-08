# Bob Rasa Server

For the moment as the intent detector of the system, supposedly later become the centralized answer server of the whole system

## Set up

It is highly recommended that you create a separate env for rasa (preferably a conda env)

```bash
conda create -n rasa
```

Then install all necessary packages with
```bash
pip install rasa[spacy]
```

As we use Spacy, you need to download the `fr` language data corpse of spacy
```bash
python -m spacy download fr_core_news_md
python -m spacy link fr_core_news_md fr
```

> In case you don't want to use GPUs when running rasa, you can use the following command to hide your gpus from tensorflow
```bash
export CUDA_VISIBLE_DEVICES=-1
```

## How to use rasa service 

Start Rasa server by running:
```bash
rasa run -m models --enable-api --log-file out.log # models is the directory containing all trained rasa models
```
(In case you have custom actions, you would also need to start __rasa actions__ server as well by running:
```bash
rasa run actions --actions actions # the last 'actions' is the filename defining custom actions
```
)
And on another terminal, you can test by typing:
```bash
curl http://localhost:5005/webhooks/rest/webhook -d '{"message":"t es quoi", "sender": "quang"}'
```

## How to use only Rasa NLU

```bash
rasa run --enable-api -m models --cors "*" --debug # the filepath can be changed to any model's path you have trained
```

and use it by typing:
```bash
curl localhost:5005/model/parse -d '{"text":"hello"}'
```