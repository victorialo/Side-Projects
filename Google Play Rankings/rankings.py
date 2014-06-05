from bs4 import BeautifulSoup
import urllib.request
import re
import requests

# def pull(addr):
# 	#main function
# 	print ("Pulling categories...")
# 	url = urllib.request.urlopen(addr)
# 	contents = url.read().decode()
# 	soup = BeautifulSoup("".join(contents))
# 	f = open('ranklist.txt','w')
# 	print("opened file")
	
# 	for li in soup.find_all("li", {"class": "child-submenu-link-wrapper"}):
# 		print(str(li))
# 		catlink = addr + li.get('href')
# 	# for category in soup.find_all("a", {"class": "child-submenu-link"}):
# 		# catlink = addr + category.get('href')
# 		print(catlink)
# 		# f = open('ranklist.txt','w')
# 		# catname = category.get('title')
# 		# f.write("\n" + catname + "\n")
# 		f.close()
# 		pullcat(catlink)

# 	url.close()
# 	return


def pullcat(addr):
	#pulls from each category
	print("Initializing file...\n")
	f = open('ranklist.txt','w')
	# with open("ranklist.txt", "w") as f:
	url = urllib.request.urlopen(addr)
	contents = url.read().decode()
	soup = BeautifulSoup("".join(contents))
	category = soup.find("title", {"id": "main-title"}).string
	f.write(str(category) + '\n\n') # write title

	#top paid ranking
	print("Generating paid rankings...\n")
	paid = addr + "/collection/topselling_paid"
	# paidurl = urllib.request.urlopen(paid)
	# paidurl = urllib.request.urlopen(paid)
	number = 0
	f.write("Top-selling Paid Apps\n")
	while number <= 480:
		payload = {'start': number, 'num':60}
		r = requests.post(paid, data=payload)
		# print(payload)
		paidsoup = BeautifulSoup(r.text)
		f.close()
		pullrank(r, paidsoup, "paid","ranklist.txt", number)
		number += 60

	f = open('ranklist.txt','a+')
	f.write("\n\n")
	#top free ranking
	print("\nGenerating free rankings...\n")
	free = addr + "/collection/topselling_free"
	# freeurl = urllib.request.urlopen(free)
	# freecontents = freeurl.read().decode()
	# freesoup = BeautifulSoup("".join(freecontents))

	# pullrank(free, freesoup, "free", "ranklist.txt",)

	number = 0
	f.write("Top-selling Free Apps\n")
	while number <= 480:
		payload = {'start': number, 'num':60}
		r = requests.post(free, data=payload)
		# print(payload)
		freesoup = BeautifulSoup(r.text)
		f.close()
		pullrank(r, freesoup, "free","ranklist.txt", number)
		number += 60


	# f.close() # you can omit in most cases as the destructor will call if
	url.close()
	return


def pullrank(url, soup, catname, filename, rank):
	#function to pull ranks
	f = open(filename,'a+')
	# rank = 0
	# while rank <= 500: 
		# for link in soup.find_all('<span class="preview-overlay-container"'):
	for link in soup.find_all("span", {"class": "preview-overlay-container"}):
		if rank < 540:
			appname = link.get('data-docid')
			rank += 1
			print("writing app " + appname + " of rank " + str(rank))
			f.write(catname + ", " + appname + ", " + str(rank) + "\n" ) # write title
			# name = soup.find(id="main-title")
			# payload = {'start': rank+60}
			# requests.post(url, data=payload)

	f.close()
	return

pullcat("https://play.google.com/store/apps/category/BOOKS_AND_REFERENCE")