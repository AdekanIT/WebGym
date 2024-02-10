from django.contrib import admin
from .models import Order, Comments, Instructors, Branches, BranchInfo

# Register your models here.
admin.site.register(Branches)
admin.site.register(Instructors)
admin.site.register(Comments)
admin.site.register(Order)
admin.site.register(BranchInfo)
