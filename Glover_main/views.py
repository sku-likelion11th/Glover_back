from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import student, stamp, stamp_collection
from django.http import HttpResponse
from django.contrib.sessions.models import Session
from django.db import transaction
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import os

# Create your views here.
# 메인페이지
def main(request, student_id=None):
    if request.method == 'POST':
        student_id = request.POST.get('student_id')
        major = request.POST.get('major')

        student_info = student.objects.get(student_id=student_id, major=major)
        stamp_collections = stamp_collection.objects.filter(student=student_info)

        agreed = student.objects.get(student_id=student_id)
        agreed.consent = True
        # is_agreed = agreed.consent
        # print(is_agreed)

        return render(request, 'user_page/search.html', {'student_info': student_info, 'stamp_collections':stamp_collections, 'agreed': agreed})

    return render(request, 'user_page/index.html')


# 서비스 소개
def introduce(request):
	return render(request, 'user_page/introduce.html')


# 만든이들
def makers(request):
	return render(request, 'user_page/makers.html')


# 관리자 페이지
def a_main(request):
	return render(
		request,
		'admin_page/a_main.html'
	)


# stamp 추가
def add_stamp(request):
    if request.method == 'POST':
        event_name = request.POST['event_name']
        event_info = request.POST['event_info']
        event_start = request.POST['event_start']
        event_end = request.POST['event_end']
        image = request.FILES.get('after_image') if 'after_image' in request.FILES else None

        # 데이터 유효성 검사 및 저장
        if event_name and event_info and event_start and event_end and image:
            mystamp = stamp (
                event_name = event_name,
                event_info = event_info,
                event_start = event_start,
                event_end = event_end,
                image = image,
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


#이벤트 참여자 체크하는 페이지
def user_check(request):
    events = stamp.objects.all()
    students = student.objects.all()
    selected_event = None

    if request.method == 'POST':
        event_name = request.POST.get('event_name')
        major = request.POST.get('major')
        student_id = request.POST.get('student_id')

        if event_name:
           selected_event = stamp.objects.get(event_name=event_name)

        if major:
           students = students.filter(major=major)

        if student_id:
           students = students.filter(student_id__icontains=student_id)
        
        # 선택된 이벤트의 체크박스 확인 후 해당 학생의 student_collection을 업데이트
        event_check = request.POST.getlist('event_check')
        
        for stamp_collection_id in event_check:
            try:
                collection = stamp_collection.objects.get(id=stamp_collection_id)
                # is_collected 값 반전
                collection.is_collected = not collection.is_collected
                collection.save()
            except stamp_collection.DoesNotExist:
                pass
        
        if student_id:
            stamp_collections = stamp_collection.objects.filter(student__student_id__icontains=student_id, stamp=selected_event)
        else:
            # student_id가 None이면 stamp_collections를 빈 쿼리셋으로 초기화
            stamp_collections = stamp_collection.objects.none()

        context = {'students': students, 
                   'events': events, 
                   'initial_data': request.POST, 
                   'stamp_collections':stamp_collections,
                   }

        return render(request, 'manager_page/user_check.html', context)

    return render(request, 'manager_page/user_check.html', {'events': events, 'students': students})


# 스탬프 수정
@transaction.atomic
def edit_stamp(request, event_name):
    stamp_instance = get_object_or_404(stamp, event_name=event_name)
    
    if request.method == 'POST':
        # POST 데이터에서 가져와서 업데이트
        updated_data = {'event_name': request.POST.get('event_name'),
                        'event_info': request.POST.get('event_info'),
                        'event_start': request.POST.get('event_start'),
                        'event_end': request.POST.get('event_end')}
    
        # 이미지 업데이트 처리
        before_image = request.FILES.get('before_image')
        if before_image:
            # FileSystemStorage사용하여 이미지 저장
            fs = FileSystemStorage(location=os.path.join(settings.MEDIA_ROOT, 'before_images'))
            filename = fs.save(before_image.name, before_image)
            updated_data['before_image'] = filename
        
        after_image = request.FILES.get('after_image')
        if after_image:
            fs = FileSystemStorage(location=os.path.join(settings.MEDIA_ROOT, 'after_images'))
            filename = fs.save(after_image.name, after_image)
            updated_data['after_image'] = filename
            
        # DB에 직접 업뎃
        stamp.objects.filter(event_name=event_name).update(**updated_data)
        return redirect('stamp_list')  # 수정 후 도장 목록으로 리디렉션
        
    return render(request, 'manager_page/edit_stamp.html', {'stamp_instance': stamp_instance})


# stamp 삭제
def delete_stamp(request, event_name):
    delstamp = get_object_or_404(stamp, event_name=event_name)
    
    if request.method == 'POST':
        # Store the post pk before deleting the comment
        delstamp.delete()
        return redirect('stamp_list')
    return render(request, 'manager_page/stamp_list.html', {'delstamp': delstamp})


# X버튼 확인
# def edit_X_check(request):
# 	return render(request, 'manager_page/edit_X_check.html')


# # 저장하시겠습니까
# def edit_save_check(request):
# 	return render(request, 'manager_page/edit_save_check.html')