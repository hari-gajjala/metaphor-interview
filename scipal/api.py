from typing import List
from metaphor_python import Metaphor
import os

metaphor = Metaphor(api_key=os.environ.get('METAPHOR_API_KEY'))

def get_similar_url(url: str, start_crawl_date: str):
    results = metaphor.find_similar(
        url,
        num_results=6,
        start_crawl_date=start_crawl_date,
    )

    return results


def search_url(paper_topic: str, paper_type: str, start_crawl_date: str):
    """
    paper_topic: [review article, original research article, clinical paper, perspective/opinion article]
    """

    response = metaphor.search(
        f"{paper_type} about the topic of {paper_topic}.",
        num_results=6,
        start_crawl_date=start_crawl_date,
    )

    return response


def get_html(doc_ids: List[str]):
    response = metaphor.get_contents(doc_ids)

    return response


# response = search_url("covid", "review article", "2021-01-01")
#
# for result in response.results:
#     print(get_html(result.id))
#     print('------------------------------')

