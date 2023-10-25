from django.shortcuts import render
from django.http import HttpResponse
from typing import List
from metaphor_python import Metaphor
import os

def index(request):
    return render(request, "scipal/index.html", {})

def results(request):
    return render(request, "scipal/results.html", {})


def find(request):
    scientific_domains = [
        "academic.oup.com",
        "ncbi.nlm.nih.gov",
        "pubmed.ncbi.nlm.nih.gov",
        "sciencedirect.com",
        "onlinelibrary.wiley.com",
        "link.springer.com",
        "ahajournals.org",
        "acc.org",
        "oup.com",
        "nature.com",
        "jamanetwork.com",
        "thelancet.com",
        "ahajournals.org",
        "oup.com",
        "bmj.com",
        "futuremedicine.com",
        "dovepress.com",
        "elsevier.com",
        "cell.com",
        "springer.com",
        "frontiersin.org",
        "pubs.acs.org",
        "springer.com",
        "nejm.org",
        "crf.org",
        "plos.org",
        "lww.com",
        "rsc.org",
        "nature.com",
        "lww.com",
        "science.org",
        "controlledreleasesociety.org",
        "asianpubs.org",
        "webofscience.com",
    ]

    comment = request.POST['comment']
    doc_type = request.POST['docType']
    crawl_date = request.POST['crawlDate']
    if not comment or not doc_type or not crawl_date:
        return render(
            request,
            "scipal/index.html",
            {
                "error_message1" : "Please fill all fields of Choice 1",
            },
        )

    metaphor = Metaphor(api_key=os.environ.get('METAPHOR_API_KEY'))
    response = metaphor.search(
        f"{doc_type}s about the topic of {comment}.",
        num_results=6,
        start_crawl_date=crawl_date,
        include_domains=scientific_domains,
    )

    return render(request, "scipal/results.html", {'results': response.results})


def similar(request):
    scientific_domains = [
        "academic.oup.com",
        "ncbi.nlm.nih.gov",
        "pubmed.ncbi.nlm.nih.gov",
        "sciencedirect.com",
        "onlinelibrary.wiley.com",
        "link.springer.com",
        "ahajournals.org",
        "acc.org",
        "oup.com",
        "nature.com",
        "jamanetwork.com",
        "thelancet.com",
        "ahajournals.org",
        "oup.com",
        "bmj.com",
        "futuremedicine.com",
        "dovepress.com",
        "elsevier.com",
        "cell.com",
        "springer.com",
        "frontiersin.org",
        "pubs.acs.org",
        "springer.com",
        "nejm.org",
        "crf.org",
        "plos.org",
        "lww.com",
        "rsc.org",
        "nature.com",
        "lww.com",
        "science.org",
        "controlledreleasesociety.org",
        "asianpubs.org",
        "webofscience.com",
    ]

    similar_url = request.POST['similarUrl']
    crawl_date = request.POST['crawlDate2']
    if not similar_url or not crawl_date:
        return render(
            request,
            "scipal/index.html",
            {
                "error_message2" : "Please fill all fields of Choice 2",
            },
        )

    metaphor = Metaphor(api_key=os.environ.get('METAPHOR_API_KEY'))
    results = metaphor.find_similar(
        similar_url,
        num_results=6,
        start_crawl_date=crawl_date,
        include_domains=scientific_domains,
    )


    return render(request, "scipal/results.html", {'results': results.results})