import sys
import xbmcgui
import xbmcplugin
# We include the things we need.


addon_handle = int(sys.argv[1])

xbmcplugin.setContent(addon_handle, 'audio')
# Puts This Addon in the Audio section of the Kodi Addons.


#--Based_Skid here
#We Need to Add in code that will allow us to define the station list from a url, say a txt file on the git for example
#If this addon ever were to be made "official" this txt file should be hosted on the anonops site example: radio.anonops.com/stationlist.txt
#Same with the images. example:radio.anonops.com/imgs. but for now they are on the git 
#-----

url = 'http://stream.anonops.com:8080/AnonOps' # Rather straightforward, here.
li = xbmcgui.ListItem('Anonops Main', iconImage='https://raw.githubusercontent.com/Based-Skid/plugin.audio.anonopsradio/master/images/o1XuBFO.png')  #Name, then the icon. I'm pleasantly surprised it accepts URLs!
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)



 = 'http://stream.anonops.com:8080/AnonNews'
li = xbmcgui.ListItem('ANONOPS NEWS', iconImage='https://raw.githubusercontent.com/Based-Skid/plugin.audio.anonopsradio/master/images/QPqSTEd.png')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
# Commit out Non Functional Stations
#url = 'http://stream.anonops.com:8080/AnonPop'
#li = xbmcgui.ListItem('ANONOPS POP', iconImage='https://raw.githubusercontent.com/Based-Skid/plugin.audio.anonopsradio/master/images/8g48ep6.png')
#xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

#url = 'http://stream.anonops.com:8080/AnonRock'
#li = xbmcgui.ListItem('ANONOPS ROCK', iconImage='https://raw.githubusercontent.com/Based-Skid/plugin.audio.anonopsradio/master/images/jLimbbr.png')
#xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

#url = 'http://stream.anonops.com:8080/AnonChill'
#li = xbmcgui.ListItem('ANONOPS CHILL', iconImage='https://raw.githubusercontent.com/Based-Skid/plugin.audio.anonopsradio/master/images/40MPQHw.png')
#xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

#url = 'http://stream.anonops.com:8080/AnonWorld'
#li = xbmcgui.ListItem('ANONOPS WORLD', iconImage='https://raw.githubusercontent.com/Based-Skid/plugin.audio.anonopsradio/master/images/ALLwVzf.png')
#xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

#url = 'http://stream.anonops.com:8080/AnonClassic'
#li = xbmcgui.ListItem('ANONOPS CLASSICAL', iconImage='https://raw.githubusercontent.com/Based-Skid/plugin.audio.anonopsradio/master/images/5f0lXXO.png')
#xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

#url = 'http://stream.anonops.com:8080/AnonCountry'
#li = xbmcgui.ListItem('ANONOPS COUNTRY', iconImage='https://raw.githubusercontent.com/Based-Skid/plugin.audio.anonopsradio/master/images/e9KO5c6.png')
#xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

xbmcplugin.endOfDirectory(addon_handle) # Here we tell the system that this is the end for now.
