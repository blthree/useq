import React, { Component } from "react";
import ReactDOM from "react-dom";

class NoteSelector extends React.Component {
  constructor(props) {
    super(props);
    this.state = {value: '-1'};

    this.handleChange = this.handleChange.bind(this);
  }

  handleChange(event) {
    this.setState({value: event.target.value});
    alert('Your favorite flavor is: ' + event.target.value);
  }


  render() {
    return (
          <label>Step 7:
            <select id="step7" class="seq-step" value={this.state.value} onChange={this.handleChange}>
                <option value="-1">XXX</option>
                <option value="0">G2</option>
                <option value="1">G#2</option>
                <option value="2">A3</option>
                <option value="3">A#3</option>
                <option value="4">B3</option>
                <option value="5">C3</option>
                <option value="6">C#3</option>
                <option value="7">D3</option>
                <option value="8">D#3</option>
                <option value="9">E3</option>
                <option value="10">F3</option>
                <option value="11">F#3</option>

                <option value='12'>G3</option>
                <option value="13">G#3</option>
                <option value="14">A4</option>
                <option value="15">A#4</option>
                <option value="16">B4</option>
                <option value="17">C4</option>
                <option value="18">C#4</option>
                <option value="19">D4</option>
                <option value="20">D#4</option>
                <option value="21">E4</option>
                <option value="22">F4</option>
                <option value="23">F#4</option>

                <option value="24">G4</option>
                <option value="25">G#4</option>
                <option value="26">A5</option>
                <option value="27">A#5</option>
                <option value="28">B5</option>
                <option value="29">C5</option>
                <option value="30">C#5</option>
                <option value="31">D5</option>
                <option value="32">D#5</option>
                <option value="33">E5</option>
                <option value="34">F5</option>
                <option value="35">F#5</option>
            </select></label>
    );
  }
}

// const wrapper = document.getElementById("seq-input-holder");
// wrapper ? ReactDOM.render(<NoteSelector />, wrapper) : false;

export default NoteSelector;