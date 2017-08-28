var socketioClient = require('socket.io-client')
var socket = socketioClient('ws://localhost')

socket.on('connect', function() {
	console.log('connect')
	// socket.send('blah') same as emit message
	socket.emit('message', 'blah3254')
})

socket.on('event', function(data) {
	console.log(`event`, data)
})

socket.on('disconnect', function() {
	console.log('disconnect')
})
