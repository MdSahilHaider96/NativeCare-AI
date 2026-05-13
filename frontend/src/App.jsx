import { useState, useRef, useEffect } from 'react';
import './App.css';
import TechnologyBackground from './components/layout/TechnologyBackground';
import EmergencyBanner from './components/chat/EmergencyBanner';
import ChatHeader from './components/chat/ChatHeader';
import MessageList from './components/chat/MessageList';
import ChatInput from './components/chat/ChatInput';

function App() {
  const [chatHistory, setChatHistory] = useState([
    { role: 'ai', content: 'Hello! I am NativeCare AI. How can I assist you with your health today?' }
  ]);
  const [userInput, setUserInput] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [isEmergency, setIsEmergency] = useState(false);
  const chatEndRef = useRef(null);

  const scrollToBottom = () => {
    chatEndRef.current?.scrollIntoView({ behavior: "smooth" });
  };

  useEffect(() => {
    scrollToBottom();
  }, [chatHistory, isLoading]);

  const handleChat = async (e) => {
    e?.preventDefault();
    if (!userInput.trim() || isLoading) return;

    const query = userInput;
    const updatedHistory = [...chatHistory, { role: 'user', content: query }];
    setUserInput('');
    setChatHistory(updatedHistory);
    setIsLoading(true);

    try {
      const response = await fetch("http://localhost:8001/api/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ 
          query: query,
          history: updatedHistory,
        }),
      });

      if (!response.ok) {
        const errorData = await response.json().catch(() => null);
        throw new Error(errorData?.answer || `Server returned ${response.status}`);
      }

      const data = await response.json();

      if (data.is_emergency) {
        setIsEmergency(true);
        alert("🚨 EMERGENCY DETECTED! CALL 102.");
      }

      setChatHistory(prev => [...prev, { role: 'ai', content: data.answer }]);
    } catch (error) {
      console.error("Chat error:", error);
      setChatHistory(prev => [...prev, { role: 'ai', content: "Sorry, I am having trouble connecting to the server. Please try again later." }]);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="app-container">
      <TechnologyBackground />

      {isEmergency && (
        <EmergencyBanner onDismiss={() => setIsEmergency(false)} />
      )}

      <main className="chat-interface">
        <ChatHeader />

        <MessageList 
          chatHistory={chatHistory} 
          isLoading={isLoading} 
          chatEndRef={chatEndRef} 
        />

        <ChatInput 
          userInput={userInput} 
          setUserInput={setUserInput} 
          onSubmit={handleChat} 
          isLoading={isLoading} 
        />
      </main>
    </div>
  );
}

export default App;
