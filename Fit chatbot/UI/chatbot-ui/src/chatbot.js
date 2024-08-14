// src/Chatbot.js

import React, { useState, useEffect } from 'react';
import CountryDropdown from './CountryDropdown';

const Chatbot = () => {
    const [question, setQuestion] = useState('');
    const [messages, setMessages] = useState([]);
    const [loading, setLoading] = useState(false);
    const [selectedCountry, setSelectedCountry] = useState('en');
    const [isMinimized, setIsMinimized] = useState(true);

    useEffect(() => {
        // Add initial message when the component mounts
        if (!isMinimized) {
            setMessages([{ type: 'bot', text: "Hi, welcome to simple chatbot. How can I help you?" }]);
        }
    }, [isMinimized]);

    const handleInputChange = (e) => {
        setQuestion(e.target.value);
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        if (question.trim()) {
            setMessages([...messages, { type: 'user', text: question }]);
            setLoading(true); // Start loading
            try {
                const response = await fetch('http://127.0.0.1:5000/chatbot', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({ question, language: selectedCountry }),
                });
                const data = await response.json();
                setMessages([...messages, { type: 'user', text: question }, { type: 'bot', text: data.message }]);
            } catch (error) {
                console.error('Error fetching response:', error);
            }
            setLoading(false); // Stop loading
            setQuestion('');
        }
    };

    const toggleChat = () => {
        setIsMinimized(!isMinimized);
    };

    return (
        <div>
            {/* Minimized Icon */}
            {isMinimized && (
                <div className="chatbot-icon" onClick={toggleChat}>
                    <div className="chatbot-tooltip">I'm a chatbot. How can I help you?</div>
                    <div className="chatbot-icon-img" > </div>
                </div>
            )}

            {/* Chat Window */}
            {!isMinimized && (
                <div className="chatbot">
                    <div className="chatbot-header">
                        <CountryDropdown onChange={setSelectedCountry} />
                        <button className="toggle-button" onClick={toggleChat}>
                            Minimize
                        </button>
                    </div>
                    <div className="chatbot-messages">
                        {messages.map((msg, index) => (
                            <div key={index} className={`chatbot-message ${msg.type}`}>
                                {msg.text}
                            </div>
                        ))}
                        {loading && (
                            <div className="loader">
                                <div></div>
                                <div></div>
                                <div></div>
                            </div>
                        )}
                    </div>
                    <form onSubmit={handleSubmit} className="chatbot-form">
                        <input
                            type="text"
                            value={question}
                            onChange={handleInputChange}
                            placeholder="Ask me anything..."
                            disabled={loading}
                        />
                        <button type="submit" disabled={loading}>Send</button>
                    </form>
                </div>
            )}
        </div>
    );
};

export default Chatbot;
