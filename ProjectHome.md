**Video plugin that allows streaming of live uk freeview channels from tvcatchup.com directly in your xbmc frontend**

**_Requires sign up to tvcatchup.com and to be a UK resident._**

V1.3.4
Now Working from within XBMC and supports Dharma too
  * What's on now has been added with the option to switch it off if you want.
  * Automatically downloads missing libraries and updated files.
  * We now have a new home at http://plugins.tvcatchup.com/~xbmc

LATEST UPDATES:
  * Now compatible with Dharma RC2
  * Username/Password are stored in plugin settings (no more edit defualt.py) - thanks to dink for submitting change!
  * All channels available now

Notes:
  * TVCatchup.com requires registration (free). Sign up and get a username/password
  * Extract to the plugins\video folder in your xbmc dir
  * Boot up XBMC

KNOWN BUGS:
  * xbmc seems to hang if you try to watch a channel which is "off-line" at the moment (i.e. five us only broadcasts between certain hours - out of hours xbmc hangs) **_Fixed with latest T3CH stable build and plugin v1.2.1_**
  * xbox version of xbmc has a memory leak when trying to watch rtmp streams (like this & iPlayer). The xbox will freeze after 4-5 minutes. (needs a patch to be applied to xbmc SVN code) - info from rudeboyx **_Fixed with latest T3CH stable build and plugin v1.2.1_**
  * can be processor intensive on the xbox due to the decryption required on the stream (dj\_gerbil)
