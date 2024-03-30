function checkCurrentPage(url) {
    return window.location.href !== url;
}
function goToArticles() {
    if (checkCurrentPage("/articles/")) {
        window.location.href = "/articles/";
    }
}
function goToCareer() {
    if (checkCurrentPage("/career/")) {
        window.location.href = "/career/";
    }
}
function goToSkills() {
    if (checkCurrentPage("/skills/")) {
        window.location.href = "/skills/";
    }
}
function goToProjects() {
    if (checkCurrentPage("/projects/")) {
        window.location.href = "/projects/";
    }
}

document.addEventListener("DOMContentLoaded", function() {
    var elementsTopRight = document.querySelectorAll('.rotate-t-r');
    elementsTopRight.forEach(function(element) {
        var rotation = getRandomRotation(35,70);
        element.style.transform = 'rotate(' + rotation + 'deg)';
    });
    var elementsTopLeft = document.querySelectorAll('.rotate-t-l');
    elementsTopLeft.forEach(function(element) {
        var rotation = getRandomRotation(135,180);
        element.style.transform = 'rotate(' + rotation + 'deg)';
    });
    var elementsBottomRight = document.querySelectorAll('.rotate-b-r');
    elementsBottomRight.forEach(function(element) {
      var rotation = getRandomRotation(135,180);
      element.style.transform = 'rotate(' + rotation + 'deg)';
    });
    var elementsBottomLeft = document.querySelectorAll('.rotate-b-l');
    elementsBottomLeft.forEach(function(element) {
      var rotation = getRandomRotation(35,70);
      element.style.transform = 'rotate(' + rotation + 'deg)';
    });
});
  
function getRandomRotation(min,max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
}


document.addEventListener('DOMContentLoaded', function() {
  // Функция для проверки ширины экрана и отображения соответствующего содержимого
  function toggleContent() {
    var screenWidth = window.outerWidth;
    var desktopContent = document.querySelector('.desktop');
    var mobileContent = document.querySelector('.mobile');
    
    if (screenWidth >= 769) {
      desktopContent.style.display = 'block';
      mobileContent.style.display = 'none';
    } else {
      desktopContent.style.display = 'none';
      mobileContent.style.display = 'block';
      mobileContent.style.width = 'fit-content';
      mobileContent.style.height = 'auto';
    }
  }
  
  // Вызов функции при загрузке страницы и изменении размера окна
  toggleContent();
  window.addEventListener('resize', toggleContent);
});

window.onload = function() {
    const bottomBar = document.getElementById("bottomBar");
    const itemWidth = bottomBar.querySelector(".item").offsetWidth;
    const containerWidth = bottomBar.offsetWidth;

    const itemsPerRow = Math.floor(containerWidth / itemWidth);
    const itemsToDuplicate = itemsPerRow - (bottomBar.children.length % itemsPerRow);

    for (let i = 0; i < itemsToDuplicate; i++) {
        const itemClone = bottomBar.querySelector(".item").cloneNode(true);
        bottomBar.appendChild(itemClone);
    }
};