import { useState } from 'react';
import "./Welcome.css";

function Welcome({setPlayerAmount}) {

    const [playersNum, setplayesNum] = useState(0)
    
    return (
        <div className='welcome'>
            <div className='container'>
              <h1>Welcome to The Floor!</h1>
              <div>
                <h2>Add players:</h2>
                 <div className='playerSet'>
                  <button onClick={()=> playersNum > 0 ? setplayesNum(playersNum-1) : setplayesNum(0)}>-</button>
                  <p>{playersNum}</p>
                  <button onClick={()=> playersNum <10 ? setplayesNum(playersNum+1) : setplayesNum(10)}>+</button>
                </div>
              </div>  
              <button id='startButton' onClick={() => setPlayerAmount(true)}>Play!</button>
            </div>
        </div>
    );
};

export default Welcome;