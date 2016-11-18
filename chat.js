// Open websocket
var ws = new WebSocket("ws://localhost:8000/");

// Close socket when window closes
$(window).on('beforeunload', function(){
   ws.close();
});

ws.onopen = function() {
   ws.send("test");
};

ws.onmessage = function (event)  { 
   var message_received = event.data;
   chat_add_message("Bot", message_received);
};

/* Chat Utility Functions */

// Add a message to the chat history
function chat_add_message(name, message) {
   chat_add("<b>"+name+"</b>: "+message+"<br />");
}
// Add a line to the chat history
function chat_add(html) {
   $("#chat_log").append(html);
   chat_scrolldown();
}
// Scrolls the chat history to the bottom
function chat_scrolldown() {
    $("#chat_log").animate({ scrollTop: $("#chat_log")[0].scrollHeight }, 500);
}

// If press ENTER, talk to chat and send message to server
$(function() {
   $('#chat_input').on('keypress', function(event) {
      if (event.which === 13 && $(this).val() != ""){
         var message = $(this).val();
         $(this).val("");
         chat_add_message("User", message);
         ws.send(message);
      }
   });
});