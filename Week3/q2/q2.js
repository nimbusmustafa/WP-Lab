// Function to update the clock and wish the user
function updateClockAndWish() {
    const now = new Date();
    const hours = now.getHours();
    const minutes = now.getMinutes();
    const seconds = now.getSeconds();

    // Formatting time for clock and greeting
    const time = `${hours < 10 ? '0' : ''}${hours}:${minutes < 10 ? '0' : ''}${minutes}:${seconds < 10 ? '0' : ''}${seconds}`;

    // Display dynamic clock time
    const clockTimeElement = document.getElementById("clock-time");
    clockTimeElement.innerHTML = `<span>${time}</span>`;

    // Calculate rotation for each hand
    const hourRotation = (hours % 12) * 30 + (minutes / 60) * 30; // 30 degrees per hour
    const minuteRotation = minutes * 6; // 6 degrees per minute
    const secondRotation = seconds * 6; // 6 degrees per second

    // Update the rotation of the clock hands
    document.getElementById("hour-hand").style.transform = `rotate(${hourRotation}deg)`;
    document.getElementById("minute-hand").style.transform = `rotate(${minuteRotation}deg)`;
    document.getElementById("second-hand").style.transform = `rotate(${secondRotation}deg)`;

    // Wishing based on the time of day
    const greetingElement = document.getElementById("greeting");
    if (hours >= 5 && hours < 12) {
        greetingElement.innerHTML = "Good Morning! 🌞";
        alert("Good Morning! 🌞");
    } else if (hours >= 12 && hours < 17) {
        greetingElement.innerHTML = "Good Afternoon! ☀️";
        alert("Good Afternoon! ☀️");
    } else if (hours >= 17 && hours < 21) {
        greetingElement.innerHTML = "Good Evening! 🌇";
        alert("Good Evening! 🌇");
    } else {
        greetingElement.innerHTML = "Good Night! 🌙";
        alert("Good Night! 🌙");
    }

    // Set the clock update interval
    setTimeout(updateClockAndWish, 1000);
}

// Call the function when the page loads
updateClockAndWish();
