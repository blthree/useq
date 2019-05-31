'use strict';
import React, { Component } from "react";
import ReactDOM from "react-dom";
const e = React.createElement;

class SeqStep extends React.Component {
  constructor(props) {
    super(props);
    this.state = { note: "XXX", step: this.props.step_num, id: this.props.id };
  }

  render() {
        return (<span id= {"step"+this.props.id+"-note"} className="seq-note">{this.props.note}</span>);
     }


}
export default SeqStep;