from django.db import models

class MLAlgorithm(models.Model):
    ALGORITHM_TYPES = [
        ('classification', 'Classification'),
        ('regression', 'Regression'),
        ('clustering', 'Clustering'),
        ('dimensionality', 'Dimensionality Reduction'),
        ('neural', 'Neural Networks'),
        ('ensemble', 'Ensemble Methods'),
    ]
    
    name = models.CharField(max_length=100)
    algorithm_type = models.CharField(max_length=50, choices=ALGORITHM_TYPES)
    short_description = models.TextField()
    implementation_code = models.TextField()
    accuracy = models.FloatField(null=True, blank=True)
    use_cases = models.TextField()
    pros = models.TextField()
    cons = models.TextField()
    wikipedia_url = models.URLField(blank=True, null=True, help_text="Wikipedia page URL for this algorithm")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name

class ComparisonGraph(models.Model):
    title = models.CharField(max_length=200)
    algorithms = models.ManyToManyField(MLAlgorithm)
    comparison_data = models.JSONField(default=dict)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
