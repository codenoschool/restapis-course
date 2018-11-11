const express = require('express');
const request = require('request');
const bodyParser = require('body-parser');

const app = express();
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: false }));

const HOST = 'https://jsonplaceholder.typicode.com';

app.get('/', function(req, res) {
	res.send('Hello World!');
});

app.get('/users', (req, res) => {
	request.get(HOST + '/users', {json:true}, function(err, r) {
		if (err) {
			console.log(err);
		} else {
			res.send(r.body);
		}
	});
});

app.post('/users', (req, res) => {
	let user = {
		"name": req.body.name,
		"username": req.body.username
	};
	
	request.post(HOST + '/users', {form: user, json:true}, (err, r) => {
		if (err) {
			console.log(err);
		} else {
			res.send(r.body);
		}
	});
});

app.put('/users/:id', (req, res) => {
	let user = {
		"username": req.body.username
	};

	request.put(HOST + '/users/' + req.params.id, {form: user, json:true}, (err, r) => {
		if (err) {
			console.log(err);
		} else {
			res.send(r.body);
		}
	});
});

app.delete('/users/:id', (req, res) => {
	request.delete(HOST + '/users/' + req.params.id, {json:true}, (err, r) => {
		if (err) {
			console.log(err);
		} else {
			res.send(r.body);
		}
	});
});

app.listen(3000);
