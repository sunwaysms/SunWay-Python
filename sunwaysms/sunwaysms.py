from zeep import Client

wsdl = 'https://sms.sunwaysms.com/SMSWS/SOAP.asmx?wsdl'

client = Client(wsdl=wsdl)

array_of_string_type = client.get_type("ns0:ArrayOfString")
array_of_long_type = client.get_type("ns0:ArrayOfLong")

class Sunway:

    #send a single message to a single number:
    def sendarray(UserName, Password, RecipientNumber, MessageBody, SpecialNumber):
        RecipientNumber1 = array_of_string_type([RecipientNumber])
        print(client.service.SendArray(UserName, Password, RecipientNumber1, MessageBody, SpecialNumber))

    #send a single message to multiple numbers:
    def multisendarray(UserName, Password, RecipientNumber, MessageBody, SpecialNumber):
        RecipientNumber1 = array_of_string_type(RecipientNumber)
        print(client.service.SendArray(UserName, Password, RecipientNumber1, MessageBody, SpecialNumber))

    #get the status of massages:
    def messagestatus(UserName, Password, MessageID):
        MessageID1 = array_of_long_type([MessageID])
        print(client.service.GetMessageStatus(UserName, Password, MessageID1))

    #get the Credit of User:
    def getcredit(Username, Password):
         print(client.service.GetCredit(Username, Password))


    def GetUserInfo(Username, Password):
        print(client.service.GetUserInfo(Username, Password))
        
    #Scheduled sending of SMS for the number:
    def sendarrayschedule(UserName, Password, RecipientNumber, MessageBody, SpecialNumber, Year, Month, Day, Hour, Minute):
        RecipientNumber1 = array_of_string_type([RecipientNumber])
        print(client.service.SendArraySchedule(UserName, Password, RecipientNumber1, MessageBody, SpecialNumber, Year, Month, Day, Hour, Minute))


    def getinboxmessagewithnumber(UserName, Password, NumberOfMessage, SpecialNumber):
        
        print(client.service.GetInboxMessageWithNumber(UserName, Password, int(NumberOfMessage), SpecialNumber))