// Lab 04: To Do List

let input = document.querySelector('#userInput')
let button = document.querySelector('#add')
let list = document.querySelector('#list')
let completed = document.querySelector('#completed')



let listName = ["Task List", "Wish List", "Grocery List", "Shopping List", "Reading Journal", "Gift Ideas", "Shopping List", "Errands", "Expenses"]
// This line changes the name of your list
function changeTitle(){
    document.getElementById("changeHeader").innerText = listName[Math.floor(Math.random() * listName.length)]
}

button.addEventListener('click', () => {
    let userInput = document.createElement('div')
    userInput.innerText = input.value

    list.appendChild(userInput)
    input.value = ""
})








