const eliminarActive = () => {
    let current = document.getElementsByClassName("active");
    current[0].className = current[0].className.replace(" active", "");
}

const btns = $(".nav-link");
switch (window.location.pathname) {
    case "/":
        eliminarActive();
        btns[0].classList.add("active");
        break;
    case "/persona/":
        eliminarActive();
        btns[1].classList.add("active");
        break;
    case "/tipodocumento/":
        eliminarActive();
        btns[2].classList.add("active");
        break;
    case "/ciudad/":
        eliminarActive();
        btns[3].classList.add("active");
        break;
}
