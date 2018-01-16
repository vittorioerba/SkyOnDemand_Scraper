# Sky On Demand - Scraper   

I found SkyOnDemand's UI really difficoult to use. I mainly want to be able to sort the available movies by online ranking (like IMDB, TMDB and so on).

For the moment, I wrote two scripts to get started.

# sky\_on\_demand\_scraper.py

This script retrives the movie list from the "A-Z" list page. The results are saved in a csv file, with titles, year of release and nationality.

The main problem I had was given by the _inifinte scrolling_ feature of the pages. 
I tracked the network requests of the page as I scrolled down, finding the urls of all the components loaded by the page.  
The script keeps on requesting these pages incrementally, until it finds a _404: Page not found_ error. Then it stops and moves on to the next letter.

# sky\_on\_demand\_votes.py

This script interfaces with the free API of [https://www.themoviedb.org](TMDB) and gets ranking and description of every movie in the inut csv file.

# infinity

I recently added a couple of analogous scripts for Mediaset Infinity. Main
probelm was that the content in their pages is dynamically loaded after the
source is sent out, so that I had to figure out which request pointed to the
right data. Then it was just reading a json and stripping the titles.
