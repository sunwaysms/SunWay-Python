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

#ارسال پیام کوتاه به یک شماره خاص
Sunway.sendarray(UserName= 'xxx', Password= 'xxx', RecipientNumber= '09xxxxxxxxx', MessageBody= '', SpecialNumber= 'xxx')

#دریافت موجودی اعتبار کاربر در پنل سان وی
Sunway.getcredit(Username='xxx', Password='xxx')

#دریافت وضعیت پیام های ارسال شده 
Sunway.messagestatus(UserName='xxx', Password='xxx', MessageID='xxxxxxxxx')

#ارسال یک پیام به چندین شماره به صورت همزمان
Sunway.multisendarray(UserName= 'xxx', Password= 'xxx', RecipientNumber= ['xxxxxx','xxxxxx'], MessageBody= '', SpecialNumber= 'xxx')

#ارسال پیامک در زمان خاص
Sunway.sendarrayschedule(UserName= 'xxx', Password= 'xxx', RecipientNumber= '09xxxxxxxxx', MessageBody= '', SpecialNumber= 'xxx', Year= 'xxx', Month= 'xxx', Day= 'xxx', Hour= 'xxx', Minute= 'xxx')

#

```


## license
Released under the MIT License.
