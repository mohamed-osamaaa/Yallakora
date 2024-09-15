import requests
from bs4 import BeautifulSoup
import csv

date = input("Please enter a Date in the following format MM/DD/YYYY: ")
#exception
page = requests.get(f"https://www.yallakora.com/match-center/?date={date}")

def main(page):
    src = page.content
    soup = BeautifulSoup(src, "lxml")
    
    matches_details = []
    
    championships = soup.find_all("div", {'class':'matchCard'})
    
    def get_match_info(championship):
        try:
            championship_title = championship.contents[1].find('h2').text.strip()
            all_matches = championship.contents[3].find_all('div')
            number_of_matches = len(all_matches)
        except (IndexError, AttributeError):
            return
        
        for i in range(number_of_matches):
            try:
                # get teams names
                team_A = all_matches[i].find('div', {'class':'teamA'}).text.strip()
                team_B = all_matches[i].find('div', {'class':'teamB'}).text.strip()
                # get score
                match_result = all_matches[i].find('div', {'class':'MResult'}).find_all('span', {'class':'score'})
                score = f"{match_result[0].text.strip()} - {match_result[1].text.strip()}"
                # get match time
                match_time = all_matches[i].find('div', {'class':'MResult'}).find('span', {'class':'time'}).text.strip()
                # add match info to matches_details
                matches_details.append({'نوع البطولة': championship_title,
                                        'الفريق الاول': team_A,
                                        'الفريق الثاني': team_B,
                                        'ميعاد المباراة': match_time,
                                        'النتيجة': score})
            except (AttributeError, IndexError):
                continue 
    
    for championship in championships:
        get_match_info(championship)
    
    if matches_details:
        keys = ['نوع البطولة', 'الفريق الاول','الفريق الثاني', 'ميعاد المباراة', 'النتيجة']

        with open('E:\\Projects\\Web Scraping\\Yallakora\\matches-details.csv', 'w', newline='', encoding='utf-8') as output_file:
            dict_writer = csv.DictWriter(output_file, keys)
            dict_writer.writeheader()
            dict_writer.writerows(matches_details)
            print("File created")
    else:
        print("No match data found")

main(page)
