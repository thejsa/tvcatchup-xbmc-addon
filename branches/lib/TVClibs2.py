oo000 = [ 'urllib' , 'urllib2' , 're' , 'os' , 'sys' , 'xbmcplugin' , 'xbmcgui' , 'xbmc' , 'TVClibs' , 'xbmcaddon' ]
ii = map ( __import__ , oo000 )
ii
if 51 - 51: IiI1i11I
Iii1I1 = False
__scriptname__ = "plugin.video.tvcatchup"
__author__ = 'dj_gerbil [tvc@killergerbils.co.uk]'
__svn_url__ = ""
__version__ = "1.3.1"
__phpurl__ = ii [ 8 ] . Ii ( "WVQvbHNDPXB3L3dyOUtJXVg1c3ApNHFpeC5qdj9fcTtUZmh6UFFmdGZ1ZHJrQFksS0h+Mld4Mm1meHJkOVtvXTgwbXFVZWV4ZmMyMGtVRWg+ZSB0a10jIGsgcyJMbSlSMg==" , 3 )
__cachefolder__ = "addon_data"
__settings__ = ii [ 9 ] . Addon ( id = 'plugin.video.tvcatchup' )
if 73 - 73: II1I1iiiiii * ooo0OO / o0OO00 / oo
if 27 - 27: oO0OooOoO * o0Oo
def i1IiI1I11 ( ) :
 IIiIiII11i = __settings__ . getSetting ( 'uname' )
 o0oOOo0O0Ooo = __settings__ . getSetting ( 'pwd' )
 if o0oOOo0O0Ooo . find ( '.enc.' ) < 0 :
  print "Not Encoded"
  I1ii11iIi11i = ii [ 1 ] . urlopen ( __phpurl__ + ii [ 8 ] . Ii ( "bXFjQzRNcHJzb2hmTF8/OGBNbmkuVWRyQHRqZ20tS19MKmNoXnVxdSk9aWcoXE8ydlAmcnlCaGRmcHJjQk1laGpjIHcqYSMgdiBAInJeeU1A" , 3 ) + o0oOOo0O0Ooo )
  I1IiI = I1ii11iIi11i . read ( )
  __settings__ . setSetting ( 'pwd' , I1IiI + '.enc.' )
 o0OOO = __settings__ . getSetting ( 'whatson' )
 if ( not IIiIiII11i or IIiIiII11i == '' ) or ( not o0oOOo0O0Ooo or o0oOOo0O0Ooo == '' ) :
  iIiiiI = ii [ 7 ] . translatePath ( ii [ 3 ] . path . join ( "T:" + ii [ 3 ] . sep , __cachefolder__ ) )
  Iii1ii1II11i = iIiiiI + ii [ 3 ] . sep + __scriptname__
  if not ii [ 3 ] . path . isdir ( Iii1ii1II11i ) :
   try :
    print "%s doesn't exist, creating" % Iii1ii1II11i
    ii [ 3 ] . makedirs ( Iii1ii1II11i )
   except IOError , iI111iI :
    print "Couldn't create %s, %s" % ( Iii1ii1II11i , str ( iI111iI ) )
    raise
  Iii1ii1II11i = iIiiiI + ii [ 3 ] . sep + __scriptname__ + ii [ 3 ] . sep + 'TVC_cache'
  if not ii [ 3 ] . path . isdir ( Iii1ii1II11i ) :
   try :
    print "%s doesn't exist, creating" % Iii1ii1II11i
    ii [ 3 ] . makedirs ( Iii1ii1II11i )
   except IOError , iI111iI :
    print "Couldn't create %s, %s" % ( Iii1ii1II11i , str ( iI111iI ) )
    raise
  iIiiiI = ii [ 7 ] . translatePath ( ii [ 3 ] . path . join ( "T:" + ii [ 3 ] . sep , __cachefolder__ , __scriptname__ ) )
  IiII = ii [ 3 ] . path . join ( iIiiiI , 'TVC_cache' )
  Iii1ii1II11i = ii [ 6 ] . Dialog ( )
  Iii1ii1II11i . ok ( 'Welcome to the TVCatchup plugin.' , 'To start using this plugin first go to www.TVCatchup.com' , 'and create a (free) account.' )
  __settings__ . openSettings ( )
  if 28 - 28: Ii11111i * iiI1i1
