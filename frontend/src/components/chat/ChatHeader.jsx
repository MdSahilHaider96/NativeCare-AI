import React from 'react';

const ChatHeader = () => {
  return (
    <header className="chat-header">
      <div className="header-brand">
        <div className="logo-container" style={{ padding: 0, overflow: 'hidden' }}>
          <img src="/nativecare-logo.png" alt="NativeCare AI Logo" style={{ width: '100%', height: '100%', objectFit: 'cover' }} />
        </div>
        <div>
          <h1>NativeCare AI</h1>
          <p className="status">
            <span className="status-dot"></span> Online and ready
          </p>
        </div>
      </div>
    </header>
  );
};

export default ChatHeader;
