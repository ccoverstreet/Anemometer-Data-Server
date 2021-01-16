const express = require("express")
const bodyParser = require("body-parser")
const fs = require("fs");

const app = express()
const port = 8080

const dataHandler = require("./src/data.js");

app.use(bodyParser.urlencoded({extended: true}))

app.use(function (req, res, next) {
	next();
})

app.get("/", (req, res) => {
	res.send(JSON.stringify(dataHandler.getDataHolder()));
})

app.post("/dump", (req, res) => {
	console.log(req.body);
	dataHandler.addData(req.body);
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

