from django.contrib import admin

from .models import Area, Sector, Route, Degree, Repetition, Presa, PresaCatch, Seguro


class SectorAdmin(admin.ModelAdmin):
    list_display = ("name", "area",)
    list_filter = ("area",)


class RouteSeguroInline(admin.TabularInline):
    model = Route.seguros.through
    extra = 1


class RoutePresasInline(admin.TabularInline):
    model = PresaCatch
    extra = 1


class RouteAdmin(admin.ModelAdmin):
    list_display = ("name", "degree", "sector",)
    list_filter = ("sector", "type", "degree")
    inlines = (RouteSeguroInline, RoutePresasInline)


admin.site.register(Area)
admin.site.register(Sector, SectorAdmin)
admin.site.register(Route, RouteAdmin)
admin.site.register(Degree)
admin.site.register(Repetition)
admin.site.register(Presa)
admin.site.register(PresaCatch)
admin.site.register(Seguro)
