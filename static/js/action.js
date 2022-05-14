var select = document.getElementById("select_month");
var input = document.querySelector("input");

select.addEventListener("change", function(){
   input.value = this.value;
});