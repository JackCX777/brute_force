import vlc
import time


# creating Instance class object
player_instance = vlc.Instance()
# setting 9999 times loop variant 1
# player_instance = vlc.Instance('--input-repeat=9999')

# creating a new media list
media_list = player_instance.media_list_new()

# creating a media player object
media_player = player_instance.media_list_player_new()
# media_player = player_instance.media_player_new('K_Motionz_-_Hack_It(ft.Duskee).mp3')
# media_player = vlc.MediaPlayer('K_Motionz_-_Hack_It(ft.Duskee).mp3')

# creating a new media
media = player_instance.media_new('K_Motionz_-_Hack_It(ft.Duskee).mp3')

# adding media to media list
media_list.add_media(media)

# setting media list to the mediaplayer
media_player.set_media_list(media_list)

# setting infinity? loop variant 2
media_player.set_playback_mode(vlc.PlaybackMode.loop)

media_player.play()


time.sleep(1000000)
