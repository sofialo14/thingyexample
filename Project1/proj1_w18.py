import requests
import json

json_file = open('sample_json.json', 'r')
json_str = json_file.read()
json_dict = json.loads(json_str)
json_file.close()

class Media:
	def __init__(self, title="No Title", author="No Author", release_year="No Release Year", json_1=None):
		for item in json_dict:
			if json_1 is not None:
				self.title = json_dict["trackName"]
				self.author = json_dict["artistName"]
				self.year = json_dict["releaseDate"][:5]

			else:
				self.title = title
				self.author = author
				self.year = release_year

	def __str__(self):
		return "{} by {} ({})".format(self.title, self.author, self.year)

	def __len__(self):
		return 0



## Other classes, functions, etc. should go here

class Song(Media):
	def __init__(self, title="No Title", author="No Author", release_year="No Release Year", alb="No Album", genre="No Genre", track_len="No Track Length", json_1=None):
		super().__init__(title, author, release_year)
		for item in json_dict:
			if json_1 is not None:
				self.album = json_dict["collectionName"]
				self.track_length = json_dict["trackTimeMillis"]
				self.genre = json_dict["primaryGenreName"]

			else:
				self.album = alb
				self.track_length = track_len
				self.genre = genre

	def __str__(self):
		return "{} [{}]".format(super().__str__(), self.genre)

	def __len__(self):
		return (len(self.track_length))



class Movie(Media):
	def __init__(self, title="No Title", author="No Author", release_year="No Release Year", rating="No Rating", movie_len="No Movie Length", json_1=None):
		super().__init__(title, author, release_year)
		for item in json_dict:
			if json_1 is not None:
				self.rate = json_dict["contentAdvisoryRating"]
				self.movie_length = json_dict["trackTimeMillis"]

			else:
				self.rate = rating
				self.movie_length = movie_len

	def __str__(self):
		return "{} [{}]".format(super().__str__(), self.rate)

	def __len__(self):
		return len(self.movie_length)

if __name__ == "__main__":
	# your control code for Part 4 (interactive search) should go here
	pass
