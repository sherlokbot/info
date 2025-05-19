"use strict";

// Инициализация анимации при скролле
document.querySelectorAll(".object-wrapper").forEach(wrapper => {
    wrapper.querySelectorAll(".object").forEach(element => {
        element.classList.remove("object-animation");
        new IntersectionObserver(entries => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    element.classList.add("object-animation");
                } else {
                    element.classList.remove("object-animation");
                }
            });
        }).observe(element);
    });
});
