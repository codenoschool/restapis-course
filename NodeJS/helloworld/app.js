var express = require('express');

var app = express();

app.get('/', function(req, res) {
	res.send('Hello World!');
});

app.listen(3000, function() {
	console.log('Running on http://127.0.0.1:3000/ (Press CTRL+C to quit)');
});
