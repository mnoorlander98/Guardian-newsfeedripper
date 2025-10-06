#hi

import newspaper
import feedparser
import pandas as pd

def scrape_news_from_feed(feed_url):
    articles= []
    feed = feedparser.parse(feed_url)
    for entry in feed.entries:
        # create a newspaper article object
        article = newspaper.Article(entry.link)
        # download and parse the article
        article.download()
        article.parse()
        # extract relevant information
        articles.append({
            'title': article.title,
            'author': article.authors,
            'publish_date': article.publish_date,
            'content': article.text
        })
    return articles


feed_url='https://www.theguardian.com/uk/rss'
articles = scrape_news_from_feed(feed_url)


#print extracted articles
for article in articles:
    print('Title:', article['title'])
    print('Author:', article['author'])
    print('Publish Date:', article['publish_date'])
    print('Content:', article['content'])
    print()
