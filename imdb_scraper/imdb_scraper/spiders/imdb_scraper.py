from scrapy import Spider
from scrapy.selector import Selector
import pycountry as pyc

from imdb_scraper.items import ImdbScraperItem

class TopMoviesSpider(Spider):
    name = "top_movies"
    allowed_domains = ["imdb.com"]
    start_urls = [
        "https://www.imdb.com/chart/top/?ref_=nv_mv_250",
    ]

    def parse(self, response):
        movies = Selector(response).css("tbody.lister-list tr")

        for movie in movies:
            item = ImdbScraperItem()

            item["title"] = movie.css("td.titleColumn a::text").get()
            item["year"] = movie.css("td.titleColumn span.secondaryInfo::text").get().strip("()")
            item["ratings"] = movie.css("td.ratingColumn.imdbRating strong::text").get()

            yield item


class UpcomingReleaseSpider(Spider):
    name = "upcoming_release"
    allowed_domains = ["imdb.com"]

    region = input("Enter your country(eg., IN, US): ")
    type = input("Enter the type(eg., MOVIE, TV): ")
    
    start_urls = ["https://www.imdb.com/calendar/?ref_=rlm&region={0}&type={1}".format(region, type)]

    def parse(self, response):
        print("=====================================RESPONSE========================================")
        upcoming_movies_data = Selector(response).css("section.ipc-page-section.ipc-page-section--base article.sc-f56042d2-1.kgXUZB")
        
        for movies_data in upcoming_movies_data:
            # Fetch the release date
            release_date = movies_data.css("div h3.ipc-title__text::text").get()
            # Fetch all the movies 
            movies = movies_data.css('ul li[data-testid="coming-soon-entry"]')

            for movie in movies:
                # Get the movie title
                title = movie.css("div a.ipc-metadata-list-summary-item__t::text").get()

                # Fetch all the genres associate with the movie
                genre_data = movie.css("div ul.ipc-metadata-list-summary-item__tl li")
                genres = [genre.css("span::text").get() for genre in genre_data]

                # Fetch all the casts associate with the movie
                cast_data = movie.css("div ul.ipc-metadata-list-summary-item__stl li")
                casts = [cast.css("span::text").get() for cast in cast_data]

                yield {
                    "title" : title,
                    "release_date" : release_date,
                    "genres" : genres,
                    "casts" : casts
                }