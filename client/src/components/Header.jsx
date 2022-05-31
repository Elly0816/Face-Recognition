import React from 'react';

export default function Header(props) {


    function toFind() {
        props.changeForm(true);
    }

    function toSave() {
        props.changeForm(false);
    }
    /*The functions above change the toFind state in parent (App) component */

    return <header >
        <
        div className = 'title' >
        <
        h1 > fACE bLUR < /h1> <
        /div> <
        div className = 'links' >
        <
        div >
        <
        a href = "#" > < h5 onClick = { toFind } > Find and blur this face < /h5></a >
        <
        /div>

    <
    div >
        <
        a href = "#" > < h5 onClick = { toSave } > Add to Images < /h5></a >
        <
        /div> <
        /div> <
        /header>
}