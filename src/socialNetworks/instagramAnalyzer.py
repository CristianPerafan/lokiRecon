import os
import json
import codecs


from src import consolePrint as cp
from instagram_private_api import Client,ClientCookieExpiredError, ClientLoginRequiredError, ClientError, ClientThrottledError
from src import config


class InstagramAnalyzer:
    def __init__(self):   
        self.api = None
        user = config.getInstagramUsername()
        password = config.getInstagramPassword()
        self.login(user,password)


    
        

    def analyze(self):
        cp.printConsole("Enter the username of the profile you want to analyze",cp.YELLOW)
        userName = input(">:")
        cp.printConsole("Analyzing profile: "+userName,cp.GREEN)
        
    def login(self,username:str,password:str):
        try:
            settings_file="config/settings.json"
            if not os.path.isfile(settings_file):
                self.api = Client(
                    username=username,password=password,
                    on_login=lambda x: self.onlogin_callback(x,settings_file))

            else:
                # reuse auth settings
                with open(settings_file) as file_data:
                    cached_settings = json.load(file_data, object_hook=self.from_json)
                self.api = Client(
                    username=username,password=password,
                    settings=cached_settings)
                

        except (ClientCookieExpiredError, ClientLoginRequiredError) as e:
            # Login expired
            self.api = Client(auto_patch=True, authenticate=True, username=username, password=password,
                                 on_login=lambda x: self.onlogin_callback(x, settings_file))
        except ClientError as e:
            cp.printConsole('ClientError {0!s} (Code: {1:d}, Response: {2!s})'.format(e.msg, e.code, e.error_response), cp.RED)
            error = json.loads(e.error_response)
            cp.printout(error['message'], cp.RED)

    def from_json(self, json_object):
        if '__class__' in json_object and json_object['__class__'] == 'bytes':
            return codecs.decode(json_object['__value__'].encode(), 'base64')
        return json_object
    def to_json(self, python_object):
        if isinstance(python_object, bytes):
            return {'__class__': 'bytes',
                    '__value__': codecs.encode(python_object, 'base64').decode()}
        raise TypeError(repr(python_object) + ' is not JSON serializable')
    
    def onlogin_callback(self,api,settings_file):
        settings = api.settings
    
        with open(settings_file, 'w') as outfile:
            json.dump(settings, outfile, default=self.to_json)
            cp.printConsole('SAVED: {0!s}'.format(settings_file), cp.GREEN)