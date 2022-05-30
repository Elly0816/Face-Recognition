import React from 'react';

export default function Header(props) {

    function toFind() {
        props.changeForm(true);
    }


    function toSave() {
        props.changeForm(false);
    }

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
        a href = "#" > < h3 onClick = { toFind } > Find and blur this face < /h3></a >
        <
        /div>

    <
    div >
        <
        a href = "#" > < h3 onClick = { toSave } > Add to Images < /h3></a >
        <
        /div> <
        /div> <
        /header>
}