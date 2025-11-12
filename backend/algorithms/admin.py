from django.contrib import admin
from .models import MLAlgorithm, ComparisonGraph

@admin.register(MLAlgorithm)
class MLAlgorithmAdmin(admin.ModelAdmin):
    list_display = ('name', 'algorithm_type', 'accuracy', 'created_at')
    list_filter = ('algorithm_type', 'created_at')
    search_fields = ('name', 'algorithm_type')

@admin.register(ComparisonGraph)
class ComparisonGraphAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    filter_horizontal = ('algorithms',)

admin.site.site_header = "ML Algorithms Admin"
admin.site.site_title = "ML Algorithms Portal"
admin.site.index_title = "Welcome to ML Algorithms Admin Panel"
