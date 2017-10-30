var express  = require('express');
var expressHbs = require('express-handlebars');
var bodyParser = require('body-parser');
var axios = require('axios');



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

	axios.post('localhost:8000/',{data:JSON.stringify(req.body)})
		.then((response) => {
			res.render('result.hbs',{data:response});
		});
});

app.listen(3000, () => {
	console.log('Server started');
});