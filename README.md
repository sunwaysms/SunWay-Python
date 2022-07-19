# SunWay Python
SunWay sms webservice Python package

## installation
You can install SunWay python package with pip:

```shell
pip install sunwaysms
```

## usage

```python
from sunwaysms import Sunway

#send a single message to a single number:
Sunway.sendarray(UserName= 'xxx', Password= 'xxx', RecipientNumber= '09xxxxxxxxx', MessageBody= '', SpecialNumber= 'xxx')

#get the Credit of User:
Sunway.getcredit(Username='xxx', Password='xxx')

#get the status of massages:
Sunway.messagestatus(UserName='xxx', Password='xxx', MessageID='xxxxxxxxx')

#send a single message to multiple numbers:
Sunway.multisendarray(UserName= 'xxx', Password= 'xxx', RecipientNumber= ['xxxxxx','xxxxxx'], MessageBody= '', SpecialNumber= 'xxx')
```


## license
Released under the MIT License.
