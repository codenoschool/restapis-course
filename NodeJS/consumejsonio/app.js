const express = require('express');
const request = require('request');
const app = express();

const API_KEY = process.env.API_KEY;

app.get('/', (req, res) => {
	res.send('Hello World!');
});

app.get('/bin/:id', (req, res) => {
	let options = {
		url: 'https://api.jsonbin.io/b/' + req.params.id,
		method: 'GET',
		json: true,
		headers: {
			'secret-key': API_KEY
		}
	};

	request(options, function(err, r) {
		res.send(r.body);
	});
});

app.delete('/bin/:id', (req, res) => {
	let options = {
		url: 'https://api.jsonbin.io/b/' + req.params.id,
		method: 'DELETE',
		json: true,
		headers: {
			'secret-key': API_KEY
		}
	};

	request(options, function(err, r) {
		res.send(r.body);
	});
});

app.listen(3000);
