from django.contrib import admin
from .models import Company,MedicalDetails,Medicine,Employee,Customer,Bill,EmployeeSalary,BillDetails,CustomerRequest,CompanyAccount,CompanyBank,EmployeeBank
# Register your models here.

admin.site.register(Company)
admin.site.register(MedicalDetails)
admin.site.register(Medicine)
admin.site.register(Employee)
admin.site.register(Bill)
admin.site.register(Customer)
admin.site.register(EmployeeSalary)
admin.site.register(EmployeeBank)
admin.site.register(BillDetails)
admin.site.register(CustomerRequest)
admin.site.register(CompanyAccount)
admin.site.register(CompanyBank)



