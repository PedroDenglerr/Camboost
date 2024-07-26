function toggleMenu() {
    const menu = document.querySelector('.menu');
    menu.style.display = menu.style.display === 'block' ? 'none' : 'block';
  }
  
  // Cerrar el menú si se hace clic en cualquier parte de la página
  document.addEventListener('click', function (event) {
    const menu = document.querySelector('.menu');
    const menuIcon = document.querySelector('.menu-icon');
    
    if (!menu.contains(event.target) && event.target !== menuIcon) {
      menu.style.display = 'none';
    }
  });

  // ABOUT US SECTION

  document.addEventListener('DOMContentLoaded', function() {
    const links = document.querySelectorAll('.side-navbar ul li a');

    links.forEach(link => {
        link.addEventListener('click', function() {
            // Remove active class from all links
            links.forEach(l => l.classList.remove('active'));
            
            // Add active class to clicked link
            this.classList.add('active');
        });
    });
});


///

function toggleAnswer(element) {
  const answer = element.nextElementSibling;
  if (answer.style.display === "block") {
      answer.style.display = "none";
  } else {
      answer.style.display = "block";
  }
}