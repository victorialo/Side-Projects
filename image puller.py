import urllib.request

def get(url, newname, maxi):
	count = 1
	while count in range(1,maxi+1):
		url2 = url + str(count) + ".JPG"
		print(url2 + " is being downloaded...")
		urllib.request.urlretrieve(url2, newname + str(count) + ".JPG")
		count+=1

get("http://www.photomomentum.com/clients/uc/ucb/adm/images/ucb-", "Admissions ", 347)