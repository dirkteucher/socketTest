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
	  
	  //Notify client it has connected to the server
	  io.emit('chat message2', "Connected");
	  
	  function notifyMovementDetected(parsedJSON){
		  io.emit('bikeMoved', parsedJSON);
	  }
	  
	console.log(msg);
		var fileName = './tiltDetection.json';
		var file = require(fileName);
		fs.watch("./tiltDetection.json", function(event, fileName) {

			
				var parsedJSON = require('./tiltDetection.json');
				notifyMovementDetected(parsedJSON);			
			
			//fs.readFile('./tiltDetection.json', 'utf8', function(err, data) { //if change detected 
			//	console.log(data);
			//});
	});
  });
});


http.listen(8080, function(){
  console.log('listening on *:8080');
});