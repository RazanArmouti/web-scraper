import requests
from bs4 import BeautifulSoup


def get_citations_needed_count(url):
    """
    arguments: url
    return: integer
    """
    res = requests.get(url)
    b_soup=BeautifulSoup(res.text,"html.parser")
    result = b_soup.find_all("a",title="Wikipedia:Citation needed")
    return len(result)

def get_citations_needed_report(url):
    """
    arguments: url
    return :formated string
    """
    citation = []
    res = requests.get(url)       
    b_soup = BeautifulSoup(res.text,"html.parser")
    results = b_soup.find_all("a", title="Wikipedia:Citation needed")
   

    for result in results:
        citation.append(result.parent.parent.parent.text)

    final = '\n'.join(citation)
    return final


if __name__=="__main__":
    wikipedia_url="https://en.wikipedia.org/wiki/History_of_Mexico"
    print(get_citations_needed_count(wikipedia_url))
    print(get_citations_needed_report(wikipedia_url))
