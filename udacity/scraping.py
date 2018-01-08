def find_first_link(url):
    response = requests.get(url)
    html = response.text
    soup = bs4.BeautifulSoup(html, "html.parser")

    # TODO: find the first link in the article, or set to None if
    # there is no link in the article.
    article_link = "a url, or None"

    if article_link:
        return article_link