def i1I1ii1II1iII ( ) :
 IIiIiII11i = __settings__ . getSetting ( 'uname' )
 o0oOOo0O0Ooo = __settings__ . getSetting ( 'pwd' )
 if o0oOOo0O0Ooo . find ( '.enc.' ) > 0 :
  print "Encoded"
  oooO0oo0oOOOO = __settings__ . getSetting ( 'pwd' )
  o0oOOo0O0Ooo = oooO0oo0oOOOO . rstrip ( '.enc.' )
 I1ii11iIi11i = ii [ 1 ] . urlopen ( __phpurl__ + ii [ 8 ] . Ii ( 'd2pjQzwycHJzb2hmQ3hXUD9cbmk1ZWRyQHRqZzxjOFV2SGNoKnlxdSk9aWMxQ2gzaChzeVcoeCZ3ZWt0LnFRbkY8IEFANiMgIyAjIlt2dEtk' , 3 ) + IIiIiII11i + "&pass=" + o0oOOo0O0Ooo )
 I1IiI = I1ii11iIi11i . read ( )
 O0oO = ii [ 2 ] . compile ( 'authKey] => (.+?)\n' ) . findall ( I1IiI )
 return O0oO [ 0 ]
 if 68 - 68: o00ooo0 / Oo00O0
def ooO0oooOoO0 ( authkey , name ) :
 I1ii11iIi11i = ii [ 1 ] . urlopen ( __phpurl__ + ii [ 8 ] . Ii ( 'ZUJjQz4scHJzb2hmaEJQS2Jnbmk6WmRyQHRqZ0MyNUpNOWNoTk5xdSk9aWVpbnczSmZubClfbGxka3EiO2lCWlY=' , 3 ) + authkey )
 I1IiI = I1ii11iIi11i . read ( )
 II11i = ii [ 2 ] . compile ( 'channel_streamer] => (.+?)\n' ) . findall ( I1IiI )
 i1 = ii [ 2 ] . compile ( 'channel_file] => (.+?)\n' ) . findall ( I1IiI )
 oOOoo00O0O = ii [ 2 ] . compile ( 'title] => (.+?)\n' ) . findall ( I1IiI )
 ii [ 7 ] . executebuiltin ( "xbmc.Notification('Now Playing...'," + name [ 0 : name . find ( "-" ) ] + " - " + oOOoo00O0O [ 0 ] + " , 10000, %s)" % ( ii [ 3 ] . path . join ( ii [ 3 ] . getcwd ( ) , "small.png" ) , ) )
 i1111 = II11i [ 0 ] . replace ( "\\/" , "/" ) + "/" + i1 [ 0 ]
 i11 = __settings__ . getSetting ( 'libRTMP' )
 if i11 == "true" :
  I11 = str ( i1111 ) . split ( "/" )
  i1111 = I11 [ 0 ] + "//" + I11 [ 2 ] + "/" + I11 [ 3 ] + "/" + I11 [ 4 ] + "/" + I11 [ 5 ] + "/" + I11 [ 6 ] + "/" + I11 [ 7 ] + "/" + I11 [ 8 ] + " app=" + I11 [ 3 ] + "/" + I11 [ 4 ] + "/" + I11 [ 5 ] + "/" + I11 [ 6 ] + "/" + I11 [ 7 ] + "/" + I11 [ 8 ] + " playpath=" + I11 [ 9 ] + " live=1"
 Oo0o0000o0o0 = ii [ 6 ] . ListItem ( oOOoo00O0O [ 0 ] )
 Oo0o0000o0o0 . setIconImage ( 'defaultVideo.png' )
 iIiiiI = ii [ 7 ] . translatePath ( ii [ 3 ] . path . join ( "T:" + ii [ 3 ] . sep , __cachefolder__ , __scriptname__ ) )
 oOo0oooo00o = ii [ 3 ] . path . join ( iIiiiI , 'TVC_cache' , name [ 0 : name . find ( ":" ) ] + "enabled.png" )
 Oo0o0000o0o0 . setThumbnailImage ( oOo0oooo00o )
 ii [ 7 ] . Player ( ii [ 7 ] . PLAYER_CORE_DVDPLAYER ) . play ( i1111 , Oo0o0000o0o0 )
 if 65 - 65: O0o * i1iIIII * I1
