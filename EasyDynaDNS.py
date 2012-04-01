#!/usr/bin/python
import urllib2, sys

from ConfigParser import ConfigParser


class Config:

    def __init__( self, cfg ):
        self.username = ""
        self.password = ""
        self.ip = ""
        self.hostname = ""
        self.tld = ""
        self.mx = ""
        self.backmx = ""
        self.wildcard = ""
        self.easydnsurl = ""
        # Config file skeleton in case the file doesn't exist
        self.newconfig = "[EasyDNSConfig]\nusername =\npassword =\nhostname =\nip =\ntld =\nmx =\nbackmx =\nwildcard =\neasydnsurl =\n"
      
        self.LoadConfig( cfg )
      
    
    def LoadConfig( self, cfg ):
        
        config = ConfigParser()
        
        # If cfg file not named, set default name
        if cfg == "":
            cfg = "EasyDynaDNS.cfg"
            
        # Read config file
        try:
            config.readfp( open( cfg ) )
        except IOError as ( errno, strerror ):
            print "Error: Config file may not exist, attempting to create %s." % ( cfg, )
            
            try:
                # If the file didn't exist, try to create a new one.
                fp = open( cfg, "w" )
            except IOError as ( errno, strerror) :
                print "Error: Could not open %s for writing: %i - %s" %s ( cfg, errno, strerror )
                sys.exit(1)
            except:
                print "Unspecified error."
                sys.exit(1)
                
            fp.write( self.newconfig )
            fp.close()
            print "Please fill in the config file %s values and run again." % ( cfg )
            sys.exit()
            
            
    


EZConfig = Config( "" )            
#EasyDynaDNS_URL = 'http://members.easydns.com/dyn/dyndns.php?hostname=dcb.david-c-brown.com&myip=1.1.1.1'
#Username = ''
#Password = ''

#PasswordManager = urllib2.HTTPPasswordMgrWithDefaultRealm()

#PasswordManager.add_password(None, EasyDynaDNS_URL, Username, Password)

#Authenticator = urllib2.HTTPBasicAuthHandler(PasswordManager)

#Opener = urllib2.build_opener(Authenticator)

#urllib2.install_opener(Opener)

#Page = urllib2.urlopen(EasyDynaDNS_URL)

#print Page.readlines()[0][:-1]
