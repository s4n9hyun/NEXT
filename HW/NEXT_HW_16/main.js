document.addEventListener("DOMContentLoaded", () => {
    const mainFlex = document.getElementById("mainFlex");
    const mainText = document.getElementById("mainText");
    const flexElements = [
        document.getElementById("flex1"),
        document.getElementById("flex2"),
        document.getElementById("flex3"),
        document.getElementById("flex4"),
    ];

    const colors = ["red", "pink", "green", "blue"];
    const texts = ["About Section", "Products Section", "Technology Section", "Downloads Section"];

    flexElements.forEach((flex, index) => {
        flex.addEventListener("click", () => {
            const selectedColor = colors[index];
            const selectedText = texts[index];
            mainFlex.style.backgroundColor = selectedColor;
            mainText.textContent = selectedText;
            flexElements.forEach((f) => (f.style.backgroundColor = "lightgray"));
            flex.style.backgroundColor = selectedColor;
        });
    });
});
