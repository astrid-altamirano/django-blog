# blogging/admin.py
# Ready to submit
from django.contrib import admin
from polling.models import Poll

admin.site.register(Poll)