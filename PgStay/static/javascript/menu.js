document.addEventListener('DOMContentLoaded', function() {
 var menuButton = document.querySelector('#menu-button');
 var menuImage = document.querySelector('#menu-image');

 menuButton.addEventListener('click', function() {
    menuImage.src = '{% static 'images/img_2.png' %}';
 });
});