const express = require("express")
const bodyParser = require("body-parser")

const app = express()
const port = 8080

app.use(bodyParser.urlencoded({extended: true}))

app.use(function (req, res, next) {
	console.log(req.body)
	next()
})

app.post("/", (req, res) => {
	res.send("good")
})

app.get("/dump", (req, res) => {
	console.log(req)
})

app.post("/dump", (req, res) => {
	console.log(req)
})

app.listen(port, () => {
	console.log("Started Server.")
})
