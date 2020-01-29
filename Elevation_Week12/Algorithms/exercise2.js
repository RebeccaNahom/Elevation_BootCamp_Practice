let printBackwardsStars = function(num){
    let startPoint = "******"
    if (num >= 1){
      for (let i = 1; i <= num; i++){
        console.log('str: ' + startPoint);
        // startPoint = startPoint-"*"
      }
    } 
  }
  
  printBackwardsStars(4)