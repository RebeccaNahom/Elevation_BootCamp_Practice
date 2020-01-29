const express = require('express')
const users = require('./usersJson')
const router = express.Router()

const usersDB = []
users.forEach(p => usersDB.push({id: p.id, name: p.name, username: p.username, email: p.email}))

// GET
router.get('/users', function (req, res) {
  let value = req.body.value;
  let type = req.body.type;

  if (type === "id") {
    value = Number(value)
  }

  let result = usersDB.filter(p => p[type] === value)
  res.send(result)
})

module.exports = router