import urllib,urllib2,re,sys,xbmcplugin,xbmcgui

def getURL(url):
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
    opener.addheaders = [('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.8.1.14) Gecko/20080404 Firefox/2.0.0.14')]
    urllib2.install_opener(opener)
    #Now Login
    params = "_qf__login=&"+urllib.urlencode({'vb_login_username':uname})+"&"+urllib.urlencode({'vb_login_password':pwd})+"&submit.x=53&submit.y=17"
    lg = opener.open('http://old.tvcatchup.com/login/', params)
    data = lg.read()
    lg.close()
    response = opener.open(url);link=response.read();response.close()
    return link

def postURL(url, tvcid, channelid):
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
    opener.addheaders = [('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.8.1.14) Gecko/20080404 Firefox/2.0.0.14')]
    urllib2.install_opener(opener)
    #Now Login
    params = "_qf__login=&"+urllib.urlencode({'vb_login_username':uname})+"&"+urllib.urlencode({'vb_login_password':pwd})+"&submit.x=53&submit.y=17"
    lg = opener.open('http://old.tvcatchup.com/login/', params)
    data = lg.read()
    lg.close()
    tvcparams = "function=TVC%5FAds&token=&key="+tvcid.replace("-", "%2D")+"&version=&channel="+channelid+"&source=website&output=json"
    response = opener.open(url, tvcparams);link=response.read();response.close()
    return link

def CHANNELS(url):
        req = urllib2.Request('http://www.tvcatchup.com/channels.php')
	req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
	response = urllib2.urlopen(req)
	link=response.read()
	response.close()
	channel=re.compile('<name>(.+?)</name>').findall(link)
	chanlink=re.compile('<link>http://www.(.+?)</link>').findall(link)
	thumbs=re.compile('<logo>http://www.tvcatchup.com/channels/(.+?)</logo>').findall(link)
	for i in range(0, len(channel)):
	       ThumbURL = ''.join(["http://old.tvcatchup.com/channels/",thumbs[i]])
	       ChannelURL = ''.join(["http://www.tvcatchup.com/watch.html?c=",str(i+1)])
               ChannelNum = ''.join([str(i+1)," : ",channel[i]])
               addDir(ChannelNum,ChannelURL,1,ThumbURL)
	       
def tempCHANNELS(url):
    link = getURL("http://www.tvcatchup.com/?cache=1")
    urls=re.compile('"(.{1,2}?)":{"channel_id":"(.+?)","channel_name":"(.+?)","channel_status":"(.+?)","now":{"title":".+?","start":".+?","end":".+?"}}').findall(link)
    #channelid, tchannelid, name, logo, status
    print urls
    for channelid, tchannelid, name, status in urls:
        print status
       # print logo.replace("\\/", "/").replace(" ", "%20")
        if status=="enabled":
            addDir(name,"http://www.tvcatchup.com/watch.html?c=" + channelid,1,"")

def VIDEO(url):
    slink = getURL("http://www.tvcatchup.com/?cache=1")
    idlink = getURL(url)
    info=re.compile('"(.{1,2}?)":{"channel_id":"(.+?)","channel_name":"(.+?)","channel_status":"(.+?)","now":{"title":"(.+?)","start":"(.+?)","end":"(.+?)"}}').findall(slink)
    #channelid, tchannelid, name, logo, status, nowname, nowstart, nowend, nextname, nextstart, nextend
    tvcid=re.compile('TVCWebPlayer\("(.+?)"\);').findall(idlink)
    print tvcid
    rtmplink = postURL("http://api.tvcatchup.com", tvcid[0], url.split("=")[1])
    rtmp = re.compile('"channel_streamer":"(.+?)chan=.+?"').findall(rtmplink)
    rtfile = re.compile('"channel_file":"(.+?)"').findall(rtmplink)
    video=[(rtmp[i], rtfile[i])for i in range (0,len(rtmp))]
    for channelid, tchannelid, name, logo, status, nowname, nowstart, nowend in info:
        if channelid==url.split("=")[1]:
            for rtmp, rtf in video:
               print rtmp.replace("\\/","/") + rtf
               addLink(nowstart + " - " + nowname, rtmp.replace("\\/","/") + rtf)
               #addLink(nextstart + " - " + nextname, rtmp.replace("\\/","/") + rtf)

