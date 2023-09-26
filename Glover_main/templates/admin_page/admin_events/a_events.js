const template = `
    <div class="stamp1-set">
        <button class="stamp1">
            <img src="../../img/stamp1.png" alt="빈 스탬프 이미지">
        </button>
        <button class="stamp2">
            <img src="../../img/stamp1.png" alt="빈 스탬프 이미지">
        </button>
        <button class="stamp3">
            <img src="../../img/stamp1.png" alt="빈 스탬프 이미지">
        </button>
    </div>
    <div class="stamp2-set">
        <button class="stamp4">
            <img src="../../img/stamp1.png" alt="빈 스탬프 이미지">
        </button>
        <button class="stamp5">
            <img src="../../img/stamp1.png" alt="빈 스탬프 이미지">
        </button>
        <button class="stamp6">
            <img src="../../img/stamp1.png" alt="빈 스탬프 이미지">
        </button>
    </div>
`;
$(".stampset").append(template);

const open=document.querySelector(".stamp1");
const modal=document.querySelector(".modal-cont");
const close=document.querySelector(".bi-x");

function init(){
    open.addEventListener("click",function(){
        document.querySelector(".modal-bg").classList.remove("hidden"); // 어두운 배경도 표시
        modal.classList.remove("hidden");
    });
    close.addEventListener("click",function(){
        document.querySelector(".modal-bg").classList.add("hidden"); // 어두운 배경도 숨김
        modal.classList.add("hidden");
    });
}

init();

