# #spot check 1:
# class Restaurant:
#     def __init__(self, name, rating, is_veg):
#         self.name = name
#         self.rating = rating
#         self.is_veg = is_veg
#     def get_menu(self):
#         if self.is_veg:
#             return "We have vegetables"
#         else:
#             return "We have meat"
#
# r1 = Restaurant("Zoozaazo", 4, False)
# r2 = Restaurant("Top La Pompei", 3, False)
# r3 = Restaurant("El Viego", 5, True)


#exerecise 1-6 and extensions:
import operator


class YouTubeSongManager:
    def __init__(self):
        self.songs = {}
        self.counter = {}
        self.songs_part_str = []

    def save(self, name1, url1):
        name = name1.lower().replace("'", "")
        url = url1.split("=")[1]
        self.songs.update({name: url})

    def get(self, name1):
        name = name1.lower().replace("'", "")
        for song in self.songs:
            url = "https://www.youtube.com/watch?v=" + self.songs[song]
            if song == name or name in song:
                self.songs_part_str.append(url)
        if name not in self.counter:
            self.counter[name] = 1
        else:
            self.counter[name] +=    1
        return self.songs_part_str

    def get_most_popular_song(self):
        return  max(self.counter.items(), key=operator.itemgetter(1))[0]


song_manager = YouTubeSongManager()
song_manager.save("Don't Fear the Reaper", "https://www.youtube.com/watch?v=ClQcUyhoxTg")
song_manager.save("Leonard Cohen - Hallelujah", "https://www.youtube.com/watch?v=TBMf3mcIGkw")
song_manager.save("Christina Perri - A Thousand Years", "https://www.youtube.com/watch?v=QgaTQ5-XfMM")

print(song_manager.songs)
# print(song_manager.get("j") )
# print(song_manager.get("Leonard Cohen - Hallelujah") )
# print(song_manager.get("Christina Perri - A Thousand Years") )
# print(song_manager.songs["dont fear the reaper"]) # outputs: ClQcUyhoxTg
# print(song_manager.get("Don't Fear the Reaper")) # outputs: ﻿https://www.youtube.com/watch?v=ClQcUyhoxTg
song_manager.get("Don't Fear the Reaper")
song_manager.get("Don't Fear the Reaper")
song_manager.get("Golden Brown")
song_manager.get("Don't Fear the Reaper")
song_manager.get("Golden Brown")

print(song_manager.counter) # outputs: {'Don't Fear the Reaper': 3, 'Golden Brown': 2}
print(song_manager.get_most_popular_song()) # outputs: "Don't Fear the Reaper"﻿



