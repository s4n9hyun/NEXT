const username = document.querySelector(".username");
const usernameWrapper = document.querySelector(".usernameWrapper");
const header = document.querySelector("#header");

function checkUsername() {
    const checkName = window.localStorage.getItem("username");
    if (checkName) {
        usernameWrapper.style.display = "none";
        header.innerHTML = `<h1>${window.localStorage.getItem("username")}'s Todo List</h1><button type="button" onclick="resetUsername()">초기화</button>`;
    } else {
        usernameWrapper.style.display = "flex";
        header.innerHTML = "";
    }
}

// Execute checkUsername function
checkUsername();

/* Function to set the user's name based on input value */
// Read value from input
// Save it to local storage with the key 'username'
function setUsername() {
    const name = username.value;
    window.localStorage.setItem("username", name);
    username.value = "";
    checkUsername();
}

function resetUsername() {
    // Remove the username from local storage
    window.localStorage.removeItem("username");
    
    // Reset the display to show the username input form
    usernameWrapper.style.display = "flex";
    header.innerHTML = "";
}