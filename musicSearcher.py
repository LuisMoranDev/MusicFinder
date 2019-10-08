import requests 
from bs4 import BeautifulSoup as bs 

lyrics = input("Please provide lyrics of the song: ")

# lyrics = "not good enough for the truth"
lyrics = lyrics.split()
final = '+'.join(lyrics)

page = requests.get('https://search.azlyrics.com/search.php?q=' + final)
soup = bs(page.text, 'html.parser')

delete_lyrics = soup.find('small')
delete_lyrics.decompose()
band_info_list = soup.find(class_='panel')
band_info_items = band_info_list.find_all('tr')
if len(band_info_items) < 1:
	print("sorry no song was found")
else:
	count = 0
	print("Here are three top three results")
	for i in range(1,len(band_info_items)-1):
		if count < 3:
			band_info_items[i].small.decompose()
			band_info_items[i] = band_info_items[i].get_text()
			print(band_info_items[i].strip())
			count += 1
