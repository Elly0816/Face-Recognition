import React, { useState } from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import { Form, Button } from 'react-bootstrap';
import axios from 'axios';


export default function InputForm(props) {

    const url = `http://127.0.0.1:5000/${props.route}`;

    const [reply, setReply] = useState();

    let file;

    function uploadFile(url, file) {
        let formData = new FormData();
        formData.append('file', file);
        axios.post(url, formData, {
            headers: {
                'Content-Type': 'multipart/form-data'
            }
        }).then(response => {
            setReply(response);
        }).catch(error => console.log(error));
    }

    function onChange(e) {
        file = e.target.files[0];
    }


    function submitFile(e) {
        e.preventDefault();
        console.log('target files: ', e.target);
        let fileToSubmit = file;
        uploadFile(url, fileToSubmit);
    }

    return <div className = 'form-container-parent' >
        <
        div className = 'form' >
        <
        Form onSubmit = { submitFile } >
        <
        div >
        <
        h3 > { props.action } < /h3> <
        /div> <
        Form.Control onChange = { onChange }
    type = "file"
    size = "lg" / >
        <
        div > {
            reply && < p > { reply.message } < /p>} <
            /div> <
            div >
            <
            Button variant = "success"
            type = "submit" > Submit < /Button> <
            /div> <
            /Form> <
            /div> <
            /div>

        }