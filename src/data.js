const fs = require("fs");

var dataHolder = {};

function addData(inputData) {
	id = inputData.PASSKEY;

	// Takes request body from http
	if (dataHolder[id] == undefined) {
		// If anemometer hasn't submitted data before
		dataHolder[id] = {
			id: id,
			unixTimes: [],
			temp: [],
			humidity: [],
			pressure: [],
			windDir: [],
			windSpeed: [],
			windGust: [],
			solarRad: [],
			batLevel: []
		};
	} 
	
	// Push all data into arrays
	dataHolder[id].unixTimes.push(new Date(inputData.dateutc).getTime())
	dataHolder[id].temp.push(FtoC(parseFloat(inputData.tempinf)));
	dataHolder[id].humidity.push(parseFloat(inputData.humidityin));
	dataHolder[id].pressure.push(parseFloat(inputData.baromrelin));
	dataHolder[id].windDir.push(parseFloat(inputData.winddir))
	dataHolder[id].windSpeed.push(parseFloat(inputData.windspeedmph));
	dataHolder[id].windGust.push(parseFloat(inputData.windgustmph));
	dataHolder[id].solarRad.push(parseFloat(inputData.solarradiation));
	dataHolder[id].batLevel.push(parseFloat(inputData.wh68batt));
}

function dumpToFile() {
	keys = Object.keys(dataHolder);
	for (key of keys) {
		createCSV(dataHolder[key]);
	}
}

function createCSV(anem) {
	keys = Object.keys(anem);
	keys.shift();
	outputStr = "";
	for (var i = 0; i < keys.length; i++) {
		if (i != 0) {
			outputStr += ",";
		}

		outputStr += keys[i];
	}
	outputStr += "\n";

	for (var i = 0; i < anem.unixTimes.length; i++) {
		for (var j = 0; j < keys.length; j++) {
			if (j != 0) {
				outputStr += ",";
			}

			outputStr += anem[keys[j]][i];
		}
		outputStr += "\n";
	}


	fs.writeFileSync(`./data/${anem.id}-${new Date().toLocaleDateString("SV-se")}-${new Date().toLocaleTimeString("SV-se").replaceAll(":", "-")}.csv`, outputStr);
	console.log(outputStr);
}

function FtoC(tempF) {
	return (tempF - 32.0) * 5.0/9.0;
}

function getDataHolder() {
	return dataHolder;
}

exports.addData = addData;
exports.getDataHolder = getDataHolder;
exports.dumpToFile = dumpToFile;
