import unittest
import proj1_w18 as proj1

class TestMedia(unittest.TestCase):

    def testConstructor(self):
        m1 = proj1.Media()
        m2 = proj1.Media("1999", "Prince", "1970")

        self.assertEqual(m1.title, "No Title")
        self.assertEqual(m1.author, "No Author")
        self.assertEqual(m2.title, "1999")
        self.assertEqual(m2.author, "Prince")
        self.assertEqual(m1.year, "No Release Year")
        self.assertEqual(m2.year, "1970")

    def testConstructor_Song(self):
        s1 = proj1.Song()
        s2 = proj1.Song("Crazy In Love", "Beyonce", "2003", "Dangerously In Love", "R&B", 180)

        self.assertEqual(s1.album, "No Album")
        self.assertEqual(s1.track_length, "No Track Length")
        self.assertEqual(s1.genre, "No Genre")
        self.assertEqual(s2.album, "Dangerously In Love")
        self.assertEqual(s2.track_length, 180)
        self.assertEqual(s2.genre, "R&B")

    def testConstructor_Movie(self):
        mv1 = proj1.Movie()
        mv2 = proj1.Movie("Spotlight", "Tom McCarthy", "2015", "R", 128)

        self.assertEqual(mv1.rate, "No Rating")
        self.assertEqual(mv1.movie_length, "No Movie Length")
        self.assertEqual(mv2.rate, "R")
        self.assertEqual(mv2.movie_length, 128)

    def testConstructor_String(self):
        m3 = proj1.Media("1999", "Prince", "1970")
        self.assertEqual(m3.__str__(), "1999 by Prince (1970)")

        s3 = proj1.Song("Crazy In Love", "Beyonce", "2003", "Dangerously In Love", "R&B", 180)
        self.assertEqual(s3.__str__(), "Crazy In Love by Beyonce (2003) [R&B]")

        mv3 = proj1.Movie("Spotlight", "Tom McCarthy", "2015", "R", 128)
        self.assertEqual(mv3.__str__(), "Spotlight by Tom McCarthy (2015) [R]")

    def testConstructor_Length(self):
        m4 = proj1.Media()
        self.assertEqual(m4.__len__(), 0)

        # s4 = proj1.Song(track_len=180)
        # self.assertEqual(s4.__len__(), 180)
        #
        # mv4 = proj1.Movie(movie_len=128)
        # self.assertEqual(mv4.__len__(), 128)

    def testConstructor_Instances(self):
        m5 = proj1.Media()
        with self.assertRaises(AttributeError):
            m5.rate
            m5.movie_length
            m5.album
            m5.track_length
            m5.genre

        s5 = proj1.Song()
        with self.assertRaises(AttributeError):
            s5.rate
            s5.movie_length

        mv5 = proj1.Movie()
        with self.assertRaises(AttributeError):
            mv5.album
            mv5.track_length
            mv5.genre

#JSON TESTS (pt. 2):
import requests
import json

json_file = open('sample_json.json', 'r')
json_str = json_file.read()
json_dict = json.loads(json_str)
json_file.close()

print(type(json_dict))
# 
# class TestMedia2(unittest.TestCase):
#     def testConstructor_Json_Variables(self):
#         media1_json = proj1.Media(json_1 = json_dict[0])
#         self.assertEqual(media1_json.title, "Jaws")
#         self.assertEqual(media1_json.author, "Steven Spielberg")
#         self.assertEqual(media1_json.year, "1968")
#
#         # if json_dict["kind"] == "song":
#         #     self.assertEqual(media_json)













unittest.main()
