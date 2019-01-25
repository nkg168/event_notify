# Introduction
This is sample app for Web Scraping in Python using Scrapy

# flow

1. scrape web site
2. check update
3. tweet

## setup

if you use chromedriver and it's not installed

`brew cask install chromedriver`

Start redis-server

`docker-compose -f "docker-compose.yml" up -d --build`

Set environ variable in .env that pipenv loads

```.env
cp example.env .env
vi .env
```

## run

run Web Scraping

`pipenv run scrapy crawl eventsite`

## Debugging

if using VSCode, update launch.json's configurations to include the "Scrapy" configuration as seen below:

```json
{
   "version": "0.2.0",
    "configurations": [
        {
            "name": "Scrapy",
            "type": "python",
            "request": "launch",
            "module": "scrapy",
            "args": [
                "crawl",
                "eventsite",
            ]
        }
    ]
}
```
