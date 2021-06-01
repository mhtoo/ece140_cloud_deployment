function linkHector(){
   window.location.href = "http://165.232.152.55/";
}

function linkAdib(){
   window.location.href = "http://161.35.232.250/";
}

function linkTanvir(){
   window.location.href = "http://128.199.10.10/";
}

function dropFunction() {
  document.getElementById("theDropdown").classList.toggle("show");
}

window.onclick = function(event) {
  if (!event.target.matches('.dropbtn')) {
    var dropdowns = document.getElementsByClassName("dropdown-content");
    var i;
    for (i = 0; i < dropdowns.length; i++) {
      var openDropdown = dropdowns[i];
      if (openDropdown.classList.contains('show')) {
        openDropdown.classList.remove('show');
      }
    }
  }
}