from django.contrib import admin

from school_absenteeism.absences import models as absences

admin.site.site_header = "School Absenteeism Database"


class HomeRoomInline(admin.TabularInline):
    model = absences.HomeRoom


class HomeRoomAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'school', 'grade',)
    list_filter = ('school', 'grade',)
    search_fields = ('first_name', 'last_name', 'grade', 'school__name')
admin.site.register(absences.HomeRoom, HomeRoomAdmin)


class SchoolAdmin(admin.ModelAdmin):
    ordering = ('name',)
    list_display = ('name', 'street1', 'city', 'state',)
    list_filter = ('city', 'state', 'zip_code',)
    inlines = (HomeRoomInline,)
    search_fields = ('name', 'street1', 'street2', 'city', 'state', 'zip')
    fieldsets = (
        (None, {
            'fields': ('name',)
        }),
        ('Address', {
            'fields': ('street1', 'street2', 'city', 'state', 'zip_code',)
        }),
    )
admin.site.register(absences.School, SchoolAdmin)


class AbsenceInline(admin.TabularInline):
    model = absences.Absence


class AbsenceAdmin(admin.ModelAdmin):
    date_hierarchy = 'date'
    ordering = ('-date',)
    list_display = ('student', 'home_room', 'school', 'date',)
    list_filter = ('home_room__school', 'student',)
    list_select_related = ('home_room__school',)
    search_fields = ('student__first_name', 'student__last_name',)
    
    def school(self, obj):
        return obj.home_room.school
admin.site.register(absences.Absence, AbsenceAdmin)


class StudentInline(admin.TabularInline):
    model = absences.Student


class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name',)
    inlines = (AbsenceInline,)
    search_fields = ('first_name', 'last_name',)
admin.site.register(absences.Student, StudentAdmin)


class ParentAdmin(admin.ModelAdmin):
    list_filter = ('city', 'state', 'zip_code',)
    list_display = ('first_name', 'last_name', 'street1', 'city', 'state', 'zip_code')
    search_fields = ('first_name', 'last_name', 'street1', 'street2', 'city', 'state', 'zip_code',)
    inlines = (StudentInline,)
    fieldsets = (
        (None, {
            'fields': ('first_name', 'middle_initial', 'last_name')
        }),
        ('Contact Information', {
            'fields': ('email', 'phone',)
        }),
        ('Address', {
            'fields': ('street1', 'street2', 'city', 'state', 'zip_code',)
        }),
    )
admin.site.register(absences.Parent, ParentAdmin)


class AbsenceReasonAdmin(admin.ModelAdmin):
    list_display = ('label', 'description',)
admin.site.register(absences.AbsenceReason, AbsenceReasonAdmin)


