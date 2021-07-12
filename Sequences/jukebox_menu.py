from nested_data import albums

SONGS_LIST_INDEX = 3
SONGS_TITLE_INDEX = 1

while True:
    print("Please choose your album (invalid choice exists): ")
    for index, (title, artist, year, songs) in enumerate(albums):
        # print(f"{index + 1}: {title}, {artist}, {year}, {songs}")
        print(f"{index + 1}: {title}")

    # for index, value in enumerate(albums):
    #     title, artist, year, songs = value
    #     print(index, title, artist, year, songs)

    choice = int(input())
    if 1 <= choice <= len(albums):
        songs_list = albums[choice - 1][SONGS_LIST_INDEX]
    else:
        break

    print("Please choose your song: ")
    for index, (track_number, song) in enumerate(songs_list):
        print(f"{index + 1}: {song}")

    song_choice = int(input())
    if 1 <= song_choice <= len(songs_list):
        title = songs_list[song_choice - 1][SONGS_TITLE_INDEX]
    else:
        break

    print(f"Playing {title}")
    print("=" * 40)