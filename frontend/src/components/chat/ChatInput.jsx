import React from 'react';

const ChatInput = ({ userInput, setUserInput, onSubmit, isLoading }) => {
  return (
    <div className="chat-input-area">
      <form onSubmit={onSubmit} className="input-form">
        <input
          type="text"
          value={userInput}
          onChange={(e) => setUserInput(e.target.value)}
          placeholder="Describe your symptoms..."
          disabled={isLoading}
          className="chat-input"
        />
        <button type="submit" disabled={!userInput.trim() || isLoading} className="send-button">
          <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
            <path d="m22 2-7 20-4-9-9-4Z" />
            <path d="M22 2 11 13" />
          </svg>
        </button>
      </form>
      <div className="footer-text">
        NativeCare AI is for informational purposes only and does not replace professional medical advice.
      </div>
    </div>
  );
};

export default ChatInput;
