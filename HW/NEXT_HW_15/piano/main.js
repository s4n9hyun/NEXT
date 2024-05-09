play = (e) => {
    const audio = document.querySelector(`audio[data-key="${e.keyCode}"]`);
    const key = document.querySelector(`li[data-key="${e.keyCode}"]`);
    if (audio) {
        audio.currentTime = 0; // Rewind to the start
        audio.play();
        if (key) {
            key.classList.add("play");
        }
    }
};

pause = (e) => {
    const audio = document.querySelector(`audio[data-key="${e.keyCode}"]`);
    const key = document.querySelector(`li[data-key="${e.keyCode}"]`);
    if (audio) {
        audio.pause();
        if (key) {
            key.classList.remove("play");
        }
    }
};

window.addEventListener("keydown", play);
window.addEventListener("keyup", pause);
