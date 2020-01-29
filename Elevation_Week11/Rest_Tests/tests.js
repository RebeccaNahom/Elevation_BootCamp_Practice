const RealWrapper = require("./apiWrapper")
const realWrapper = new RealWrapper()


const getUser = async function(type, value) {
    console.log(`Get user with type ${type} = ${value}`)
    let getUsers = await realWrapper.getUsers(type, value)
    console.log(`Status Code: ${getUsers.status}`)
    
    if(getUsers.status != '200'){
        console.error(`Error: Status Code: ${getUsers.status}, Body: ${getUsers.body}`)
    }
    else{
        console.table(getUsers.body)
    }
  }


getUser("id", "1")