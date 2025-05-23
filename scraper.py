from Scraper import get_urls, events, fights, fightstats, fighters, upcoming_events, normalise_tables
def main():

#     #Scrapes all urls from ufcstats.com
#     get_urls.get_event_urls()
#     get_urls.get_fight_urls()
#     get_urls.get_fighter_urls()

#     #Iterates through urls and scrapes key data into csv files
    events.scrape_events()
    fights.scrape_fights()
    fightstats.scrape_fightstats()
    fighters.scrape_fighters()
    upcoming_events.scrape_upcoming()

    #Normalises tables for clean final output
#     normalise_tables.normalise_tables()

if __name__ == '__main__':
    main()
