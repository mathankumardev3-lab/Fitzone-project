document.addEventListener("DOMContentLoaded", () => {
    const nav = document.querySelector(".navbar");
    const navLinks = document.querySelectorAll(".navbar .nav-link");
    const collapse = document.querySelector(".navbar-collapse");

    window.addEventListener("scroll", () => {
        if (window.scrollY > 40) {
            nav.classList.add("shadow");
        } else {
            nav.classList.remove("shadow");
        }
    });

    navLinks.forEach(link => {
        link.addEventListener("click", () => {
            if (collapse.classList.contains("show")) {
                bootstrap.Collapse.getOrCreateInstance(collapse).hide();
            }
        });
    });

    document.querySelectorAll(".alert").forEach(alert => {
        setTimeout(() => {
            const instance = bootstrap.Alert.getOrCreateInstance(alert);
            instance.close();
        }, 5000);
    });
});
