const toggleButton = document.getElementsByClassName("toggle-button")[0];
const navbarLinks = document.getElementsByClassName("navbar-links")[0];
const navbar = document.getElementById("navbar");

toggleButton.addEventListener("click", () => {
  navbarLinks.classList.toggle("active");
  navbar.classList.toggle("bg_image");
});
