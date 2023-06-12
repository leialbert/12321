from django.contrib import admin

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
    list_per_page = 50
    list_max_show_all = 200
    
    def requested_at_custom(self, obj):
        return obj.requested_at.strftime('%Y-%m-%d %H:%M:%S.%f')
    requested_at_custom.short_description = 'Requested At'

        