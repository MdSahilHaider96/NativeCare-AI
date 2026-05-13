import React from 'react';

const MessageBubble = ({ message }) => {
  const isAI = message.role === 'ai';

  return (
    <div className={`message-wrapper ${message.role}`}>
      {isAI && (
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
      )}
      <div className={`message ${message.role}`}>
        <div className="message-content">{message.content}</div>
      </div>
    </div>
  );
};

export default MessageBubble;
