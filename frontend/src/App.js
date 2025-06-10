import { useState } from 'react';
import './App.css';
import Welcome from './main/Welcome';

function App() {
  
  const [PlayerAmount, setPlayerAmount] = useState(false)
  //const [playerName, setplayerName] = useState(false)
  //const [game, setGame] = useState(false)
   

  return (
    <div className="App">
      {
        !PlayerAmount &&
        <Welcome setPlayerAmount = {setPlayerAmount}/>
      }
      
    </div>
  );
}

export default App;
