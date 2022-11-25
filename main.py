from wikipedia_scraper import WikipediaScraper


def main():
    wikipedia_scraper = WikipediaScraper()
    wikipedia_scraper.scrap_data('category:Software')


if __name__ == '__main__':
    main()