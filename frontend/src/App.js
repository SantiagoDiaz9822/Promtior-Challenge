import React, { useState } from "react";
import "./App.css";
import { ClipLoader } from "react-spinners";

function App() {
  const [messages, setMessages] = useState([]); // Store chat messages
  const [inputValue, setInputValue] = useState(""); // Store user input
  const [isLoading, setIsLoading] = useState(false); // Loading state

  // Function to send a message to the API
  const sendMessage = async () => {
    const message = inputValue.trim();
    if (!message) return;

    // Add the user's message to the chat
    setMessages((prevMessages) => [
      ...prevMessages,
      { sender: "You", text: message },
    ]);
    setInputValue(""); // Clear the input field

    // Set loading state to true
    setIsLoading(true);

    try {
      // Call the FastAPI backend
      const response = await fetch(
        "http://promti-Publi-6mSUCkjCjP8v-625302517.us-east-1.elb.amazonaws.com/promtior-chatbot/invoke",
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            input: message,
          }),
        }
      );

      if (!response.ok) {
        throw new Error("Failed to fetch response");
      }

      const data = await response.json();
      const botResponse = data.output;

      // Add the bot's response to the chat
      setMessages((prevMessages) => [
        ...prevMessages,
        { sender: "Bot", text: botResponse },
      ]);
    } catch (error) {
      console.error("Error:", error);
      // Add an error message to the chat
      setMessages((prevMessages) => [
        ...prevMessages,
        { sender: "Error", text: "Failed to get a response from the bot." },
      ]);
    } finally {
      // Set loading state to false
      setIsLoading(false);
    }
  };

  return (
    <div className="App">
      <h1>Promtior Chatbot</h1>
      <div className="chatbox">
        {messages.map((msg, index) => (
          <p key={index}>
            <strong>{msg.sender}:</strong> {msg.text}
          </p>
        ))}
        {/* Show "..." while loading */}
        {isLoading && (
          <p>
            <strong>Bot:</strong> <ClipLoader size={10} color="#007bff" />
          </p>
        )}
      </div>
      <div className="input-container">
        <input
          type="text"
          value={inputValue}
          onChange={(e) => setInputValue(e.target.value)}
          placeholder="Type your message here..."
          onKeyPress={(e) => e.key === "Enter" && sendMessage()}
        />
        <button onClick={sendMessage} disabled={isLoading}>
          Send
        </button>
      </div>
    </div>
  );
}

export default App;
