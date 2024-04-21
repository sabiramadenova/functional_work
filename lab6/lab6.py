from rx import interval
from rx.subject import Subject


class MusicPlayer:
    def __init__(self):
        self.playback_state = Subject()
        self.sequence = Subject()
        self.audio_settings = Subject()

    def play(self):
        self.playback_state.on_next("play")

    def pause(self):
        self.playback_state.on_next("pause")

    def stop(self):
        self.playback_state.on_next("stop")

    def next_track(self):
        self.sequence.on_next("next")

    def previous_track(self):
        self.sequence.on_next("previous")

    def set_volume(self, volume):
        self.audio_settings.on_next(("volume", volume))

    def set_equalizer(self, equalizer_setting):
        self.audio_settings.on_next(("equalizer", equalizer_setting))


def simulate_user_interactions(player):

    interval(1) \
        .subscribe(lambda _: player.play())

    interval(1) \
        .subscribe(lambda _: player.pause())

    interval(2) \
        .subscribe(lambda _: player.next_track())

    interval(2) \
        .subscribe(lambda _: player.set_volume(80))


def main():
    player = MusicPlayer()

    simulate_user_interactions(player)

    player.playback_state.subscribe(lambda state: print("Playback state:", state))

    player.sequence.subscribe(lambda action: print("Sequence action:", action))

    player.audio_settings.subscribe(lambda setting: print("Audio setting:", setting))

    input("Press Enter to quit...\n")


if __name__ == "__main__":
    main()
