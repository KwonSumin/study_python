import sys,os
import configparser

config = configparser.ConfigParser()

resource = os.path.dirname(__file__) + '\resource';
sys.path.append(resource);

