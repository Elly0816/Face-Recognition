import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import { Form, Button } from 'react-bootstrap';


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
        div >
        <
        Button variant = "success"
    type = "submit" > Submit < /Button> <
        /div> <
        /Form> <
        /div> <
        /div>

}