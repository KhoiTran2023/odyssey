//chatbot function
document.addEventListener("DOMContentLoaded", function() {
    // Get the chat log and message input elements
    var chatLog = document.getElementById("chat-body");
    var messageInput = document.getElementById("chatMessage");
    
    // Add an event listener to the message input element
    messageInput.addEventListener("keydown", function(event) {
        // Check if the user has pressed the enter key
        if (event.keyCode === 13) {
        // Get the user's message
        var message = messageInput.value;
        
        // Send the user's message to the server using an AJAX request
        var xhr = new XMLHttpRequest();
        xhr.open("POST", "/chatbot/", true);
        xhr.setRequestHeader("Content-Type", "application/json");
        xhr.onreadystatechange = function() {
            if (xhr.readyState === 4 && xhr.status === 200) {
            // Get the bot's response
            var response = JSON.parse(xhr.responseText).message;
            
            // Display the bot's response in the chat log
            chatLog.innerHTML += "<p><strong>You:</strong> " + message + "</p>";
            chatLog.innerHTML += "<p><strong>Bot:</strong> " + response + "</p>";
            
            // Clear the message input field
            messageInput.value = "";
            }
        };
        xhr.send(JSON.stringify({ 'message': message }));
        }
    });
    });


// Make the DIV element draggable:
dragElement(document.getElementById("chat-container"));

function dragElement(elmnt) {
  var pos1 = 0, pos2 = 0, pos3 = 0, pos4 = 0;
  if (document.getElementById("chat-header")) {
    // if present, the header is where you move the DIV from:
    document.getElementById("chat-header").onmousedown = dragMouseDown;
  } else {
    // otherwise, move the DIV from anywhere inside the DIV:
    elmnt.onmousedown = dragMouseDown;
  }

  function dragMouseDown(e) {
    e = e || window.event;
    e.preventDefault();
    // get the mouse cursor position at startup:
    pos3 = e.clientX;
    pos4 = e.clientY;
    document.onmouseup = closeDragElement;
    // call a function whenever the cursor moves:
    document.onmousemove = elementDrag;
  }

  function elementDrag(e) {
    e = e || window.event;
    e.preventDefault();
    // calculate the new cursor position:
    pos1 = pos3 - e.clientX;
    pos2 = pos4 - e.clientY;
    pos3 = e.clientX;
    pos4 = e.clientY;
    // set the element's new position:
    elmnt.style.top = (elmnt.offsetTop - pos2) + "px";
    elmnt.style.left = (elmnt.offsetLeft - pos1) + "px";
  }

  function closeDragElement() {
    // stop moving when mouse button is released:
    document.onmouseup = null;
    document.onmousemove = null;
  }
}