const quizData = [
    {
        question: "What is the capital of France?",
        options: ["Berlin", "Madrid", "Paris", "Rome"],
        correctAnswer: "Paris"
    },
    {
        question: "Which planet is known as the Red Planet?",
        options: ["Earth", "Mars", "Jupiter", "Saturn"],
        correctAnswer: "Mars"
    },
    {
        question: "Who wrote 'Romeo and Juliet'?",
        options: ["William Shakespeare", "Jane Austen", "Charles Dickens", "Mark Twain"],
        correctAnswer: "William Shakespeare"
    },
    {
        question: "What is the largest ocean on Earth?",
        options: ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
        correctAnswer: "Pacific Ocean"
    },
    {
        question: "What is the smallest prime number?",
        options: ["0", "1", "2", "3"],
        correctAnswer: "2"
    }
];

let currentQuestionIndex = 0;
let score = 0;

// Function to load the current question
function loadQuestion() {
    const quizContainer = document.getElementById("quiz-container");
    quizContainer.innerHTML = ''; // Clear the container for the new question

    const questionObj = quizData[currentQuestionIndex];
    const questionElement = document.createElement("div");
    questionElement.classList.add("question");
    
    questionElement.innerHTML = `
        <h3>${questionObj.question}</h3>
        <div class="options">
            ${questionObj.options.map((option, index) => `
                <label>
                    <input type="radio" name="question${currentQuestionIndex}" value="${option}">
                    ${option}
                </label><br>
            `).join('')}
        </div>
    `;
    quizContainer.appendChild(questionElement);
}

// Function to move to the next question
function nextQuestion() {
    const selectedOption = document.querySelector(`input[name="question${currentQuestionIndex}"]:checked`);
    if (!selectedOption) {
        alert("Please select an answer before moving to the next question.");
        return;
    }

    // Check if the answer is correct
    if (selectedOption.value === quizData[currentQuestionIndex].correctAnswer) {
        score++;
    }

    currentQuestionIndex++;

    if (currentQuestionIndex < quizData.length) {
        loadQuestion(); // Load the next question
    } else {
        showScore(); // All questions are answered, show the score
    }
}

// Function to display the final score
function showScore() {
    const scoreContainer = document.getElementById("score");
    scoreContainer.innerHTML = `Your score is: ${score} out of ${quizData.length}`;
    document.getElementById("next-btn").style.display = "none"; // Hide the next question button after the quiz
}

// Event listener for the "Next Question" button
document.getElementById("next-btn").addEventListener("click", nextQuestion);

// Initial load of the first question
loadQuestion();
