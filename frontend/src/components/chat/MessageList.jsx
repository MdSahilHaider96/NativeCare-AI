import React from 'react';
import MessageBubble from './MessageBubble';

const MessageList = ({ chatHistory, isLoading, chatEndRef }) => {
  return (
    <div className="chat-messages">
      {chatHistory.map((msg, index) => (
        <MessageBubble key={index} message={msg} />
      ))}
      
      {isLoading && (
        <div className="message-wrapper ai">
          <div className="avatar ai-avatar">
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
              <path d="M12 8V4H8" />
              <rect width="16" height="12" x="4" y="8" rx="2" />
              <path d="M2 14h2" />
              <path d="M20 14h2" />
              <path d="M15 13v2" />
              <path d="M9 13v2" />
            </svg>
          </div>
          <div className="message ai typing">
            <span className="dot"></span>
            <span className="dot"></span>
            <span className="dot"></span>
          </div>
        </div>
      )}
      <div ref={chatEndRef} />
    </div>
  );
};

export default MessageList;
