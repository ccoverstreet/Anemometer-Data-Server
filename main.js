const express = require("express")
const bodyParser = require("body-parser")
const fs = require("fs");

const app = express()
const port = 8080

const dataTypes = require("./src/data.js");

app.use(bodyParser.urlencoded({extended: true}))

app.use(function (req, res, next) {
	console.log(req.body);
	next();
})

app.post("/", (req, res) => {
	res.send("good");
})

app.get("/dump", (req, res) => {
	console.log(req);
})

app.post("/dump", (req, res) => {
	console.log(req);
})

app.listen(port, () => {
	console.log("Started Anemometer Data Server.");
	console.log("Checking if \"data\" dir exists.");
	if (!fs.existsSync("./data")) {
		console.log("\"data\" dir not found. Creating dir.");
		fs.mkdirSync("./data", 0755);
	}
	console.log("Ready for data.");
})
