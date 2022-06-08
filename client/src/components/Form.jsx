import React, { useState } from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import { Form, Button } from 'react-bootstrap';
import axios from 'axios';


export default function InputForm(props) {

    const url = `https://faceblur01.herokuapp.com/${props.route}`;

    const [reply, setReply] = useState();

    let file;
    let target = '';

    function uploadFile(url, file) {
        const formData = new FormData();
        if (props.route === 'save') {
            formData.append('file', file);
            axios.post(url, formData, {
                headers: {
                    'Content-Type': 'multipart/form-data'
                }
            }).then(response => {
                console.log(response.data);
                setReply(response.data);
                props.changeForm(false);
            }).catch(error => console.log(error));
        } else if (props.route === 'find') {
            formData.append('file', file)
            axios.post(url, formData, {
                /*response type ensures the zip file is not invalid */
                responseType: 'arraybuffer',
                headers: {
                    'Content-Type': 'multipart/form-data'
                }
            }).then(response => {
                const blob = window.URL.createObjectURL(new Blob([response.data], {
                    type: 'application/zip'
                }))
                const link = document.createElement('a');
                link.href = blob;
                link.setAttribute('download', 'file.zip');
                document.body.appendChild(link);
                link.click();
            }).catch(error => console.log(error))
        }

    }

    function onChange(e) {
        file = e.target.files[0];
        target = e.target;
    }


    function submitFile(e) {
        e.preventDefault();
        console.log('target files: ', e.target);
        uploadFile(url, file);
        target.value = null;
        setTimeout(() => { setReply() }, 6000);
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
            reply && < h6 > { reply.message } < /h6>} <
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