import csv

from django.contrib import admin
from vaas.router.models import PositiveUrl, Route
from vaas.router.forms import RouteModelForm


class RouteAdmin(admin.ModelAdmin):
    form = RouteModelForm
    filter_horizontal = ('clusters',)
    search_fields = ['condition', 'clusters__name', 'director__name']
    list_display = ['condition', 'director', 'priority', 'action', 'get_clusters']
    fieldsets = (
        (None, {
            'fields': ('condition', 'positive_urls', 'priority', 'action', 'clusters', 'director')
        }),
    )

    def get_clusters(self, obj):
        return [c.name for c in obj.clusters.all()]


admin.site.register(Route, RouteAdmin)
