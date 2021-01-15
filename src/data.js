
var dataHolder = {};

function addData(inputData) {
	// Takes request body from http
	if (dataHolder[inputData.PASSKEY] == undefined) {
		// If anemometer hasn't submitted data before
		dataHolder[inputData.PASSKEY] = {
			unixTimes: [],
			temp: [],
			windDir: [],
			windSpeed: [],
			windGust: [],
			lastTime: 0
		};
	} else {
		dataHolder[inputData.PASSKEY].unixTimes.push(new Date(inputData.datutc).getTime())
		dataHolder[inputData.PASSKEY].temp.push(FtoC(inputData.tempinf));
	}
}

function FtoC(tempF) {
	floatTemp = parseFloat(tempF)
	return (floatTemp - 32.0) * 5.0/9.0;
}
