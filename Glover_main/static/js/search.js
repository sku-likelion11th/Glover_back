// const template = `
//     <div class="stamp1-set">
//         <button class="stamp1">
//             <img src="../../img/stamp1.png" alt="빈 스탬프 이미지">
//         </button>
//         <button class="stamp2">
//             <img src="../../img/stamp1.png" alt="빈 스탬프 이미지">
//         </button>
//         <button class="stamp3">
//             <img src="../../img/stamp1.png" alt="빈 스탬프 이미지">
//         </button>
//     </div>
//     <div class="stamp2-set">
//         <button class="stamp4">
//             <img src="../../img/stamp1.png" alt="빈 스탬프 이미지">
//         </button>
//         <button class="stamp5">
//             <img src="../../img/stamp1.png" alt="빈 스탬프 이미지">
//         </button>
//         <button class="stamp6">
//             <img src="../../img/stamp1.png" alt="빈 스탬프 이미지">
//         </button>
//     </div>
// `;
// $(".stampset").append(template);

// const open=document.querySelector(".stamp1");
// const modal=document.querySelector(".modal-cont");
// const close=document.querySelector(".bi-x");

// function init(){
//     open.addEventListener("click",function(){
//         document.querySelector(".modal-bg").classList.remove("hidden"); // 어두운 배경도 표시
//         modal.classList.remove("hidden");
//     });
//     close.addEventListener("click",function(){
//         document.querySelector(".modal-bg").classList.add("hidden"); // 어두운 배경도 숨김
//         modal.classList.add("hidden");
//     });
// }

// init();


const stampButtons = document.querySelectorAll(".stamp1");
const modal = document.querySelector(".modal-cont");
const modalName = document.querySelector(".name p");
const modalInfo = document.querySelector(".detail p");
const modalStart = document.querySelector(".start p");
const modalEnd = document.querySelector(".finish p");
const modalClose = document.querySelector(".bi-x");

function formatDate(dateString) {
    const date = new Date(dateString);
    const year = date.getFullYear().toString().slice(-2); // Get the last two digits of the year
    const month = String(date.getMonth() + 1).padStart(2, '0'); // Ensure two-digit month
    const day = String(date.getDate()).padStart(2, '0'); // Ensure two-digit day
    return `${year}-${month}-${day}`;
}

function init() {
    stampButtons.forEach((button) => {
        button.addEventListener("click", function () {
            const name = button.getAttribute("data-name");
            const info = button.getAttribute("data-info");
            const startDate = formatDate(button.getAttribute("data-start"));
            const endDate = formatDate(button.getAttribute("data-end"));

            modalName.textContent = name;
            modalInfo.textContent = info;
            modalStart.textContent = startDate;
            modalEnd.textContent = endDate;

            document.querySelector(".modal-bg").classList.remove("hidden");
            modal.classList.remove("hidden");
        });
    });

    modalClose.addEventListener("click", function () {
        document.querySelector(".modal-bg").classList.add("hidden");
        modal.classList.add("hidden");
    });
}

init();

