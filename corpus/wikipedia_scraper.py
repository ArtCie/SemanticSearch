import requests


class WikipediaScraper:
    """
    Class to scrap Wikipedia articles from given category

    Attributes:
        URL                 Wikipedia API URL
        CATEGORY_LIMIT      Limit of categories to search
        _categories         List of categories -> prevents recursive loop
        _articles           List of articles -> prevents duplications
    """
    def __init__(self):
        self.URL = "https://en.wikipedia.org/w/api.php"
        self.CATEGORY_LIMIT = 2000
        self._categories = []
        self._articles = []

    def scrap_data(self, category):
        print(f"Handling {category}")
        self._categories.append(category)
        pages = self._fetch_category_data(category)
        local_results = []
        for page in pages:
            self._handle_result(local_results, page)
        self._save_to_file(category[9:], local_results)

    def _fetch_category_data(self, category):
        DEFAULT_PARAMS = {
            "action": "query",
            "cmtitle": category,
            "cmlimit": "50",
            "list": "categorymembers",
            "format": "json"
        }
        result = requests.get(url=self.URL, params=DEFAULT_PARAMS)
        return result.json()['query']['categorymembers']

    def _handle_result(self, local_results, page):
        new_category = 'c' + page['title'][1:]
        if page['title'].startswith('Category:') and new_category not in self._categories and \
                len(self._categories) < self.CATEGORY_LIMIT:
            self.scrap_data(new_category)
        elif page['title'] not in self._articles and not self._is_prefix(page['title']):
            local_results.append(page['title'])
            self._articles.append(page['title'])

    @staticmethod
    def _is_prefix(title: str):
        return title.startswith('File:') or title.startswith('Template:') or title.startswith('Category:')

    @staticmethod
    def _save_to_file(category, local_results):
        try:
            if local_results:
                with open(f"result/{category}.txt", 'w+') as final_result:
                    for article in local_results:
                        final_result.write(article + "\n")
        except Exception as e:
            print(f"Exception! {e}")
