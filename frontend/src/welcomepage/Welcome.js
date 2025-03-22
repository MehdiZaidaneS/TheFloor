import React, { useState } from 'react';
import "./Welcome.css";

const Welcome = () => {

    const [playersNum, setplayesNum] = useState(0)
    
    return (
        <div>
            <h1>Welcome to The FloorGame!</h1>
            <h2>Add players</h2>
            <button onClick={()=> setplayesNum(playersNum-1)}>-</button>
            <p>{playersNum}</p>
            <button onClick={()=> setplayesNum(playersNum+1)}>+</button>
            <button>Start!</button>
        </div>
    );
};

export default Welcome;