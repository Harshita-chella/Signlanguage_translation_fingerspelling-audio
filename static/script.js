window.addEventListener("DOMContentLoaded", (event) => {

	const text = 
		document.getElementById("textToConvert");
	const convertBtn = 
		document.getElementById("convertBtn");

	convertBtn.addEventListener('click', function () {
		const speechSynth = window.speechSynthesis;
		const enteredText = text.value;
		const error = document.querySelector('.error-para');
		if (!speechSynth.speaking &&
			!enteredText.trim().length) {
			error.textContent = `Nothing to Convert! 
			Enter text in the text area.`
		}
		if (!speechSynth.speaking && enteredText.trim().length) {
			error.textContent = "";
			const newUtter = 
				new SpeechSynthesisUtterance(enteredText);
			speechSynth.speak(newUtter);
			convertBtn.textContent = "Sound is Playing..."
		}
		setTimeout(() => {
			convertBtn.textContent = "Play Converted Sound"
		}, 5000);
	});

	const executeBtn = document.getElementById("execute");
    const toggleContainer = document.getElementById("toggle-container");
    const toggleBackBtn = document.getElementById("toggle-back-btn");

    executeBtn.addEventListener('click', function () {
        // Code to execute after clicking "Execute Python Script" button
        // For demonstration, let's just slide in the toggle container and shift the body to the left
        toggleContainer.style.right = "0"; // Slide in the container from the right
        document.body.classList.add('move-left'); // Shift the body section to the left
    });

    toggleBackBtn.addEventListener("click", function () {
        // Code to execute after clicking "Close" button
        // For demonstration, let's just slide out the toggle container and shift the body back to its initial position
        toggleContainer.style.right = "-100%"; // Slide out the container to the right
        document.body.classList.remove('move-left'); // Shift the body section back to its initial position
    });

});
