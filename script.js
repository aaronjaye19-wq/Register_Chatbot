const API_URL = 'http://localhost:5000';

const chatContainer = document.getElementById('chatContainer');
const userInput = document.getElementById('userInput');
const sendBtn = document.getElementById('sendBtn');

userInput.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') {
        sendMessage();
    }
});

function askSample(question) {
    userInput.value = question;
    sendMessage();
}

async function sendMessage() {
    const message = userInput.value.trim();

    if (!message) return;

    const welcomeMessage = document.querySelector('.welcome-message');
    if (welcomeMessage) {
        welcomeMessage.remove();
    }

    addMessage(message, 'user');
    userInput.value = '';

    showTypingIndicator();

    try {
        const response = await fetch(`${API_URL}/chat`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ message: message })
        });

        const data = await response.json();

        removeTypingIndicator();

        if (data.response) {
            addMessage(data.response, 'bot');
        } else {
            addMessage('Sorry, I encountered an error. Please try again.', 'bot');
        }
    } catch (error) {
        console.error('Error:', error);
        removeTypingIndicator();
        addMessage('Unable to connect to the server. Please make sure the backend is running.', 'bot');
    }
}

function addMessage(text, sender) {
    const messageDiv = document.createElement('div');
    messageDiv.className = `message ${sender}`;

    const contentDiv = document.createElement('div');
    contentDiv.className = 'message-content';
    contentDiv.textContent = text;

    messageDiv.appendChild(contentDiv);
    chatContainer.appendChild(messageDiv);

    chatContainer.scrollTop = chatContainer.scrollHeight;
}

function showTypingIndicator() {
    const typingDiv = document.createElement('div');
    typingDiv.className = 'message bot';
    typingDiv.id = 'typingIndicator';

    const contentDiv = document.createElement('div');
    contentDiv.className = 'message-content';

    const typingIndicator = document.createElement('div');
    typingIndicator.className = 'typing-indicator';
    typingIndicator.innerHTML = `
        <div class="typing-dot"></div>
        <div class="typing-dot"></div>
        <div class="typing-dot"></div>
    `;

    contentDiv.appendChild(typingIndicator);
    typingDiv.appendChild(contentDiv);
    chatContainer.appendChild(typingDiv);

    chatContainer.scrollTop = chatContainer.scrollHeight;
}

function removeTypingIndicator() {
    const typingIndicator = document.getElementById('typingIndicator');
    if (typingIndicator) {
        typingIndicator.remove();
    }
}