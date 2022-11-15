const addBook = document.querySelector(".add-book")
const addContent = document.querySelector(".add-content")
const bookAuthor = addContent.querySelector("#text-author")
const bookTitle = addContent.querySelector("#text-title")
const actionBtn = addContent.querySelector("button")
const closeIcon = addContent.querySelector("header img")
const alertContainer = document.querySelector("[data-alert-container]")

const books = JSON.parse(localStorage.getItem("books"))
let curBookId

actionBtn.addEventListener("click", () => {
    if (bookAuthor.value === "Author" || bookTitle.value === "Title" || bookAuthor.value.length === 0 || bookTitle.value.length === 0) {
        showAlert("Empty rows")
    }
    else {
        let author = bookAuthor.value
        let title = bookTitle.value

        if (actionBtn.innerText === "Add") {
            books.push({author, title})
        }
        else {
            books[curBookId] = {author, title}
        }

        localStorage.setItem("books", JSON.stringify(books));

        document.querySelectorAll(".book").forEach(list => list.remove())
        fillGrid();
        closeIcon.click();
    }
});

addBook.addEventListener("click", () => {
    bookAuthor.value = "Author"
    bookTitle.value = "Title"
    actionBtn.innerText = "Add"
    addContent.style.display = "block"
});

bookAuthor.addEventListener("click", () => {
    if (bookAuthor.value === "Author") {
        bookAuthor.value = ""
    }
});

bookTitle.addEventListener("click", () => {
    if (bookTitle.value === "Title") {
        bookTitle.value = ""
    }
});

closeIcon.addEventListener("click", () => {
    bookAuthor.value = bookTitle.value = ""
    addContent.style.display = "none"
});

function deleteBook(bookId) {
    books.splice(bookId, 1)
    localStorage.setItem("books", JSON.stringify(books))
    document.querySelectorAll(".book").forEach(list => list.remove())

    fillGrid();
}

function editBook(bookId, author, title) {
    curBookId = bookId
    addBook.click()

    bookAuthor.value = author
    bookTitle.value = title
    actionBtn.innerText = "Edit"
}

function showAlert(message, duration = 5000) {
    const alert = document.createElement("div")
    alert.textContent = message
    alert.classList.add("alert")
    alertContainer.prepend(alert)

    setTimeout(() => {
        alert.classList.add("hide")
        alert.addEventListener("transitionend", () => {
            alert.remove()
        })
    }, duration)
}

function fillGrid() {
    books.forEach((book, id) => {
        let bookList = `<list class="book">
                            <img onclick="editBook(${id}, '${book.author}', '${book.title}')" src="./assets/edit-svgrepo-com.svg" alt="Edit Book" id="edit">
                            <img onclick="deleteBook(${id})" src="./assets/delete-svgrepo-com.svg" alt="Delete Book" id="delete">
                            <div class="details">
                                <p><b>Author: </b>${book.author}</p>
                                <p><b>Title: </b>${book.title}</p>
                            </div>
                        </list>`;

        addBook.insertAdjacentHTML("beforebegin", bookList)
    });
}

fillGrid()