import sys
import xbmcgui
import xbmcplugin
# We include the things we need.


addon_handle = int(sys.argv[1])

xbmcplugin.setContent(addon_handle, 'audio')
# Put this in the audio category.


url = 'http://stream.anonops.com:8080/AnonOps' # Rather straightforward, here.
li = xbmcgui.ListItem('Anonops Main', iconImage='https://raw.githubusercontent.com/Based-Skid/plugin.audio.anonopsradio/master/plugin.audio.anonopsradio/o1XuBFO.png')  #Name, then the icon. I'm pleasantly surprised it accepts URLs!
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
#Bleh. It's a hacky hack to use Imgur, but it'll work for now. I plan to either do one of two things:
#1) Figure out how to use the poorly documented system to add in the icon files to the code via the zip file
#   (Files are not in the zip file at the moment, to save space. )
#OR
#2) Host the images on radio.anonops.com or another controlled domain so the admins can swap out
#   the images as needed. This may be a more effective solution, as it's easy to swap out the URLs, then they can
#   swap out the files -- it'd make it really easy to do things like put on stamps for things like, as an example,
#   freeanons, freelorax, and other causes.
#   OR 
#   swap out images for holidays, and so on.


url = 'http://stream.anonops.com:8080/AnonNews'
li = xbmcgui.ListItem('ANONOPS NEWS', iconImage='https://raw.githubusercontent.com/Based-Skid/plugin.audio.anonopsradio/master/images/QPqSTEd.png')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

url = 'http://stream.anonops.com:8080/AnonPop'
li = xbmcgui.ListItem('ANONOPS POP', iconImage='https://raw.githubusercontent.com/Based-Skid/plugin.audio.anonopsradio/master/images/8g48ep6.png')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

url = 'http://stream.anonops.com:8080/AnonRock'
li = xbmcgui.ListItem('ANONOPS ROCK', iconImage='https://raw.githubusercontent.com/Based-Skid/plugin.audio.anonopsradio/master/images/jLimbbr.png')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

url = 'http://stream.anonops.com:8080/AnonChill'
li = xbmcgui.ListItem('ANONOPS CHILL', iconImage='https://raw.githubusercontent.com/Based-Skid/plugin.audio.anonopsradio/master/images/40MPQHw.png')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)


url = 'http://stream.anonops.com:8080/AnonWorld'
li = xbmcgui.ListItem('ANONOPS WORLD', iconImage='https://raw.githubusercontent.com/Based-Skid/plugin.audio.anonopsradio/master/images/ALLwVzf.png')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

url = 'http://stream.anonops.com:8080/AnonClassic'
li = xbmcgui.ListItem('ANONOPS CLASSICAL', iconImage='hhttps://raw.githubusercontent.com/Based-Skid/plugin.audio.anonopsradio/master/images/5f0lXXO.png')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

url = 'http://stream.anonops.com:8080/AnonCountry'
li = xbmcgui.ListItem('ANONOPS COUNTRY', iconImage='https://raw.githubusercontent.com/Based-Skid/plugin.audio.anonopsradio/master/images/e9KO5c6.png')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)


xbmcplugin.endOfDirectory(addon_handle) # Here we tell the system that this is the end for now.
