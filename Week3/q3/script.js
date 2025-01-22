// Function to calculate the grade based on average marks
function calculateGrade() {
    const subject1 = parseInt(document.getElementById("subject1").value);
    const subject2 = parseInt(document.getElementById("subject2").value);
    const subject3 = parseInt(document.getElementById("subject3").value);
    const subject4 = parseInt(document.getElementById("subject4").value);

    // Check if any input is empty or not a valid number
    if (isNaN(subject1) || isNaN(subject2) || isNaN(subject3) || isNaN(subject4)) {
        alert("Please enter valid marks for all subjects.");
        return;
    }

    // Calculate the average
    const total = subject1 + subject2 + subject3 + subject4;
    const average = total / 4;

    // Determine grade based on average
    let grade = '';
    if (average > 90) {
        grade = 'A';
    } else if (average > 80) {
        grade = 'B';
    } else if (average > 70) {
        grade = 'C';
    } else if (average > 60) {
        grade = 'D';
    } else {
        grade = 'F';
    }

    // Display results
    document.getElementById("grade").innerText = grade;
    document.getElementById("average").innerText = average.toFixed(2);

    // Show the result section with animation
    document.getElementById("result").style.display = 'block';
    document.getElementById("result").classList.add('fadeInResult');
}
