
#STEP 1:
# list for songs and their genre, dictionary to count the number of genre:
songs = []
genre_count = {}

print("*"*10,"Wellcome to Personal Music Library Management","*"*10)

#STEP 2:
# input limit of songs for user:
inputs = 1
while inputs <= 5:
    #inputing song details:
    print(f'\nEnter song {inputs}:')

    song = input("Song name: ")
    genre = input("Sone genre: ")

#STEP 3:
    #making a list of  song details(songTuple)
    songTuple = (song,genre)
    songs.append(songTuple)

    #counting genre
    genre_count[genre] = genre_count.get(genre, 0) +1

    inputs += 1

#STEP 4:
#Printing result:
print("\n","="*10,"'YOUR MUSIC LIBRARY'","="*10)
songCountvar = 1
for song,genre in songs:
    print(f"    {songCountvar}. {song}:({genre}.)\n")
    songCountvar += 1

print("="*10,"'GENRE STATISTICS'","="*10)
genreCountvar = 1
for genre, songs in genre_count.items():
    print(f"    {genreCountvar}. {genre}: {songs}Songs.\n")
    genreCountvar += 1

#finding most popular genre:
popularGenre = max(genre_count, key = genre_count.get)
print("="*10,"'MOST POPULAR GENRE'","="*10,"\n" \
f"  {popularGenre}.\n")
