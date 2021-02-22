// main.js: Entrypoint for data server
// Cale Overstreet
// 2020/1/16
// Sets up dumping schedule and routes

const express = require("express")
const bodyParser = require("body-parser")
const fs = require("fs");
const zipdir = require("zip-dir");
const nodeSchedule = require("node-schedule");

const app = express()
const port = 8080

const dataHandler = require("./src/data.js");

var dump = nodeSchedule.scheduleJob("0 * * * *", dataHandler.dumpToFile);

app.use(bodyParser.urlencoded({extended: true}))

app.use(function (req, res, next) {
	console.log(`[${new Date().toLocaleString("SV-se")}]: ${req.originalUrl}`)
	next();
})

app.get("/", (req, res) => {
	res.sendFile(__dirname + "/index.html");
})

app.post("/currentData", (req, res) => {
	res.send(JSON.stringify(dataHandler.getDataHolder(), null, 4));
})

app.get("/zipData", async (req, res) => {
	buffer = await zipdir(__dirname + "/data");
	fs.writeFileSync(__dirname + "/alldata.zip", buffer);

	res.sendFile(__dirname + "/alldata.zip");
});

app.get("/manualDump", (req, res) => {
	dataHandler.dumpToFile();
	res.send("Manually dumped data");
}) 

app.post("/dump", (req, res) => {
	console.log(req.body);
	dataHandler.addData(req.body);
})

app.listen(port, () => {
	console.log("Starting Anemometer Data Server...");
	console.log("Checking if \"data\" dir exists...");
	if (!fs.existsSync("./data")) {
		console.log("\"data\" dir not found. Creating dir...");
		fs.mkdirSync("./data", 0755);
	}
	console.log("Ready for data.");
})

