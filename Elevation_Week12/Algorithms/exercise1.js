let printStars = function(num){
  let numOfLines = "*"
  if (num >= 1){
    for (let i = 1; i <= num; i++){
      console.log(numOfLines);
      numOfLines += "*"
    }
  } 
}

printStars(10)