const checkbox = document.getElementById('check')

checkbox.addEventListener("change", () => {
    document.body.classList.toggle("dark-mode");
    localStorage.setItem("darkMode", checkbox.checked);
});

window.addEventListener("load", () => {
    if (localStorage.getItem("darkMode") === "true") {
        document.body.classList.add("dark-mode");
        checkbox.checked = true;
    }
});
