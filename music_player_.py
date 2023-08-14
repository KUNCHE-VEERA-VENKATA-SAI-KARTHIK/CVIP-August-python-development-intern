#pip install pygame
import os
import pygame

# Initialize pygame
pygame.mixer.init()


# Function to list available songs
def list_songs():
    print("Available songs:")
    songs = [file for file in os.listdir() if file.endswith(".mp3")]
    for idx, song in enumerate(songs, start=1):
        print(f"{idx}. {song}")


# Function to play a selected song
def play_song(song_number):
    songs = [file for file in os.listdir() if file.endswith(".mp3")]
    if 1 <= song_number <= len(songs):
        song_to_play = songs[song_number - 1]
        pygame.mixer.music.load(song_to_play)
        pygame.mixer.music.play()
        print(f"Now playing: {song_to_play}")
    else:
        print("Invalid song number!")


# Main loop
while True:
    print("\nMusic Player Menu:")
    print("1. List Songs")
    print("2. Play Song")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        list_songs()
    elif choice == "2":
        list_songs()
        song_number = int(input("Enter the song number to play: "))
        play_song(song_number)
    elif choice == "3":
        pygame.mixer.music.stop()
        print("Exiting the music player. Goodbye!")
        break
    else:
        print("Invalid choice. Please choose a valid option.")
