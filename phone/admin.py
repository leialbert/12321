from django.contrib import admin
from django.utils import timezone
import pytz

from .models import PhoneNumber, RequestLog

@admin.register(PhoneNumber)
class PhoneNumberAdmin(admin.ModelAdmin):
    list_display = ('number', 'created_at')
    search_fields = ('number',)
    ordering = ('-created_at',)
    fields = ('number',)
    readonly_fields = ('created_at',)
    list_per_page = 50
    empty_value_display = '-empty-'
    list_max_show_all = 200

@admin.register(RequestLog)
class RequestLogAdmin(admin.ModelAdmin):
    list_display = ('requested_at_custom', 'callId','caller', 'callee', 'block', 'request_ip')
    search_fields = ('caller', 'callee', 'request_ip')
    readonly_fields = ('requested_at', 'callId', 'caller', 'callee', 'block', 'request_ip')
    ordering = ('-requested_at',)
    list_filter = ('block','request_ip')
    list_per_page = 50
    list_max_show_all = 200
    
    def requested_at_custom(self, obj):
        requested_at_localtime = timezone.localtime(obj.requested_at, timezone=pytz.timezone('Asia/Shanghai'))
        return requested_at_localtime.strftime('%Y-%m-%d %H:%M:%S.%f')
    requested_at_custom.short_description = 'Requested At'

        