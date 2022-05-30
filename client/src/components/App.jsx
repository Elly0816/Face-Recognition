import React, { useState } from 'react';
import Header from './Header';
import InputForm from './Form';
import Footer from './Footer';

function App() {

    const [toFind, setToFind] = useState(true);

    function changeForm(what) {
        setToFind(what);
    }

    return <div >
        <
        Header changeForm = { changeForm }
    /> {
        toFind ?
            <
            InputForm action = { 'Upload the image with the face you would like to blur' }
        /> :  <
        InputForm action = { 'Upload the image you would like to save' }
        />} <
        Footer / >
            <
            /div>

    }

    export default App;