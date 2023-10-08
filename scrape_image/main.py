from scrape import scrape
from process_html import process_html_responses


if __name__=="__main__":

    try:
        scrape()

        process_html_responses()
    except Exception as e:
        print(e)


