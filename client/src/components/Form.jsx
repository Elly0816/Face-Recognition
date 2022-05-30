import React from 'react';
import { Form } from 'react-bootstrap';


export default function InputForm(props) {



    return <div className = 'form-container-parent' >
        <
        div className = 'form' >
        <
        Form >
        <
        div >
        <
        h3 > { props.action } < /h3> <
        /div> <
        Form.Control type = "file"
    size = "lg" / >
        <
        /Form> <
        /div> <
        /div>

}