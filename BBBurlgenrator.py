import hashlib 

#Provide URN of BBB server eg. "sub.domain.com"
DOMAIN=""
# if https is enabled then set True else False
HTTPS=True
# shared secret
SECRET=""
# api name for url eg. "create"
API_NAME=""
# parametesrs in string format eg ."name=Test+Meeting&meetingID=abc123&attendeePW=111222&moderatorPW=333444"
PARAMETERS=""
class CheckSumGenerator:
    def __init__(self,secret):
        self.secret=secret

    def setChecksum(self,apiName,parameters):
        checksumRawData=(apiName+parameters+self.secret).encode('utf-8')
        self.checksum=hashlib.sha1(checksumRawData).hexdigest()

    def getChecksum(self):
        return self.checksum


class UrlGenerator(CheckSumGenerator):
    def __init__(self,domain,secret,https=False):
        super().__init__(secret)
        self.bbbUrl=("https://","http://")[https] + domain+'/bigbluebutton/api/'

    def getURL(self,apiName,parameters):
        super().setChecksum(apiName,parameters)
        url= self.bbbUrl+apiName+ "?"+parameters+"&checksum="+self.checksum
        return url

#C=CheckSumGenerator(SECRET)
#C.setChecksum(API_NAME,PARAMETERS)
#CS=C.getChecksum()
#print(CS);
if any(v is "" for v in [DOMAIN,SECRET,API_NAME,PARAMETERS]):
    print("Provide data in variables")
    import sys
    sys.exit()
 
U=UrlGenerator(DOMAIN,SECRET,True)
url=U.getURL(API_NAME,PARAMETERS);
print(url);
