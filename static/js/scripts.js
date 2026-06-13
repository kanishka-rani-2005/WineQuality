document.addEventListener("DOMContentLoaded", () => {

    const inputs = document.querySelectorAll(".input-text");

    inputs.forEach(input => {

        input.addEventListener("input", () => {

            let value = input.value;

            value = value.replace(/[^0-9.]/g, "");

            const parts = value.split(".");

            if(parts.length > 2){
                value = parts[0] + "." + parts[1];
            }

            input.value = value;
        });

    });

    const form = document.querySelector(".form-detail");

    const btn = document.querySelector(".register");

    if(form){

        form.addEventListener("submit", () => {

            btn.innerHTML = "Predicting...";

            btn.disabled = true;
        });
    }

    const cards = document.querySelectorAll(
        ".glass-card,.hero,.result-card"
    );

    const observer = new IntersectionObserver(
        entries => {

            entries.forEach(entry => {

                if(entry.isIntersecting){

                    entry.target.style.opacity = "1";

                    entry.target.style.transform =
                        "translateY(0)";
                }
            });
        },
        {
            threshold:0.15
        }
    );

    cards.forEach(card => {

        card.style.opacity = "0";

        card.style.transform =
            "translateY(50px)";

        card.style.transition =
            "all .8s ease";

        observer.observe(card);
    });

});