from django.db import models
    
class PhoneNumber(models.Model):
    number = models.CharField('电话号码',max_length=15, unique=True)
    created_at = models.DateTimeField('创建时间', auto_now_add=True)

    def __str__(self):
        return self.number
    
class RequestLog(models.Model):
    requested_at = models.DateTimeField('请求时间', auto_now_add=True)
    caller = models.CharField('主叫号码',max_length=15)
    callee = models.CharField('被叫号码',max_length=15)
    block = models.BooleanField('是否拦截', default=False)
    request_ip = models.CharField('请求IP',max_length=15)
    callId = models.CharField('Call ID',max_length=50)
    

    def __str__(self):
        return self.requested_at.strftime('%Y-%m-%d %H:%M:%S.%f')