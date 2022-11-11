# Search engine back-end


## 👀 Preview:

<p align="center">
  <img src="https://user-images.githubusercontent.com/94259578/201445688-b91f8ef3-992c-4d4a-8ea0-8cccc4ee28e8.png" width="680px"/>
</p>

## 🛠️ Install and run

### Setup opensearch

1. Run the `docker-compose` file. From `backend/`:

```bash
docker-compose up
```

2. Create the `open search` index and insert the data:

**Note:** Before perform this step you must complete the data recollection (`data/scraping`) and data cleansing (`data/cleansing`) steps.

```bash
(optional) virtualenv -p python3 venv
(optional) source venv/bin/activate

pip install notebook 
jupyter notebook
```

Then, open and run the `setup_opensearch.ipynb` file.

### Start the python API

**Note:** Before perform this step, the `docker-compose` file should be running an the data should be already inserted on `open search`.

```bash
(optional) virtualenv -p python3 venv
(optional) source venv/bin/activate

pip install -r requirements.txt
python app.py
```
