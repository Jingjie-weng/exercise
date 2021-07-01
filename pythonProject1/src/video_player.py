"""A video player class."""

from .video_library import VideoLibrary
from data_cleanse import *
import random
currently_playing = []
paused = [1,1]

class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        with open('videos.txt') as f:
            a = f.read()
            print(a)
        """Returns all videos."""

    def play_video(self, video_id):
        """Plays the respective video.

        Args:
            video_id: The video_id to be played.
        """

        for ids in id:
            if video_id == ids:  # This checks if the input video is in the library
                if len(currently_playing) == 0:
                    print('Playing video ' + title[id.index(ids)])
                    currently_playing.append(video_id)
                elif video_id == currently_playing[-1]:
                    print('Stopping video: ' +  title[id.index(currently_playing[-1])])
                    print('Playing video: ' +  title[id.index(ids)])
                    currently_playing.append(video_id)
                elif currently_playing[-1] != video_id:
                    print('Stopping video: ' + title[id.index(currently_playing[-1])])
                    print('Playing video: ' + title[id.index(ids)])
                    currently_playing.append(video_id)

    def stop_video(self):
        """Stops the current video."""
        if len(currently_playing) != 0: # checks if there is video playing
            print('Stopping video: ' + currently_playing[-1])
            currently_playing.clear()  # returns currently plyaing video to default(none).
        else:
            print('Cannot stop video: No video is currently playing.')

    def play_random_video(self):
        """Plays a random video from the video library."""
        for ids in id:
            randomvid = id[random.randint(0, len(id))]
            if len(currently_playing)==0:
                print('Playing video: '+ title[random.randint(0,len(id))])
                currently_playing.append(randomvid)

            else:
                print('Stopping video: '+ title[id.index(currently_playing[-1])])
                print('Playing video: ' + title[id.index(randomvid)])
                currently_playing.append(randomvid)
            break


    def pause_video(self):
        """Pauses the current video."""
        if paused[-1]== 1:  # checks if there is video playing
            print('Pausing video: ' + currently_playing[-1])
            paused.append(0)
        elif len(currently_playing) ==0:
            print("Cannot pause video: No video is currently playing")
        else:
            print('Video already paused: '+currently_playing[-1])


    def continue_video(self):
        """Resumes playing the current video."""
        if paused[-1]==0:
            print('Continuing video: '+str(currently_playing))
            paused.append(1)
        elif paused[-1] ==1:
            print('Cannot continue video: Video is not paused')
        elif len(currently_playing) ==0:
            print("Cannot continue video: No video is currently playing")

    def show_playing(self):
        """Displays video currently playing."""
        if len(currently_playing) != 0:
            print('Currently playing: '+str(resulttoken[id.index(currently_playing[-1])]))
        else:
            print('No video is currently playing')





    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        playlists=['sample']
        for names in playlists:
            if str(playlist_name).lower()!=names.lower():
                print("Successfully created new playlist: " + str(playlist_name))
                playlists.append(str(playlist_name))
                list=[]
                playlist_name = list
            else:
                print('Cannot create playlist: A playlist with the same name already exists')







    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        print("add_to_playlist needs implementation")

    def show_all_playlists(self):
        """Display all playlists."""

        print("show_all_playlists needs implementation")

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("show_playlist needs implementation")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        print("remove_from_playlist needs implementation")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("clears_playlist needs implementation")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("deletes_playlist needs implementation")

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        print("search_videos needs implementation")

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        print("search_videos_tag needs implementation")

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")
