class MP3Player:
    def __init__(self):
        self.queue = []
        self.current_song = None

    def add_song(self, s):
        self.queue.append(s)
        print("Added song to queue")

    def play_next_song(self):
        if len(self.queue) == 0:
            print("Queue empty")
            return
        self.current_song = self.queue.pop(0)
        print("Playing next song")

    def skip_song(self):
        if len(self.queue) == 0:
            print("Queue empty")
        self.current_song = self.queue.pop(0)
        print("Skipping song")


if __name__ == "__main__":
    player = MP3Player()

    print("Welcome!")
    while True:
        print("Current song: ")
        print(player.current_song if player.current_song != None else "--Play a song--")
        print()
        match input("Enter command: "):
            case "add":
                player.add_song(input("Enter song name: "))
            case "next":
                player.play_next_song()
            case "skip":
                player.skip_song()
            case "help":
                print(
                    """
    add     Adds a song to the play queue
    next    Plays the next song in the queue
    skip    Skips the current song
    help    Displays comands
                    """
                )
            case "exit":
                break
            case _:
                print("Unknown command. Type 'help' for commands.")
        print()
