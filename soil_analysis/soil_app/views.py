from django.shortcuts import render

# Create your views here.
from .forms import SoilUploadForm
from .utils import analyze_soil_data, get_ai_suggestions

def upload_soil_data(request):
    if request.method == 'POST':
        form = SoilUploadForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save()
            grade, graph_html, nutrient_levels = analyze_soil_data(instance.csv_file.path)
            suggestions = get_ai_suggestions(grade, nutrient_levels)
            
            context = {
                'form': form,
                'grade': grade,
                'graph_html': graph_html,
                'suggestions': suggestions,
            }
            return render(request, 'soil_app/results.html', context)
    else:
        form = SoilUploadForm()
    
    return render(request, 'soil_app/upload.html', {'form': form})