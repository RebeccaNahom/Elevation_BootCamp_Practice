// // example:
// $.get("https://www.googleapis.com/books/v1/volumes?q=intitle:Name+of+the+Wind", function(result){
//     console.log(result.items[0].volumeInfo.description)
// })

// $.get("https://jsonplaceholder.typicode.com/users", function(users){
//     console.log(users[9].company.catchPhrase);

// })

// // exercise 1+2:
// function fetch(queryType, queryValue) {
//     if (queryType == "title") {
//         $.get(`https://www.googleapis.com/books/v1/volumes?q=intitle:${queryValue}`, function (result) {
//             console.log(result.items[0].volumeInfo);
//         })
//     }
//     if (queryType == "isbn") {
//         $.get(`https://www.googleapis.com/books/v1/volumes?q=isbn:${queryValue}`, function (result) {
//             console.log(result.items[0].volumeInfo);
//         })
//     }
// }

// // fetch(9782806269171)
// // fetch(1440633908)
// // fetch(9781945048470)
// // fetch(9780307417138)

// // fetch("isbn", 9789814561778)
// // fetch("title", "How to Win Friends and Influence People")

// // exercise 3:
// function fetch() {
//     $.get(`https://www.googleapis.com/books/v1/volumes?q=intitle:harry+potter`, function (result) {
//         console.log(result.items.length)
//         result.items.forEach(function(item){
//             console.log({"title:": item.volumeInfo.title,
//              "author:": item.volumeInfo.authors,
//              "ISBN:": item.volumeInfo.industryIdentifiers})
//         });
//     })
// }
// fetch()

