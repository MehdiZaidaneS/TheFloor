import React, { useState } from 'react';
import mydata from "../testdata/data.json"
import "./Welcome.css";

const Welcome = () => {

    const [playersNum, setplayesNum] = useState(0)
    const [amountConfirmed, setamountConfirmed] = useState(false) 
   

    
    
    function setInputs(){
      let content = []
      for (let i= 0; i<playersNum; i++){
         content.push(
          <div className='player' key={i}>
            <input type="text" id="fname" name="fname" placeholder='Player name...'></input>
            <select id="category" name="category">
              <option value="volvo">Choose category</option>
              {
                mydata.map(category => (
                  <option value={category.name} key={category.name}>{category.name}</option>
                ))
              }
            </select>
          </div>
        )
      }
      return content
    }

    return (
        <div className='welcome'>
            <div className='container'>
              <h1>Welcome to The Floor!</h1>
              {
                amountConfirmed === false &&
                <div>
                  <h2>Add players:</h2>
                  <div className='playerSet'>
                    <button onClick={()=> playersNum > 0 ? setplayesNum(playersNum-1) : setplayesNum(0)}>-</button>
                    <p>{playersNum}</p>
                    <button onClick={()=> playersNum <10 ? setplayesNum(playersNum+1) : setplayesNum(10)}>+</button>
                  </div>
                </div>  
              }
              {
                amountConfirmed && setInputs()       
              }
              <button id='startButton' onClick={()=> setamountConfirmed(true)}>Play!</button>
            </div>
        </div>
    );
};

export default Welcome;