const express = require('express')
const bodyParser = require('body-parser')

const app = express()
app.use(bodyParser.json())
app.use(bodyParser.urlencoded({ extended: false }))

app.get('/', function(req, res){
    res.send("Hello, world.")
})

app.get('/potatoe', function(req, res){
    res.send("Here is a potato")
})

app.get('/test/:data', function (req, res) {
    const data = req.params.data
    res.send(`Thanks for the get. I got your ${data}, here's a potato.`)
})

app.post('/test', function (req, res) {
    console.log(req.body)
    res.send("Thanks for the post, here's a potatoe.")
})

app.post('/testData', function (req, res) {
    console.log(req.body)
    res.end()
})

const port = 3000
app.listen(port, function () {
    console.log(`Server running on ${port}`)
})