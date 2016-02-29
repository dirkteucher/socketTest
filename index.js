var app = require('express')();
var http = require('http').Server(app);
var io = require('socket.io')(http);
var fs = require('fs');//require the file sytem to check for json file changes
var jf = require('jsonfile'); //jsonfile module

app.get('/', function(req, res){
  res.sendFile(__dirname + '/index.html');
});

io.on('connection', function(socket){
  socket.on('chat message', function(msg){

		var fileName = './tiltDetection.json';
		var file = require(fileName);
	fs.watch("./tiltDetection.json", function(event, fileName) {

		console.log("watching");
		
		 jf.readFile('./tiltDetection.json', function(err, data) { //if change detected read the sports.json 
		
        var data = data; //store in a var
		io.emit('chat message', data);
		 });		
	});
	
  });
});



http.listen(8080, function(){
  console.log('listening on *:8080');
});