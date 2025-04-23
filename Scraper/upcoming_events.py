#Import libraries for web-scraping and saving to CSV file.
import requests
import bs4
import re
import csv
import os
import pandas as pd

#Define paths for url folder and scraped files folder
url_path = os.getcwd() + '/urls'
file_path = os.getcwd() + '/scraped_files'

def scrape_upcoming():
    
    with open(file_path + '/' + 'upcoming_events.csv','w',newline="",encoding='UTF8') as csv_file:
            writer = csv.writer(csv_file)
            
            writer.writerow(['event_name',
                             'date',
                             'fighter_1',
                             'fighter_2',
                             'division',
                             'event_url'
                            ])

            upcoming = pd.read_csv('urls/event_urls.csv',header=None,names = ['events'])
            upcoming_event = upcoming['events'][0]
            fight_url = requests.get(upcoming_event)
            fight_soup = bs4.BeautifulSoup(fight_url.text,'lxml')

            date_tag = fight_soup.find('i', class_='b-list__box-item-title')
            if date_tag:
                date = date_tag.find_next_sibling(string=True).strip()
            else:
                date = 'Not Found'
            event_name = fight_soup.h2.text.strip()

            fight_soup = fight_soup.select('p.b-fight-details__table-text')
            temp = [ele.get_text().strip() for ele in fight_soup if len(ele.get_text().strip())>0 and ele.get_text().strip() != 'View Matchup']
            counter = 3
            for ele in temp[::3]:
                writer.writerow([
                    event_name,
                    date,
                    temp[counter-3],
                    temp[counter-2],
                    temp[counter-1],
                    upcoming_event
                ])
                counter = counter + 3 