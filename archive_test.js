const fs = require("fs");
const zipdir = require("zip-dir");

var bufferProm = zipdir(__dirname + "/data");

(async function() {

	buffer = await bufferProm;
	fs.writeFileSync("./alldata.zip", buffer);
})();

