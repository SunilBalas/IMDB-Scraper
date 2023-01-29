# IMDb Scraper
This Scraper is built using Scrapy, a powerful and flexible web scraping framework for Python. It allows you to scrape information from the IMDb website and save it in a structured format such as CSV or JSON.

## Installation
1. Install Scrapy using pip: 
```
pip install scrapy
```
2. Clone this repository: 
```
git clone https://github.com/SunilBalas/IMDB-Scraper.git
```
3. Navigate to the project directory: 
```
cd imdb_scraper
```

## Usage
To scrape top movies in India and US region, run the following command:
```
scrapy crawl top_movies -O top_movies.json
```

To scrape upcoming movies in India and US region, run the following command:
```
scrapy crawl upcoming_release -O upcoming_releases.json
```

## Output
The scraped data will be saved in the specified output file in CSV or JSON format. The data will include the following fields:

For Top Movies:
 - title: The title of the movie
 - year: The release year of the movie
 - rating: The IMDb rating of the movie

For Upcoming Movies:
 - title: The title of the movie
 - release date: The release date of a movie
 - genre: The genre of the movie
 - cast: A list of the main actors in the movie
 
## Note
Using this scraper to scrape data from the IMDb website is against their terms of service. It should be used only for testing and educational purposes.
Always be respectful of the website's terms of service and robots.txt file.

## Contribution
Feel free to contribute to this project by submitting pull requests or by reporting any issues you encounter.
