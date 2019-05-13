import arxiv
import time

results = arxiv.query(search_query = "breaking bad", max_results = 100)

for article in results:
    print(article["title"])
    print(article["summary"])
    print()
    time.sleep(0.5)
