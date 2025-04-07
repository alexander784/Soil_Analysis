from django.shortcuts import render
from django.http import JsonResponse
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

def chatbot_response(request):
    if request.method == 'POST':
        user_message = request.POST.get('message', '').lower()
        # Dummy nutrient levels for demo 
        nutrient_levels = {'N': 75, 'P': 45, 'K': 120, 'pH': 6.5}
        
        # Simple rule-based responses
        if 'nitrogen' in user_message:
            response = f"Nitrogen level is {nutrient_levels['N']}. "
            if nutrient_levels['N'] < 50:
                response += "Consider adding nitrogen-rich fertilizer like urea."
            else:
                response += "Nitrogen levels are adequate."
        elif 'crop' in user_message:
            grade = 1 
            response = "Based on current soil conditions, suitable crops include: "
            response += "Wheat, barley, or soybeans" if grade == 1 else "Corn or vegetables"
        else:
            response = "I can help with soil improvement tips or crop suggestions. What would you like to know?"
        
        return JsonResponse({'response': response})
    return JsonResponse({'response': 'Error: Invalid request'})