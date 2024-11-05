import { useState } from 'react';
import { evaluate } from 'mathjs';

function App() {
  const [display, setDisplay] = useState('');

  const buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', '=', '+'],
    ['sin(', 'cos(', 'tan(', '^'],
    ['sqrt(', '(', ')', 'C']
  ];

  const handleClick = (value) => {
    if (value === 'C') {
      setDisplay('');
    } else if (value === '=') {
      try {
        const result = evaluate(display);
        setDisplay(result.toString());
      } catch (error) {
        setDisplay('Error');
      }
    } else {
      setDisplay(display + value);
    }
  };

  return (
    <div className="min-h-screen bg-[#1a472a] flex items-center justify-center p-4">
      <div className="w-full max-w-md bg-[#2d8659] p-6 rounded-xl shadow-2xl">
        <input
          type="text"
          value={display}
          className="w-full mb-4 p-4 text-right text-2xl bg-[#d5f4e6] text-[#0a2f1f] rounded-lg"
          readOnly
        />
        
        <div className="grid grid-cols-4 gap-2">
          {buttons.map((row, i) => 
            row.map((btn, j) => (
              <button
                key={`${i}-${j}`}
                onClick={() => handleClick(btn)}
                className="p-4 text-lg font-semibold bg-[#1a472a] text-white rounded-lg
                         hover:bg-[#0a2f1f] transition-colors duration-200
                         active:transform active:scale-95"
              >
                {btn}
              </button>
            ))
          )}
        </div>
      </div>
    </div>
  );
}

export default App;