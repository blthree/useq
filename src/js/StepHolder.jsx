'use strict';
import React, { Component } from "react";
import ReactDOM from "react-dom";
import SeqStep from "./SeqStep.jsx"


class StepHolder extends React.Component {
    constructor(props) {
        super(props);
        this.state = { num_notes: [...Array(8).keys()]};
      }
      //num_notes = Array(8)
    // Correct! Key should be specified inside the array.

      steps = [...Array(8).keys()].map((i) => 
        <SeqStep key={i.toString()} 
            id={i.toString()} 
            note={"XXX"} />)
      render () {
         
          return (
        <div id="seq-output">
            {this.steps}
        </div>)
      }  
}

const wrapper = document.getElementById("seq-output-holder");
wrapper ? ReactDOM.render(<StepHolder />, wrapper) : false;

export default StepHolder;