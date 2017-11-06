var express  = require('express');
var expressHbs = require('express-handlebars');
var bodyParser = require('body-parser');
var axios = require('axios');
var rp = require('request-promise');


app = express();

app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());
app.use(bodyParser());



app.engine('.hbs', expressHbs({extname: '.hbs'}));
app.set('view engine', '.hbs');

app.get('/',(req,res) => {
	res.render('main.hbs');
});

app.post('/result',(req,res) => {
	console.log(JSON.stringify(req.body));

	var options = {
    method: 'POST',
    uri: 'http://127.0.0.1:5000/',
    body: req.body,
    json: true // Automatically stringifies the body to JSON
};
console.log('body: ',options.body);

rp(options)
		.then((response) => {
			console.log('response: ',response);
			res.render('result.hbs',{data:response});
		})
    .catch(function (err) {
        // POST failed...
    });
});

app.listen(3000, () => {
	console.log('Server started');
});