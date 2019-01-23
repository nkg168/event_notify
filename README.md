# flow

1. scrape web site
2. check update
3. tweet

## setup

if you use chromedriver and it's not installed
`brew cask install chromedriver`

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

## environ variable

pipenv load .env

```.env
cp example.env .env
vi .env
```