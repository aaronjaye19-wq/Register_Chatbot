const API_URL = 'http://localhost:5000';

const chatContainer = document.getElementById('chatContainer');
const userInput = document.getElementById('userInput');
const sendBtn = document.getElementById('sendBtn');

// Store message history for edit functionality
const messageHistory = [];

userInput.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') {
        sendMessage();
    }
});

function askSample(question) {
    userInput.value = question;
    sendMessage();
}

function editMessage(index) {
    const userMessage = messageHistory[index];
    if (userMessage) {
        userInput.value = userMessage.text;
        userInput.focus();
        
        // Remove the old message and bot response
        const messages = document.querySelectorAll('.message');
        let userCount = 0;
        
        messages.forEach((msg, idx) => {
            if (msg.classList.contains('user')) {
                userCount++;
                if (userCount === index + 1) {
                    // Remove this user message
                    msg.remove();
                    // Remove following bot response if exists
                    const nextMsg = messages[idx + 1];
                    if (nextMsg && nextMsg.classList.contains('bot')) {
                        nextMsg.remove();
                    }
                }
            }
        });
        
        // Remove from history
        messageHistory.splice(index, 1);
    }
}

async function sendMessage() {
    const message = userInput.value.trim();

    if (!message) return;

    const welcomeMessage = document.querySelector('.welcome-message');
    if (welcomeMessage) {
        welcomeMessage.remove();
    }

    const isEdited = messageHistory.some(msg => msg.text === message);
    addMessage(message, 'user', isEdited);
    messageHistory.push({ text: message, edited: isEdited });
    userInput.value = '';

    showTypingIndicator();

    try {
        const response = await fetch(`${API_URL}/chat`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ message: message, is_edited: isEdited })
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

function addMessage(text, sender, isEdited = false) {
    const messageDiv = document.createElement('div');
    messageDiv.className = `message ${sender}`;

    const contentDiv = document.createElement('div');
    contentDiv.className = 'message-content';
    contentDiv.textContent = text;

    messageDiv.appendChild(contentDiv);

    // Add edit button for user messages
    if (sender === 'user') {
        const actionDiv = document.createElement('div');
        actionDiv.className = 'message-actions';
        
        const editBtn = document.createElement('button');
        editBtn.className = 'edit-btn';
        editBtn.innerHTML = `
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M11 4H4a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-7"></path>
                <path d="M18.5 2.5a2.121 2.121 0 0 1 3 3L12 15l-4 1 1-4 9.5-9.5z"></path>
            </svg>
            Edit
        `;
        editBtn.onclick = () => editMessage(messageHistory.length - 1);
        
        if (isEdited) {
            const editedLabel = document.createElement('span');
            editedLabel.className = 'edited-label';
            editedLabel.textContent = 'edited';
            actionDiv.appendChild(editedLabel);
        }
        
        actionDiv.appendChild(editBtn);
        messageDiv.appendChild(actionDiv);
    }

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
