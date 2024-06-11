function askJarvis() {
    var userInput = $('#user-input').val();
    $('#chat-log').append('<div>You: ' + userInput + '</div>');
    $('#user-input').val('');

    $.ajax({
        url: '/ask',
        method: 'POST',
        contentType: 'application/json',
        data: JSON.stringify({ question: userInput }),
        success: function(response) {
            $('#chat-log').append('<div>Jarvis: ' + response.answer + '</div>');
        }
    });
}

function startRecording() {
    if (!('webkitSpeechRecognition' in window)) {
        alert('Sorry, your browser doesn\'t support speech recognition.');
        return;
    }

    var recognition = new webkitSpeechRecognition();
    recognition.lang = 'en-US';
    recognition.interimResults = false;
    recognition.maxAlternatives = 1;

    recognition.start();

    recognition.onresult = function(event) {
        var userInput = event.results[0][0].transcript;
        $('#user-input').val(userInput);
        askJarvis();
    };

    recognition.onerror = function(event) {
        console.error('Speech recognition error:', event.error);
    };

    recognition.onend = function() {
        console.log('Speech recognition ended.');
    };
}
