from django.shortcuts import render, redirect
from .models import student, stamp, stamp_collection

# Create your views here.
# 메인페이지
def main(request, student_id=None):
    if request.method == 'POST':
        student_id = request.POST.get('student_id')
        major = request.POST.get('major')

        student_info = student.objects.get(student_id=student_id, major=major)
        
        stamp_collections = stamp_collection.objects.filter(student=student_info)
  
        return render(request, 'Glover_back/user_page.html', {'student_info': student_info, 'stamp_collections':stamp_collections})

    return render(request, 'Glover_back/main.html')


# 관리자 페이지
def manager_page(request):
	return render(
		request,
		'manager_page/manager_page.html'
	)
 
 
# stamp 추가
def add_stamp(request):
    if request.method == 'POST':
        event_name = request.POST['event_name']
        event_info = request.POST['event_info']
        event_start = request.POST['event_start']
        event_end = request.POST['event_end']
        before_image = request.FILES.get('before_image') if 'before_image' in request.FILES else None
        after_image = request.FILES.get('after_image') if 'after_image' in request.FILES else None

        # 데이터 유효성 검사 및 저장
        if event_name and event_info and event_start and event_end  and before_image and after_image: #and before_image
            mystamp = stamp (
                event_name = event_name,
                event_info = event_info,
                event_start = event_start,
                event_end = event_end,
                before_image = before_image,
                after_image = after_image,
            )
            mystamp.save()
            return redirect('stamp_list')
        else:
            # 필요한 모든 데이터가 제출되지 않은 경우에 대한 처리
            error_message = "모든 필드를 입력해야 합니다."
    else:
        error_message = ""

    return render(request, 'manager_page/add_stamp.html', {'error_message': error_message})


# stamp 리스트
def stamp_list(request):
    stamps = stamp.objects.all()
    return render(request, 'manager_page/stamp_list.html', {'stamps': stamps})