# Hoergrete-rfid

Hörgrete mach 2 - rfid enabled.

## Vision

Mopidy and Mopidy-Spotify
Controlled by GPIOS
A small Servie Runnig for RFID RC522
A Github repo where Playlist and Cards are managend in a .txt file
Automatic sync on boot up
Minimal Web interface for Volume?

## Install

1. follow my guide (26.12.21) for pi and audio setup

### hoergrete rfid script

1. `sudo apt install python3-dev python3-pip espeak git`
1. `sudo pip3 install spidev mfrc522 num2words`
1. `git clone https://github.com/jonasprobst/hoergrete-rfid.git`
1. `cd hoergrete-rfid`
1. (`git reset --hard && git pull`)

### samba

Follow this guide : https://pimylifeup.com/raspberry-pi-samba/

notes:
* yes to WINS Settings when prompted
* use generated password for user pi not raspberry

### mopidy

Follow this guide: https://www.makeuseof.com/turn-your-raspberry-pi-into-a-home-music-server-with-mopidy/ 

**important** notes:
* **do not give iris sudo permission** in step 3. This command is broken an will **kill sudo** for all users!
* change audio output to this
  ```
  [audio]
  mixer_volume = 50
  output = alsasink device=hw:0,0
  ```
* local share is `/home/pi/shared`
* `sudo python3 -m pip install Mopidy-Spotify`failed for me
  * i had to manually install `sudo python3 -m pip install pyspotify`and rerun Mopidy-Spotify fo it to work
  * (i actually also installed `sudo apt install libspotify-dev`following another tutorial - might no be needed)
  * this caused mopidy to freeze on startup 
  * so i `sudo python3 -m pip install --upgrade --force-reinstall Mopidy-Spotify`
  * that got mopidy running. had to restart the server in iris and logout and login again. then it worked... for abit
* Had some problems with ading and removing test audio files:
  * I eventually removed the missing tracks with `sudo rm -r /var/lib/mopidy/local/*´
  * then in iris by reset settings. that worked for me.

some comands to remember:
```
sudo nano /etc/mopidy/mopidy.conf
sudo mopidyctl config
sudo systemctl restart mopidy
sudo systemctl status mopidy
sudo mopidyctl local scan
sudo mopidyctl local clear
```

### mopidy gpio

Follow this guide: https://pypi.org/project/mopidy-raspberry-gpio/

note:
* **use sudo to install!!** `sudo python3 -m pip install Mopidy-Raspberry-GPIO`

```
[raspberry-gpio]
enabled = true
bcm17 = play_pause,active_low,250
bcm27 = prev,active_low,250
bcm22 = next,active_low,250
```

### mopidy-mpd to controll it using mpc

I know it's complicated but did't get my head around the websockets. 

1. `sudo python3 -m pip install Mopidy-MPD`
1. `sudo apt install mpc`

to brows the local media folder and guess the URI `mpc ls` came in handy.

### finishing touches

1. once everything works: autorun hoergrete on boot
  * sudo nano /etc/rc.local 
  * Add the following after comments and before EXIT 0
    ```
    # Hoergrete firmware update and autorun
    # git -C /home/pi/hoergrete-rfid/ pull
    sudo python3 home/pi/hoergrete-rfid/hoergrete.py &
    ```
  * sudo chmod +x /etc/rc.local
  * cross your fingers and reboot

## Workflows

it's easier than it look ... right :-S

### upload new music

1. get music ready with exFalso (https://quodlibet.readthedocs.io/en/latest/downloads.html)
1. connet to samba drive and upload the music to hoergrete
1. ssh into hoergrete
1. `sudo mopidyctl local scan`
1. `sudo systemctl restart mopidy`
1. check on webinterface unter Browse/Local Files/Tracks

### setup new rfid card

1. touch hoergrete with the new rfid card
1. navigate to iris -> Browse/Files/rfid -> "copy URI(s)"
1. head over to cards.json, create a new section an insert the ID
1. set Track URI (easiest way is "copy URI(s)" from iris track/album/etc.)
1. set options: *rdm/random* plays songs randomly (surprise). *sgl/single* plays just one song then stops (i think). 
1. git commit and push. Wait a minute or so then touch hoergrete again
1. it should now play your track ... good luck!

## Inspiration and help

Thanks you guys!

* https://docs.mopidy.com/en/latest/config/
* https://github.com/pimoroni/pirate-audio/tree/master/mopidy
* http://www.kellbot.com/yet-another-raspberry-pi-jukebox/
* https://helen.blog/2019/12/building-a-swipe-card-jukebox-using-a-raspberry-pi/
* https://mopidy.com/ext/spotify/#authentication
* https://github.com/scheleaap/rfid-jukebox
* https://raspberrypi-guide.github.io/programming/run-script-on-boot
* https://raspberry-projects.com/pi/software_utilities/email/ssmtp-to-send-emails 
* https://pimylifeup.com/raspberry-pi-rfid-rc522/
* https://wiretuts.com/installing-mopidy-music-server-on-raspberry-pi

