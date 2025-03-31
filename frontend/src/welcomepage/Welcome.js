import React, { useState } from 'react';
import "./Welcome.css";

const Welcome = () => {

    const [playersNum, setplayesNum] = useState(0)
    
    return (
        <div className='welcome'>
            <div className='container'>
              <h1>Welcome to The Floor!</h1>
              <h2>Add players:</h2>
              <div className='playerSet'>
                <button onClick={()=> setplayesNum(playersNum-1)}>-</button>
                <p>{playersNum}</p>
                <button onClick={()=> setplayesNum(playersNum+1)}>+</button>
              </div>
              <button id='startButton'>Play!</button>
            </div>
           
        </div>
    );
};

export default Welcome;