// 로그아웃 클릭시 a태그 기능중지
// 폼 전송
document.querySelector("#logout").addEventListener("click", () => {
  document.querySelector("form").submit();
});
