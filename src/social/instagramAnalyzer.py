import os
import json
import codecs
import re





from src import consolePrint as cp
from instagram_private_api import Client,ClientCookieExpiredError, ClientLoginRequiredError, ClientError, ClientThrottledError
from src import config
from src.pdfReport import PDFReport

class InstagramAnalyzer:
    def __init__(self):   
        self.api = None
        user = config.getInstagramUsername()
        password = config.getInstagramPassword()
        self.login(user,password)
        self.isPrivate = False
        self.datFolder = "data"
        self.pdfReport = PDFReport()

    def analyze(self):

        try: 
            cp.printConsole("Enter the username of the profile you want to analyze",cp.YELLOW)
            userName = input(">:")
            userInfo = self.getUserInfo(userName)
            reportFileName = "reports/"+userName+"-instagram-report.pdf"
            self.pdfReport.generateReportFromInstagramData(userInfo,reportFileName)

        except ClientError as e:
            cp.printConsole('ClientError {0!s} (Code: {1:d}, Response: {2!s})'.format(e.msg, e.code, e.error_response), cp.RED)
            error = json.loads(e.error_response)
            cp.printout(error['message'], cp.RED)

    def getUserInfo(self,userName:str):
        
        response = self.api.username_info(userName)

        # Get user info
        userInfo = response['user']
        

        # Check if the profile is private
        if 'is_private' in userInfo.keys() and userInfo['is_private'] is not None:
            if userInfo['is_private']:
                self.isPrivate = True
                cp.printConsole("The profile is private",cp.RED)
                return

        if "full_name" in userInfo.keys():
            fullName = userInfo['full_name']
        if "biography" in userInfo.keys():
            biography =  re.sub(r'[^\w\s\U0001F600-\U0001F64F]', '', userInfo['biography'])
        if "external_url" in userInfo.keys():
            externalUrl = userInfo['external_url']
        if "category" in userInfo.keys():
            category = userInfo['category']
        if "is_business" in userInfo.keys():
            isBusiness = userInfo['is_business']
        if "city_name" in userInfo.keys():
            cityName = userInfo['city_name']
        if "public_email" in userInfo.keys():
            publicEmail = userInfo['public_email']
        if "public_phone_number" in userInfo.keys():
            publicPhoneNumber = userInfo['public_phone_number']
        if "follower_count" in userInfo.keys():
            followerCount = userInfo['follower_count']
        if "following_count" in userInfo.keys():
            followingCount = userInfo['following_count']

        userInfoFiltered = {
            "username":userName,
            "full_name":fullName,
            "biography":biography,
            "external_url":externalUrl,
            "category":category,
            "is_business":isBusiness,
            "city_name":cityName,
            "public_email":publicEmail,
            "public_phone_number":publicPhoneNumber,
            "follower_count":followerCount,
            "following_count":followingCount
        }

        
        with open("data/"+userName+".json", 'w') as outfile:
            json.dump(userInfoFiltered, outfile)
            cp.printConsole('SAVED: {0!s}'.format(userName+".json"), cp.GREEN)

        return userInfoFiltered
        
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
            cp.printout(": ", cp.RED)
            cp.printout(e.msg, cp.RED)
            cp.printout("\n")
            if 'challenge' in error:
                print("Please follow this link to complete the challenge: " + error['challenge']['url'])
            exit(9)

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