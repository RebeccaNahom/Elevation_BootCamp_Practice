// let fib = [0, 1]
// function fibSeries(n) {
//     for (let i = 2; i < n + 1; i++) {
//         fib.push(fib[i - 2] + fib[i - 1])
//     }
//     console.log(fib);
// }

// fibSeries(5)

let str1 = ["a", "d", "c", "d"]
let str2 = ["d", "a", "c", "d"]

function isAnagram(str1, str2){
    if(str1.length == str2.length){
        let count = 0
        for(let i of str1){
            for(let j in str2){
                if(i == j){
                    count ++
                    console.log();
                    
                }
            }
        }

    }
}