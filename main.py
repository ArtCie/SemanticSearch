from corpus.wikipedia_scraper import WikipediaScraper
from corpus.corpus_builder import CorpusBuilder
from GUI.interface_main import InterfaceMain


def main():
    # wikipedia_scraper = WikipediaScraper()
    # wikipedia_scraper.scrap_data('category:Software')

    # corpus_builder = CorpusBuilder()
    # corpus_builder.build_corpus_file()
    # corpus = corpus_builder.build_corpus()
    # print(corpus)

    gui = InterfaceMain()
    gui.draw()




if __name__ == '__main__':
    main()
