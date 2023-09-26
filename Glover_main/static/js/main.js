// submit 버튼을 누르면 창이 새로고침 돼서 모달창이 나타나지 않음 
// 이를 해결하기 위해(디자인 작성을 위해) 임시로 js를 작성함 -> 추후에 다 수정해야됨

// 폼과 모달 요소 가져오기
var form = document.getElementById("login");
var modal = document.getElementById("modal");

// 폼 제출 이벤트 핸들러 등록
form.addEventListener("submit", function(event) {
    event.preventDefault(); // 폼 제출 방지
    var agreeButton = document.getElementById("agree_Btn");

    // 모달 창 열기
    // modal.style.display = "block";
});


// 동의 버튼 누를 때
document.getElementById('agree-Btn').addEventListener('agree', function() {
    // AJAX 요청을 사용하여 서버에 동의 업데이트 요청을 보냅니다.

    // Vanilla JavaScript를 사용하는 경우:
    var student_id = 1;  // 학생의 ID를 여기에 설정
    var xhr = new XMLHttpRequest();
    xhr.open('POST', '/update-consent/', true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.onreadystatechange = function() {
        if (xhr.readyState === 4 && xhr.status === 200) {
            var response = JSON.parse(xhr.responseText);
            if (response.success) {
                // 동의 업데이트가 성공한 경우
                // 모달을 닫거나 다음 단계로 이동합니다.
                document.getElementById('consent-modal').style.display = 'none';
            }
        }
    };
    xhr.send(JSON.stringify({ student_id: student_id }));
});


// 첫 번째 모달창 닫기 버튼 
var closeBtn = document.querySelector(".close");
closeBtn.addEventListener("click", function() {
    modal.style.display = "none"; // 모달 닫기
});




// 첫 번째 모달창에서 두 번째 모달창으로 넘어가는 코드
var agreeButton = document.getElementById("agree_Btn");
var secondModal = document.getElementById("sec_modal");
var closeButton = document.getElementById("closeButton");

// agreeButton.addEventListener("click", function() {


    // 첫 번째 모달에 블러 효과를 추가하기 위해 클래스를 추가
    // modal.classList.add("blur-effect");

    // 두 번째 모달을 표시
    // secondModal.style.display = "block";

    // 두 번째 모달에 포커스를 주어 해당 모달에만 집중할 수 있도록 함
    // secondModal.focus();
// });

// closeButton.addEventListener("click", function() {
//     // 두 번째 모달을 숨김
//     secondModal.style.display = "none";
//     // 블러 효과를 제거하기 위해 클래스를 제거
//     modal.classList.remove("blur-effect");

//     // 첫 번째 모달을 다시 표시
//     document.getElementById("modal").style.display = "block";

//     // 첫 번째 모달에 포커스를 주어 해당 모달에만 집중할 수 있도록 함
//     document.getElementById("modal").focus();
// });

// 두 번째 모달창 코드