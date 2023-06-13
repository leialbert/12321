from django.core.management.base import BaseCommand, CommandError
from django.db import IntegrityError
from phone.models import PhoneNumber

class Command(BaseCommand):
    help = 'Imports phone numbers from a given text file'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='The path to the text file to import numbers from')

    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path']

        # 打开文件
        with open(file_path, 'r') as f:
            # 读取所有行
            lines = f.readlines()

        # 创建PhoneNumber实例列表
        phone_numbers = [PhoneNumber(number=line.strip()) for line in lines]

        try:
            # 批量创建PhoneNumber实例
            PhoneNumber.objects.bulk_create(phone_numbers, ignore_conflicts=True)
        except IntegrityError:
            # 如果有重复的电话号码，就忽略它们
            self.stdout.write(self.style.ERROR('An error occurred while importing phone numbers.'))

        self.stdout.write(self.style.SUCCESS('Successfully imported phone numbers from {}'.format(file_path)))
