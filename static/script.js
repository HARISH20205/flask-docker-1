document.getElementById('predictForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const sepalLength = parseFloat(document.getElementById('sepalLength').value);
    const sepalWidth = parseFloat(document.getElementById('sepalWidth').value);
    const petalLength = parseFloat(document.getElementById('petalLength').value);
    const petalWidth = parseFloat(document.getElementById('petalWidth').value);

    const features = [sepalLength, sepalWidth, petalLength, petalWidth];

    fetch('/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ features })
    })
    .then(response => response.json())
    .then(data => {
        const resultElement = document.getElementById('predictionResult');
        if (data.error) {
            resultElement.innerHTML = `<span id="error">${data.error}</span>`;
        } else {
            const classNames = ['Setosa', 'Versicolor', 'Virginica'];
            resultElement.innerHTML = `Predicted class: ${classNames[data.prediction]}`;
        }
    })
    .catch(error => {
        document.getElementById('predictionResult').innerHTML = `<span id="error">An error occurred: ${error}</span>`;
    });
});
