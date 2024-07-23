// Create a client instance
var serverUrl   = window.location.host; // i.e. "great-server.cloudmqtt.com"
    var serverPort  = 9001; // cloudmqtt only accepts WSS sockets on this port. Others will use 9001, 8883 or others
    var clientId    = "wsbrowser_"+new Date().getUTCMilliseconds(); // make client name unique
client = new Paho.MQTT.Client(window.location.host, Number(9001), "/wss");

// set callback handlers
client.onConnectionLost = onConnectionLost;
client.onMessageArrived = onMessageArrived;

// connect the client
client.connect({onSuccess:onConnect});


// called when the client connects
function onConnect() {
  // Once a connection has been made, make a subscription and send a message.
  console.log("onConnect");
  spectrum.toggleAutoScale();
  client.subscribe("cmd/pluto/+/rx/webfft/+");
  
  
  //message = new Paho.MQTT.Message("Hello");
  //message.destinationName = "World";
  //client.send(message);
}

// called when the client loses its connection
function onConnectionLost(responseObject) {
  if (responseObject.errorCode !== 0) {
    console.log("onConnectionLost:"+responseObject.errorMessage);
  }
  //client.connect({onSuccess:onConnect});
}

// called when a message arrives
function onMessageArrived(message) {
    let topic= message.destinationName;
  console.log("onMessageArrived:"+message.payloadString+message.destinationName);
  
  if(topic.includes("frequency"))
  {
  spectrum.setCenterHz((message.payloadString/1000).toFixed(1)*1000);
  
  }
  if(topic.includes("span"))
  {
  
  spectrum.setSpanHz((message.payloadString));
  }

  if(topic.includes("average"))
  {
    spectrum.setAveraging((message.payloadString));
  }

  if(topic.includes("autoscale"))
  {
    spectrum.toggleAutoScale();
  }

  if(topic.includes("rangemin"))
  {
    spectrum.min_db=message.payloadString;
    spectrum.updateAxes();
  }  

  if(topic.includes("rangemax"))
  {
    spectrum.max_db=message.payloadString;
    spectrum.updateAxes();
  }  
}