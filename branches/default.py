moduleNames= ['urllib2','os','sys']
modules = map(__import__, moduleNames)
modules
modules[2].path.insert(0, modules[1].path.join(modules[1].getcwd(), 'lib'))
modules[2].path.insert(0, modules[1].path.join(modules[1].getcwd(), 'resources'))

tmp_lib=__import__('TVClibs')
tmp_lib2=__import__('TVClibs2',globals())

__scriptname__ = "plugin.video.tvcatchup"
__author__     = 'dj_gerbil [tvc@killergerbils.co.uk]'
__svn_url__    = ""
__version__    = "1.3.1"
    
tmp_lib2.Oo0O0OOOoo()
    
