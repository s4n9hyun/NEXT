// Select the relevant elements from the DOM
const todoForm = document.getElementById("todo-form");
const todoList = document.getElementById("todo-list");
const submitBtn = document.querySelector(".submitBtn");

// Load todos from local storage
document.addEventListener("DOMContentLoaded", loadTodos);

// Add event listener for form submission
todoForm.addEventListener("submit", addTodo);

// Function to load todos from local storage and display them
function loadTodos() {
    const todos = JSON.parse(localStorage.getItem("todos")) || [];
    todos.forEach(todo => displayTodo(todo));
}

// Function to add a new todo item
function addTodo(event) {
    event.preventDefault();
    const todoInput = document.getElementById("content");
    const todoText = todoInput.value.trim();

    if (todoText === "") {
        return;
    }

    const todo = {
        id: Date.now(),
        content: todoText
    };

    displayTodo(todo);
    saveTodoInLocalStorage(todo);
    todoInput.value = "";
}

// Function to display a todo item
function displayTodo(todo) {
    const li = document.createElement("li");
    li.innerHTML = `${todo.content} <button onclick="deleteTodo(${todo.id})">삭제</button>`;
    li.setAttribute("data-id", todo.id);
    todoList.appendChild(li);
}

// Function to save a todo item in local storage
function saveTodoInLocalStorage(todo) {
    const todos = JSON.parse(localStorage.getItem("todos")) || [];
    todos.push(todo);
    localStorage.setItem("todos", JSON.stringify(todos));
}

// Function to delete a todo item
function deleteTodo(id) {
    const todos = JSON.parse(localStorage.getItem("todos")) || [];
    const updatedTodos = todos.filter(todo => todo.id !== id);
    localStorage.setItem("todos", JSON.stringify(updatedTodos));
    document.querySelector(`li[data-id='${id}']`).remove();
}