def tempOLDVIDEO(url):
    slink = getURL("http://www.tvcatchup.com/?cache=1")
    idlink = getURL(url)
    info=re.compile('"(.{1,2}?)":{"channel_id":"(.+?)","channel_name":"(.+?)","channel_status":"(.+?)","now":{"title":"(.+?)","start":"(.+?)","end":"(.+?)"}}').findall(slink)
    #channelid, tchannelid, name, status, nowname, nowstart, nowend, nextname, nextstart, nextend
    video=re.compile('flashvars\.streamer = "(.+?)chan=.+?";\n\tflashvars.file = "(.+?)";',re.MULTILINE).findall(idlink)
    for channelid, tchannelid, name, status, nowname, nowstart, nowend in info:
        if channelid==url.split("=")[1]:
            for rtmp, rtf in video:
               print rtmp.replace("\\/","/") + rtf
               addLink(nowstart + " - " + nowname, rtmp.replace("\\/","/") + rtf)
               #addLink(nextstart + " - " + nextname, rtmp.replace("\\/","/") + rtf)

def OLDVIDEO(url):
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
    opener.addheaders = [('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')]
    urllib2.install_opener(opener)
    params = "_qf__login=&"+urllib.urlencode({'vb_login_username':uname})+"&"+urllib.urlencode({'vb_login_password':pwd})
    lg = opener.open('http://old.tvcatchup.com/login/', params)
    data = lg.read()
    print data
    lg.close()
    response = opener.open(url)
    print response
    link=response.read()
    response.close()
    title="Watch Channel"
    description=""
    rtmp=re.compile('flashvars.streamer = "(.+?)/chan=.+?";').findall(link)
    rtfile=re.compile('flashvars.file = "(.+?)";').findall(link)
    combineit = rtmp[0]+"/"+rtfile[0]
    addLink(title,combineit)
    
def get_params():
        param=[]
        paramstring=sys.argv[2]
        if len(paramstring)>=2:
                params=sys.argv[2]
                cleanedparams=params.replace('?','')
                if (params[len(params)-1]=='/'):
                        params=params[0:len(params)-2]
                pairsofparams=cleanedparams.split('&')
                param={}
                for i in range(len(pairsofparams)):
                        splitparams={}
                        splitparams=pairsofparams[i].split('=')
                        if (len(splitparams))==2:
                                param[splitparams[0]]=splitparams[1]
        return param

def check_settings():
		uname = xbmcplugin.getSetting('uname')
		pwd   = xbmcplugin.getSetting('pwd')
		if (not uname or uname == '') or (not pwd or pwd == ''):
				d = xbmcgui.Dialog()
				d.ok('Welcome to the TVCatchup plugin.', 'To start using this plugin first go to www.TVCatchup.com','and create a (free) account.')
				xbmcplugin.openSettings(sys.argv[ 0 ]) 
						
		
def addLink(name,url):
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png")
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz)
        return ok

def addDir(name,url,mode,iconimage):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok


check_settings()
uname = xbmcplugin.getSetting('uname')
pwd   = xbmcplugin.getSetting('pwd')
        
params=get_params()
url=None
name=None
mode=None
cookie=None

try:
        url=urllib.unquote_plus(params["url"])
except:
        pass
try:
        name=urllib.unquote_plus(params["name"])
except:
        pass
try:
        mode=int(params["mode"])
except:
        pass
print "Mode: "+str(mode)
print "URL: "+str(url)
print "Name: "+str(name)
if mode==None or url==None or len(url)<1:
        print "channels"
        CHANNELS('http://www.tvcatchup.com')
elif mode==1:
        print "Get Rtmp"
        try:
            VIDEO(url)
        except:
            OLDVIDEO(url)

xbmcplugin.endOfDirectory(int(sys.argv[1]))
