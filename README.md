# وب سرویس پیام کوتاه سان وی برای برنامه نویسان پایتون
اگر برنامه نویس پایتون هستید و نیاز دارید از وب سرویس پیام کوتاه استفاده کنید بهترین گزینه برای شما سان وی است به راحتی با ثبت نام در این سایت از پنل اختصاصی و وب سرویس این شرکت استفاده کنید و پروژه خود را مجهز به پیام کوتاه کنید.

در این پکیج موارد لازم برای راحتی و اتصال سریع سامانه پیام کوتاه سان وی برای شما دیده شده 

## نصب و اتصال به پروژه شما
شما به راحتی میتواند با دستور زیر از مخزن پایتون پکیج سان وی را در کامپیوتر و یا سرور خود نصب کنید

```shell
pip install sunwaysms
```

## طریقه استفاده از دستور العمل ها در پروژه شما


#فراخوانی پکیج سان وی در هر جای پروژه که نیاز دارید 
```python
from sunwaysms import Sunway
```

#ارسال پیام کوتاه به یک شماره خاص
```python
Sunway.sendarray(UserName= 'xxx', Password= 'xxx', RecipientNumber= '09xxxxxxxxx', MessageBody= '', SpecialNumber= 'xxx')
```

#دریافت موجودی اعتبار کاربر در پنل سان وی
```python
Sunway.getcredit(Username='xxx', Password='xxx')
```

#دریافت وضعیت پیام های ارسال شده 
```python
Sunway.messagestatus(UserName='xxx', Password='xxx', MessageID='xxxxxxxxx')
```

#دریافت اطلاعات کاربر از سامانه مانند موجودی حساب، پیام های ارسال شده و دریافت شده و موارد دیگر.
```python
Sunway.GetUserInfo(Username= username, Password= password)
```

#ارسال یک پیام به چندین شماره به صورت همزمان
```python
Sunway.multisendarray(UserName= 'xxx', Password= 'xxx', RecipientNumber= ['xxxxxx','xxxxxx'], MessageBody= '', SpecialNumber= 'xxx')
```

#ارسال پیامک در زمان خاص
```python
Sunway.sendarrayschedule(UserName= 'xxx', Password= 'xxx', RecipientNumber= '09xxxxxxxxx', MessageBody= '', SpecialNumber= 'xxx', Year= 'xxx', Month= 'xxx', Day= 'xxx', Hour= 'xxx', Minute= 'xxx')
```

#




## license
Released under the MIT License.
