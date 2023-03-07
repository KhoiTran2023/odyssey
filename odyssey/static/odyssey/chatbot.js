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