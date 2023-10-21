document.addEventListener('DOMContentLoaded', function() {
    const questionInput = document.getElementById('questionInput');
    const askButton = document.getElementById('askButton');
    const responseDiv = document.getElementById('response');

    askButton.addEventListener('click', function() {
        const question = questionInput.value;

        // Check if the question is not empty
        if (question.trim() === '') {
            alert('Please enter a question.');
            return;
        }

        // Send the question to the Python script
        fetch('http://127.0.0.1:8000/handle_question', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ question })
        })
        // fetch('http://127.0.0.1:8000/test', {
        //  method: 'GET' // Change to GET
        // })
        .then(response => response.json())
        .then(data => {
            // Display the response from the Python script
            responseDiv.innerHTML = `<strong>Response:</strong> ${data.answer}`;
        })
        .catch(error => {
            console.error('An error occurred:', error);
            responseDiv.innerHTML = `<strong>Error:</strong> ${error.message}`;
        });
    });
});