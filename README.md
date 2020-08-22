# web-scraping-demo-using-scrapy-spiders
This project is a simple web scraping program, base on scrapy spiders. It's main purpose is to extract a different companies informations from a list of websites contained in the **urls.txt** file.
Most of the targetted data is contained in html **h1** tags and also in **li** tags.</br>
## Running spiders for extraction
To strat the data extraction, open terminal in root of the repository, and run following commands:
### Extracting companies names from **h1** tags
In the opened terminal run :
```
scrapy crawl h1_tags

```

### Extracting companies informations from **li** tags
In the opened terminal run :
```
scrapy crawl li_tags

```
The resulting data will be saved in the two **.txt** files **h1_tags_files.txt** and **li_tags_file.txt**
