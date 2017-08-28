const WebSocket = require('ws');

const ws = new WebSocket('ws://localhost');

ws.on( 'open', function () {
    const payload = 'blah'
    ws.send( JSON.stringify( payload ) )
} )

ws.on( 'message', function ( data ) {
    console.log( data );
} )
