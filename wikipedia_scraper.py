import requests


class WikipediaScraper:
    def __init__(self):
        self.URL = "https://en.wikipedia.org/w/api.php"
        self._categories = []

    def scrap_data(self, category):
        pages = self._fetch_category_data(category)
        local_results = []
        for page in pages:
            self._handle_result(category, local_results, page)
        self._categories.append(category)
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

    def _handle_result(self, category, local_results, page):
        if page['title'].startswith('Category:') and category not in self._categories:
            self.scrap_data('c' + page['title'][1:])
        else:
            local_results.append(page['title'])

    @staticmethod
    def _save_to_file(category, local_results):
        try:
            with open(f"result/{category}.txt", 'w+') as final_result:
                for article in local_results:
                    final_result.write(article + "\n")
        except Exception as e:
            print(f"Exception! {e}")