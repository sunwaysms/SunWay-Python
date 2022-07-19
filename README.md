# وب سرویس پیام کوتاه سان وی برای برنامه نویسیتان پایتون
اگر برنامه نویس پایتون هستید و نیاز دارید از وب سرویس پیام کوتاه استفاده کنید بهترین گزینه برای شما سان وی است به راحتی با ثبت نام در این سایت از پنل اختصاصی و وب سرویس این شرکت استفاده کنید و پروژه خود را مجهز به پیام کوتاه کنید.

در این پکیج موارد لازم برای راحتی و اتصال سریع سامانه پیام کوتاه سان وی برای شما دیده شده 

## نصب و اتصال به پروژه شما
شما به راحتی میتواند با دستور زیر از مخزن پایتون پکیج سان وی را در کامپیوتر و یا سرور خود نصب کنید

```shell
pip install sunwaysms
```

## usage

```python
#فراخوانی پکیج سان وی در هر جای پروژه که نیاز دارید 
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
