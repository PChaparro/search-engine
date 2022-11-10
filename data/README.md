# 💾 Data collection

Using the [youtube-scraper](https://github.com/PChaparro/youtube-scraper) package, data from 1000 youtube videos were collected using 2200 YouTube Data API v3 quotas, that is, **22% of the daily available quotas**.

Execution time (**Obtaining 100 videos for each query**): 

![image](https://user-images.githubusercontent.com/94259578/201221913-b6d106ba-ea50-44d9-9e6c-6b1a2ed07be3.png)

From `scraping/` run: 

```
go mod tidy
go run main.go
```

# 📝 Data "cleansing"

Using regular expressions on python, unwanted characters, like emojis, urls and linebreaks were deleted.

Fom `cleansing/` run: 

```
(optional) virtualenv -p python3 venv
(optional) source venv/bin/activate

pip install notebook 
jupyter notebook
```

Then, open the `cleansing.ipynb` file.
