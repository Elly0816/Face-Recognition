import React, { ChangeEvent, FormEvent, ReactElement, useState } from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import { Form, Button } from 'react-bootstrap';
import axios from 'axios';



type replyType = {
    'message': string
}

type InputFormType = {
    route:string,
    changeForm:(value:boolean)=>void,
    action:string
}
export default function InputForm({route, changeForm, action}:InputFormType):ReactElement{

    const url = `/${route}`;

    const [reply, setReply] = useState<replyType>();

    let file:File;
    let target:ChangeEvent<HTMLFormElement>['target'];

    function uploadFile(url:string, file:File){
        const formData = new FormData();
        if (route === 'save'){
        formData.append('file', file);
        axios.post(url, formData, {
            headers: {
                'Content-Type': 'multipart/form-data'
            }
        }).then(response => {
            console.log(response.data);
            setReply(response.data);
            changeForm(false);
        }).catch(error => console.log(error));
        }
        else if (route === 'find'){
            /*In case no file was sent */
            if (!file){
                setReply({'message': "There was no file sent!"});
            } /*In case the wrong file type was sent*/
            else {
                const fileName = file.name.toLowerCase();
                const fileType = fileName.slice((fileName.lastIndexOf(".") -1 >>> 0) + 2);
                if ((fileType === 'jpg') || (fileType === 'jpeg') || (fileType === 'png')) {
                    formData.append('file', file)
                    axios.post(url, formData, {
                    /*response type ensures the zip file is not invalid */
                    responseType: 'arraybuffer',
                    headers: {
                        'Content-Type': 'multipart/form-data'
                    }
                    })
                    .then(response => {
                    setReply({'message': "Your file should have been. If not, we found no images matching the face sent"});
                    const blob = window.URL.createObjectURL(new Blob([response.data], {type: 
                    'application/zip'}))
                    const link = document.createElement('a');
                    link.href = blob;
                    link.setAttribute('download', 'file.zip');
                    document.body.appendChild(link);
                    link.click();
                    })
                    .catch(error => console.log(error))
                }
                else {
                    setReply({'message': "Invalid File Type!"});
                    
                }
            }
            
        }
        
    }

    function onChange(e:ChangeEvent<HTMLFormElement>){
        file = e.target.files[0];
        target = e.target;
    }


    function submitFile(event:FormEvent<HTMLFormElement>){
        event.preventDefault();
        console.log('target files: ', event.target);
        uploadFile(url, file);
        target.value = null;
        setTimeout(() => {setReply(undefined)}, 6000);
    }

    return <div className='form-container-parent'>
        <div className='form'>
            <Form onSubmit={(event) => {
                console.log('File submit attempt was made');
                submitFile.bind(event)}}>
                <div>
                    <h3>{action}</h3>
                </div>
                <Form.Control onChange={(event) => onChange.bind(event)} type="file" size="lg"/>
                <div>
                    {reply && <h6>{reply.message}</h6>}
                </div>
                <div>
                    <Button variant="success" type="submit">Submit</Button>
                </div>
            </Form>
        </div>
    </div>
    
}