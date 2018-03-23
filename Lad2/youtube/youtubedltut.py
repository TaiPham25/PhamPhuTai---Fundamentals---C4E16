from youtube_dl import YoutubeDL


# Sample 1: Download a single youtube video
# dl = YoutubeDL()
# dl.download(['https://www.youtube.com/watch?v=d-4Ydzc7JTQ'])

# Sample 2: Download multiple youtube videos
# dl = YoutubeDL()
# dl.download(['https://www.youtube.com/watch?v=L6NwBiYPzvk', 'https://www.youtube.com/watch?v=hPrMVbe0r1w'])


# Sample 3: Download audio
# options = {
#     'format': 'bestaudio/audio'
# }
# dl = YoutubeDL(options)
# dl.download(['https://www.youtube.com/watch?v=5Q9h_HGPoA4'])

# Sample 4: Search and then download the first video
# options = {
#     'default_search': 'ytsearch', # tell downloader to search instead of directly downloading
#     'max_downloads': 1 # Tell downloader to download only the first entry (video)
# }
# dl = YoutubeDL(options)
# dl.download(['OneRepublic - Counting Stars'])
#hay vai chuong

# Sample 5: Search and then download the first audio
# options = {
#     'default_search': 'ytsearch', # tell downloader to search instead of directly downloading
#     'max_downloads': 1, # Tell downloader to download only the first entry (audio)
#     'format': 'bestaudio/audio'
# }
# dl = YoutubeDL(options)
# dl.download(['as we fall'])
