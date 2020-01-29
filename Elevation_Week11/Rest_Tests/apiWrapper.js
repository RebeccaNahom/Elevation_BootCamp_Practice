const ApiManager = require("./apiManager")
const apiManager = new ApiManager()


class RealWrapper{

 // Recieve type ("id"/"name"/"username"/"email") and value (number or string)
  // Return an object with a key of "status" (status code) and a key of "body" (array of objects with the filtered users)
  async getUsers(type, value){
    const response = await apiManager.getUsers(type, value)
    return response
  }
}

module.exports = RealWrapper