from django.contrib import admin
from django.urls import path
from django.http import JsonResponse, HttpResponse
from django.views.generic import TemplateView
from algorithms.models import MLAlgorithm
import json

def algorithms_api(request):
    algorithms = list(MLAlgorithm.objects.values())
    return JsonResponse(algorithms, safe=False)

def algorithm_detail_api(request, algorithm_id):
    try:
        algorithm = MLAlgorithm.objects.get(id=algorithm_id)
        all_algorithms = list(MLAlgorithm.objects.values('id', 'name', 'accuracy', 'algorithm_type'))
        
        response_data = {
            'algorithm': {
                'id': algorithm.id,
                'name': algorithm.name,
                'algorithm_type': algorithm.algorithm_type,
                'short_description': algorithm.short_description,
                'implementation_code': algorithm.implementation_code,
                'accuracy': algorithm.accuracy,
                'use_cases': algorithm.use_cases,
                'pros': algorithm.pros,
                'cons': algorithm.cons,
            },
            'all_algorithms': all_algorithms
        }
        return JsonResponse(response_data)
    except MLAlgorithm.DoesNotExist:
        return JsonResponse({'error': 'Algorithm not found'}, status=404)

# Serve homepage
class HomePageView(TemplateView):
    template_name = 'home.html'

# Serve algorithm detail page  
class AlgorithmDetailView(TemplateView):
    template_name = 'algorithm_detail.html'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/algorithms/', algorithms_api),
    path('api/algorithm/<int:algorithm_id>/', algorithm_detail_api),
    path('algorithm/<int:algorithm_id>/', AlgorithmDetailView.as_view(), name='algorithm_detail'),
    path('', HomePageView.as_view(), name='home'),
]