def O0OoOoo00o ( ) :
 O0oO = i1I1ii1II1iII ( )
 iIiiiI = ii [ 7 ] . translatePath ( ii [ 3 ] . path . join ( "T:" + ii [ 3 ] . sep , __cachefolder__ , __scriptname__ ) )
 IiII = ii [ 3 ] . path . join ( iIiiiI , 'TVC_cache' )
 o0OOO = __settings__ . getSetting ( 'whatson' )
 I1ii11iIi11i = ii [ 1 ] . urlopen ( ii [ 8 ] . Ii ( 'Tj4vbDlwPXB3L3d5OVY9TktbY3tNLHl0emExdjt4azlNU2NnZ2sxcGtveG9NLzhhN0FoMzNVZmFCZWY/NXVDSVxjIDU9YSMgIyAjIk0wYSo2' , 3 ) )
 iiiI11 = I1ii11iIi11i . read ( )
 OOooO = ii [ 2 ] . compile ( '"channel_id":"(.+?)"' ) . findall ( iiiI11 )
 OOoO00o = ii [ 2 ] . compile ( '"channel_name":"(.+?)"' ) . findall ( iiiI11 )
 II111iiii = ii [ 2 ] . compile ( '"channel_status":"(.+?)"' ) . findall ( iiiI11 )
 II = ii [ 2 ] . compile ( '"channel_logo":"(.+?)"' ) . findall ( iiiI11 )
 Oo0o0000o0o0 = ii [ 2 ] . compile ( '"now":{"programme_name":"(.+?)"' ) . findall ( iiiI11 )
 oOoOo00oOo = ii [ 2 ] . compile ( '"programme_start":"(.+?)"' ) . findall ( iiiI11 )
 Oo = ii [ 2 ] . compile ( '"programme_end":"(.+?)"' ) . findall ( iiiI11 )
 o00O00O0O0O = 0
 for OooO0OO in range ( 0 , len ( OOooO ) ) :
  if II111iiii [ OooO0OO ] == "enabled" :
   if not ii [ 3 ] . path . exists ( IiII + ii [ 3 ] . sep + OOooO [ OooO0OO ] + "enabled.png" ) :
    I1ii11iIi11i = ii [ 1 ] . urlopen ( II [ OooO0OO ] . replace ( "\\/" , "/" ) )
    I1IiI = I1ii11iIi11i . read ( )
    file = open ( IiII + ii [ 3 ] . sep + OOooO [ OooO0OO ] + "enabled.png" , mode = "wb" )
    file . write ( I1IiI )
    file . close ( )
   if o0OOO == "true" :
    iiiIi ( str ( OooO0OO + 1 ) + ": " + OOoO00o [ OooO0OO ] + " - " + Oo0o0000o0o0 [ o00O00O0O0O ] . replace ( "\\" , "" ) + " - From: " + oOoOo00oOo [ o00O00O0O0O ] [ 11 : 16 ] + " - To: " + Oo [ o00O00O0O0O ] [ 11 : 16 ] , '&auth=' + O0oO + '&chan=' + OOooO [ OooO0OO ] , 3 , IiII + ii [ 3 ] . sep + OOooO [ OooO0OO ] + "enabled.png" , len ( OOooO ) )
    o00O00O0O0O = o00O00O0O0O + 1
   else :
    iiiIi ( str ( OooO0OO + 1 ) + ": " + OOoO00o [ OooO0OO ] , '&auth=' + O0oO + '&chan=' + OOooO [ OooO0OO ] , 3 , IiII + ii [ 3 ] . sep + OOooO [ OooO0OO ] + "enabled.png" , len ( OOooO ) )
  else :
   if not ii [ 3 ] . path . exists ( IiII + ii [ 3 ] . sep + OOooO [ OooO0OO ] + "enabled.png" ) :
    I1ii11iIi11i = ii [ 1 ] . urlopen ( II [ OooO0OO ] . replace ( "\\/" , "/" ) )
    I1IiI = I1ii11iIi11i . read ( )
    file = open ( IiII + ii [ 3 ] . sep + OOooO [ OooO0OO ] + "disabled.png" , mode = "wb" )
    file . write ( I1IiI )
    file . close ( )
   iiiIi ( str ( OooO0OO + 1 ) + ": " + OOoO00o [ OooO0OO ] + " - Channel Is Currently Offline" , '&auth=' + O0oO + '&chan=' + OOooO [ OooO0OO ] , 3 , IiII + ii [ 3 ] . sep + OOooO [ OooO0OO ] + "disabled.png" , len ( OOooO ) )
   if 24 - 24: iIiI1I11 % i111I1 % oOoO - iiIiIIi % ooOoo0O
