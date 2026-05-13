import React from 'react';
import './TechnologyBackground.css';

const TechnologyBackground = () => {
  return (
    <div className="tech-bg-container">
      <div className="tech-grid"></div>
      <div className="tech-particles">
        {Array.from({ length: 20 }).map((_, i) => (
          <div key={i} className={`particle particle-${i + 1}`}></div>
        ))}
      </div>
      <div className="tech-scanline"></div>
      <div className="tech-glow glow-1"></div>
      <div className="tech-glow glow-2"></div>
    </div>
  );
};

export default TechnologyBackground;
