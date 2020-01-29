const request = require('request-promise');

class ApiManager {
  constructor() {}

  // Recieve type ("id"/"name"/"username"/"email") and value (number or string)
  // Return an object with a key of "status" (status code) and a key of "body" (array of objects with the filtered users)
  async getUsers(type, value) {
    let response = {};
    await request.get('http://localhost:3000/users', { form: { type, value } }, function(
      err,
      http,
      body
    ) {
      response.body = body.length == 2 ? 'Error: The user was not found' : JSON.parse(body);
      response.status = http.statusCode;
    });
    return response;
  }
}

module.exports = ApiManager