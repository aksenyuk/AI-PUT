const addBook = document.querySelector(".add-book")
const addContent = document.querySelector(".add-content")
const closeIcon = addContent.querySelector("header img")
const bookAuthor = addContent.querySelector("#text-author")
const bookTitle = addContent.querySelector("#text-title")
const addBtn = addContent.querySelector("button")
const alertContainer = document.querySelector("[data-alert-container]")



addBtn.addEventListener("click", () => {
    let addTxt = document.getElementById("addTxt");
    let notes = localStorage.getItem("notes");
    notesObj = JSON.parse(notes);
    notesObj.push(addTxt.value);
    localStorage.setItem("notes", JSON.stringify(notesObj));
    addTxt.value = "";
});



function showBooks() {
    // document.querySelectorAll(".book");

    const books = document.createElement('div')
    books.forEach((book, id) => {
        let bookList = `<div class="book">
                            <img onclick="editBook(${id}, '${book.author}', '${book.title}')" src="./assets/edit-svgrepo-com.svg" alt="Edit Book" id="edit">
                            <img onclick="deleteBook(${id})" src="./assets/delete-svgrepo-com.svg" alt="Delete Book" id="delete">
                            <div class="details">
                                <p><b>Author: </b>${book.author}</p>
                                <p><b>Title: </b>${book.title}</p>
                            </div>
                        </div>`;

        addBook.insertAdjacentHTML("afterend", bookList);
    });
}

showBooks();