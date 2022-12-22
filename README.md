## Setup
- _Python 3.9_
- _Scrapy framework_

## Create a scrapy project
```
scrapy startproject indicators
```
## Test scraping
> X-Path - Javascript console
```
$x('//section[contains(@class, "article-content") and @itemprop="articleBody"]//table//h2/strong/text()').map(e => e.wholeText)
```

```
$x('//section[contains(@class, "article-content") and @itemprop="articleBody"]//table//h1/text()').map(e => e.wholeText)
```

> Scrapy console
```
scrapy shell "https://www.dane.gov.co/index.php/indicadores-economicos"
```

> X-Path - Scrapy console
```
response.xpath('//section[contains(@class, "article-content") and @itemprop="articleBody"]//table//h2/strong/text()').getall()
```
## Run locally
> Execute spider with scrapy
```
scrapy crawl e_indicators
```
