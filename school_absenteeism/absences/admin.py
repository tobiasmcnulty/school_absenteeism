from django.contrib import admin

from school_absenteeism.absences import models as absences

admin.site.site_header = "School Absenteeism Database"

class HomeRoomInline(admin.TabularInline):
    model = absences.HomeRoom


class HomeRoomAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'grade',)
admin.site.register(absences.HomeRoom, HomeRoomAdmin)


class SchoolAdmin(admin.ModelAdmin):
    list_display = ('name',)
    inlines = (HomeRoomInline,)
    search_fields = ('name',)
admin.site.register(absences.School, SchoolAdmin)


class AbsenceInline(admin.TabularInline):
    model = absences.Absence


class AbsenceAdmin(admin.ModelAdmin):
    list_display = ('student', 'home_room', 'date')
    search_fields = ('student__first_name', 'student__last_name',)
admin.site.register(absences.Absence, AbsenceAdmin)


class StudentInline(admin.TabularInline):
    model = absences.Student


class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name',)
    inlines = (AbsenceInline,)
    search_fields = ('first_name', 'last_name',)
admin.site.register(absences.Student, StudentAdmin)


class ParentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name',)
    search_fields = ('first_name', 'last_name',)
    inlines = (StudentInline,)
admin.site.register(absences.Parent, ParentAdmin)


class AbsenceReasonAdmin(admin.ModelAdmin):
    list_display = ('label', 'description',)
admin.site.register(absences.AbsenceReason, AbsenceReasonAdmin)


