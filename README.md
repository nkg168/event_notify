# flow
1. scrape web site
2. tweet

# Debugging
if using VSCode, update launch.json's configurations to include the "Scrapy" configuration as seen below:
```
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
