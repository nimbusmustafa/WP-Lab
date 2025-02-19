from django.shortcuts import render

def generate_cover(request):
    # Default values if form not submitted yet
    background_color = '#ffffff'
    font_color = '#000000'
    font_size = 24
    font_family = 'Arial'  # Default font family
    title_text = 'Magazine Title'
    description_text = 'Description goes here.'
    
    if request.method == 'POST':
        background_color = request.POST.get('background_color', '#ffffff')
        font_color = request.POST.get('font_color', '#000000')
        font_size = int(request.POST.get('font_size', 24))
        font_family = request.POST.get('font_family', 'Arial')  # Get font family from form
        title_text = request.POST.get('title_text', 'Magazine Title')
        description_text = request.POST.get('description_text', 'Description goes here.')
    
    return render(request, 'magazine_cover/index.html', {  # Path to your template
        'background_color': background_color,
        'font_color': font_color,
        'font_size': font_size,
        'font_family': font_family,  # Pass font family to template
        'title_text': title_text,
        'description_text': description_text,
    })
