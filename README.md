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

```

```






---
# Python program to update
# JSON
 
 
import json
 
 
# function to add to JSON
def write_json(new_data, filename='data.json'):
    with open(filename,'r+') as file:
          # First we load existing data into a dict.
        file_data = json.load(file)
        # Join new_data with file_data inside emp_details
        file_data["emp_details"].append(new_data)
        # Sets file's current position at offset.
        file.seek(0)
        # convert back to json.
        json.dump(file_data, file, indent = 4)
 
    # python object to be appended
y = {"emp_name":"Nikhil",
     "email": "nikhil@geeksforgeeks.org",
     "job_profile": "Full Time"
    }
     
write_json(y)

---

# Python program to demonstrate
# Conversion of JSON data to
# dictionary
 
 
# importing the module
import json
 
# Opening JSON file
with open('data.json') as json_file:
    data = json.load(json_file)
 
    # for reading nested data [0] represents
    # the index value of the list
    print(data['people1'][0])
     
    # for printing the key-value pair of
    # nested dictionary for loop can be used
    print("\nPrinting nested dictionary as a key-value pair\n")
    for i in data['people1']:
        print("Name:", i['name'])
        print("Website:", i['website'])
        print("From:", i['from'])
        print()

---
# Cehck if a vlaue exist in a dictonary
# Dictionary of string and int
word_freq = {
    "Hello": 56,
    "at": 23,
    "test": 43,
    "this": 78
}

value = 43
# python check if value exist in dict using "in" & values()
if value in word_freq.values():
    print(f"Yes, Value: '{value}' exists in dictionary")
else:
    print(f"No, Value: '{value}' does not exists in dictionary")


--- 

# my json file

{
  "rfid_cards": [
    {
      "id":"123456",
      "name":"zoo",
      "url":"spotify:track:xyz",
    }

  ]
}
