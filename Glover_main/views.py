from django.shortcuts import render
from .models import student, stamp, stamp_collection

# Create your views here.
def main(request, student_id=None):
    if request.method == 'POST':
        student_id = request.POST.get('student_id')
        major = request.POST.get('major')

        student_info = student.objects.get(student_id=student_id, major=major)
        
        stamp_collections = stamp_collection.objects.filter(student=student_info)
  
        return render(request, 'Glover_back/user_page.html', {'student_info': student_info, 'stamp_collections':stamp_collections})

    return render(request, 'Glover_back/main.html')