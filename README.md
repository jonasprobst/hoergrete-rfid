# hoergrete-rfid
Hörgrete mach 2 - rfid enabled.



# Manual mopidy install

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

## Vision

Mopidy and Mopidy-Spotify
Controlled by GPIOS
A small Servie Runnig for RFID RC522
A Github repo where Playlist and Cards are managend in a .txt file
Automatic sync on boot up
Minimal Web interface for Volume?

* Clients:
Mopidy-Raspberry-GPIO: https://mopidy.com/ext/raspberry-gpio/
Mopidy-Cli?



## mopidy.conf

```
[http]
enabled = false
hostname = 0.0.0.0

[audio]
mixer = software
mixer_volume = 40
output = alsasink

[mpd]
enabled = false
hostname = 0.0.0.0

[spotify]
enabled = true 
username = << your username
password = << your password
client_id = << the paragraph below addresses your client_id 
client_secret = << ...and your client secret

[raspberry-gpio]
enabled = true
bcm17 = play_pause,active_low,250
bcm22 = prev,active_low,250
bcm27 = next,active_low,250
# bcm21 = volume_down,active_low,10,rotenc_id=vol,step=1
# bcm20 = volume_up,active_low,10,rotenc_id=vol,step=1

[file]
enabled = true
media_dirs = /home/pi/Music
show_dotfiles = false
excluded_file_extensions =
  .directory
  .html
  .jpeg
  .jpg
  .log
  .nfo
  .pdf
  .png
  .txt
  .zip
follow_symlinks = false
metadata_timeout = 1000

```

sudo usermod -a -G spi,i2c,gpio,video mopidy
sudo systemctl enable mopidy
sudo systemctl start mopidy
sudo systemctl status mopidy


## Mopidy-Raspberry-GPIO

* https://mopidy.com/ext/raspberry-gpio/
* https://github.com/pimoroni/mopidy-raspberry-gpio

`sudo apt install python3-rpi.gpio`
`sudo usermod -a -G gpio mopidy`
`sudo python3 -m pip install Mopidy-Raspberry-GPIO`

---

## Install

1. follow my guide (26.12.) for setup pi and setup audio

### hoergrete rfid script

1. sudo apt install python3-dev python3-pip espeak git
1. sudo pip3 install spidev mfrc522 num2words
1. git clone https://github.com/jonasprobst/hoergrete-rfid.git
1. cd hoergrete-rfid
1. (git reset --hard && git pull)

### samba

1. Follow this to install samba: https://pimylifeup.com/raspberry-pi-samba/
  * a few changes:
  * yes to WINS Settings when prompted
  * use generated password for user pi not raspberry

### mopidy

1. Follow this to install mopidy: https://www.makeuseof.com/turn-your-raspberry-pi-into-a-home-music-server-with-mopidy/ 
1. a few **important** changes:
  * **do not give iris sudo permission** in step 3. This command is broken an will kill sudo for all users!
  * change audio output to this
    ```
    [audio]
    mixer_volume = 50
    output = alsasink device=hw:0,0
    ```
  * local share is '/home/pi/shared'
  * `sudo python3 -m pip install Mopidy-Spotify`failed for me
  * i had to manually install `sudo python3 -m pip install pyspotify`and rerun Mopidy-Spotify fo it to work
  * (i actually also installed `sudo apt install libspotify-dev`following another tutorial - might no be needed)
  * this caused mopidy to freeze on startup 
  * so i `sudo python3 -m pip install --upgrade --force-reinstall Mopidy-Spotify`
  * that got mopidy running. had to restart the server in iris and logout and login again. then it worked... strange

  sudo nano /etc/mopidy/mopidy.conf

  sudo mopidyctl config

  sudo systemctl restart mopidy
  sudo systemctl status mopidy

  sudo mopidyctl local scan
  sudo mopidyctl local clear
  
  got missing tracks out of iris by /setting/reset settings

### mopidy gpio
https://pypi.org/project/mopidy-raspberry-gpio/

**use sudo to install!!**

sudo python3 -m pip install Mopidy-Raspberry-GPIO

```
[raspberry-gpio]
enabled = true
bcm17 = play_pause,active_low,250
bcm27 = prev,active_low,250
bcm22 = next,active_low,250
```

### mopidy-mpd to controll it using mpc

sudo python3 -m pip install Mopidy-MPD
sudo apt install mpc

mpc ls
in iris go to tracks and under ... copy URI


### finishing touches

1. once everything works: autorun hoergrete on boot
  * sudo nano /etc/rc.local 
  * Add the following after comments and before EXIT 0
    ```
    # Hoergrete autorun
    sudo python3 home/pi/hoergrete-rfid/hoergrete_rfid.py &
    ```
    * sudo chmod +x /etc/rc.local