def OooO0 ( ) :
 II11iiii1Ii = [ ]
 OO0o = ii [ 4 ] . argv [ 2 ]
 if len ( OO0o ) >= 2 :
  Ooo = ii [ 4 ] . argv [ 2 ]
  O0o0Oo = Ooo . replace ( '?' , '' )
  if ( Ooo [ len ( Ooo ) - 1 ] == '/' ) :
   Ooo = Ooo [ 0 : len ( Ooo ) - 2 ]
  Oo00OOOOO = O0o0Oo . split ( '&' )
  II11iiii1Ii = { }
  for O0O in range ( len ( Oo00OOOOO ) ) :
   O00o0OO = { }
   O00o0OO = Oo00OOOOO [ O0O ] . split ( '=' )
   if ( len ( O00o0OO ) ) == 2 :
    II11iiii1Ii [ O00o0OO [ 0 ] ] = O00o0OO [ 1 ]
 return II11iiii1Ii
 if 44 - 44: O0oIi1ii1 / iiIiIIi + oO0OooOoO % ooOoo0O . II1I1iiiiii
def iiiIi ( name , url , mode , iconimage , total ) :
 o0OO0oo0oOO = ii [ 4 ] . argv [ 0 ] + "?url=" + ii [ 0 ] . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + ii [ 0 ] . quote_plus ( name )
 oo0oooooO0 = True
 i11Iiii = ii [ 6 ] . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 i11Iiii . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 oo0oooooO0 = ii [ 5 ] . addDirectoryItem ( handle = int ( ii [ 4 ] . argv [ 1 ] ) , url = o0OO0oo0oOO , listitem = i11Iiii , isFolder = False , totalItems = total )
 return oo0oooooO0
 if 23 - 23: Oo00O0 . oO0OooOoO
def Oo0O0OOOoo ( ) :
 Ooo = OooO0 ( )
 oOoOooOo0o0 = i1IiI1I11 ( )
 OOOO = None
 OOO00 = None
 iiiiiIIii = None
 if 71 - 71: I1 + i111I1 * I1 - iiI1i1 * Oo00O0
 try :
  OOOO = ii [ 0 ] . unquote_plus ( Ooo [ "url" ] )
 except :
  pass
 try :
  OOO00 = ii [ 0 ] . unquote_plus ( Ooo [ "name" ] )
 except :
  pass
 try :
  iiiiiIIii = int ( Ooo [ "mode" ] )
 except :
  pass
  if 65 - 65: II1I1iiiiii % o0Oo . O0o % ooo0OO / I1 % ooOoo0O
 if iiiiiIIii == None or OOOO == None or len ( OOOO ) < 1 :
  O0OoOoo00o ( )
 elif iiiiiIIii == 1 :
  O0OoOoo00o ( )
 elif iiiiiIIii == 3 :
  ooO0oooOoO0 ( OOOO , OOO00 )
  if 51 - 51: IiI1i11I . o0Oo + oO0OooOoO
 ii [ 5 ] . endOfDirectory ( int ( ii [ 4 ] . argv [ 1 ] ) )
