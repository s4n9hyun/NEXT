const todoForm = document.getElementById("todo-form");
const todoList = document.getElementById("todo-list");
const submitBtn = document.querySelector(".submitBtn");

document.addEventListener("DOMContentLoaded", loadTodos);

todoForm.addEventListener("submit", addTodo);

function loadTodos() {
    const todos = JSON.parse(localStorage.getItem("todos")) || [];
    todos.forEach(todo => displayTodo(todo));
}

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

function displayTodo(todo) {
    const li = document.createElement("li");
    li.innerHTML = `${todo.content} <button onclick="deleteTodo(${todo.id})">삭제</button>`;
    li.setAttribute("data-id", todo.id);
    todoList.appendChild(li);
}

function saveTodoInLocalStorage(todo) {
    const todos = JSON.parse(localStorage.getItem("todos")) || [];
    todos.push(todo);
    localStorage.setItem("todos", JSON.stringify(todos));
}

function deleteTodo(id) {
    const todos = JSON.parse(localStorage.getItem("todos")) || [];
    const updatedTodos = todos.filter(todo => todo.id !== id);
    localStorage.setItem("todos", JSON.stringify(updatedTodos));
    document.querySelector(`li[data-id='${id}']`).remove();
}
