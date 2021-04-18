**MrPlayer** is a _MP3_ player made on 100% **Python**, it is for **Windows** .

## An apealing MP3 player

<video controls autoplay muted width="540" height="572" ><source src="main.mp4" type="video/mp4"></video>

# Features of MrPlayer

**MrPlayer has all features -**

1. Play
2. Pause
3. Next
4. Previous
5. Help Button
6. Total duration and current duration
7. Duration slider
8. Volume slider

# A special feature

MrPlayer is with Lyrics which is extracted from [Genius.com](https://Genius.com) using lyricsgenius python library.

![GIF](lyrics.gif)

Lyrics fetching time may vary according to your internet speed.

---

# MrPlayer-CLI

Suggested using windows terminal becuse it suports
many languages when extracting lyrics.

Terminal theme 'is One Half Dark'

<video controls autoplay width="640" height="360" ><source src="CLI.mp4" type="video/mp4"></video>

For playing song cd to directory where the song is and type this command -

```powershell
mpc -ps "song name.mp3"
```

For getting lyrics type this command -

```powershell
mpc -gl "song name" -si "singer name"
```

For knowing the source code MrPlayer-CLI type this command -

```powershell
mpc -sc
```

# Download & Installation

1. Click on the **_Download_** button or click on the link - [releases](https://www.github.com/AkshatChauhan18/Mrplayer/releases), you will be redirected to the release page.
2. Click on the latest release
3. Download the installer and run it , MrPLayer will be installed

---

# How to use MrPlayer

When you will first time start MrPlayer it will show nothing in the song box ,
to add songs close MrPlayer and go to your **_Music_** folder
and there will be a folder already created of name MrPlayer-songs , add songs
to the MrPlayer folder and rerun the app . Enjoy using MrPlayer.

---

# How to use Lyrics feature of MrPlayer and MrPlayer-CLI

You need to create a account in [Genius.com](https://Genius.com) then go to [Genius Dev](https://Genius.com/developers)
then click 'Create an API client' ,then enter the client name you want to create ,
you will need to enter a website name in order to create an api client. Then click
save. Then click 'generate access token', it will create an access token , then
copy the access token. For both MrPlayer and MrPlayer-CLI you need to paste that
access token to 'C:\\Users\\Your User Name\\.MrPlayer\\api_key.txt'.
