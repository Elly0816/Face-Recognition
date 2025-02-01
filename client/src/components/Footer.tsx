import React, { ReactElement } from 'react';

export default function Footer():ReactElement{

    const year = new Date().getFullYear();


    return <footer>
        <p>Copyright ©️ { year }</p>
    </footer>
}