const form = document.getElementById('travel-form');
const resultDiv = document.getElementById('result');

form.addEventListener('submit', async (event) => {
    event.preventDefault();

    const formData = new FormData(form);
    const response = await fetch('http://127.0.0.1:5000', {
        method: 'POST',
        body: formData
    });

    const data = await response.json();
    resultDiv.textContent = data.itinerary;
});