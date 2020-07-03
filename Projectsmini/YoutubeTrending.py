# Python script for fetching Top trending videos/music on Youtube and top query result for a website.
# Tech Used: Youtube data API, requests

import json
import requests

API_KEY = "##########################"
len = 5

def trending_videos():
	print("\nTop 5 trending videos on youtube\n")
	URL = "https://www.googleapis.com/youtube/v3/videos?part=snippet&status&chart=mostPopular&regionCode=IN&maxResults=5&key="+API_KEY	
	response = 	requests.get(URL)
	data = json.loads(response.content)
	for i in range(0,len):
		print(str(i+1)+" on Trending -> "+data["items"][i]["snippet"]["title"])	

def trending_music():
	print("\nTop 5 trending music videos\n")
	ID = "PLFgquLnL59amuLdoZOti1JkiCckjn9Slb"
	URL = "https://www.googleapis.com/youtube/v3/playlistItems?playlistId="+ID+"&fields=items&part=snippet&maxResults=5&key="+API_KEY
	response = requests.get(URL)
	data = json.loads(response.content)
	for i in range(0,len):
		print(str(i+1)+". "+data["items"][i]["snippet"]["title"])

def youtube_search():
	while True:
		val = raw_input("Enter your query -> ")
		if(val=="q"):
			break
		URL = "https://www.googleapis.com/youtube/v3/search?part=snippet&q="+val+"&regionCode=IN&maxResults=5&key="+API_KEY
		r = requests.get(URL)
		data = json.loads(r.content)
		for i in range(0,len):
			print(str(i+1)+". "+data["items"][i]["snippet"]["title"])
		print("\n")

if __name__ == "__main__":
	trending_videos()
	trending_music()
	print("\nTop 5 result for your query\n")
	print("Enter q to quit\n")
	youtube_search()
