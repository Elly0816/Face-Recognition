import React, { useState } from 'react';
import Header from './Header';
import InputForm from './Form';
import Footer from './Footer';

function App() {

  /*This state is used to chek whether the user wants to save an image
  or is sending a reference image to blur faces */
  const [toFind, setToFind] = useState(true);


  /*This changes the state above in the Header component to true or false */
  function changeForm(what){
    setToFind(what);
  }

  return <div>
    <Header changeForm={changeForm}/>
    {toFind ? 
    <InputForm action={'Upload the image with the face you would like to blur'}
                route={'find'}
                changeForm={changeForm}
    /> : 
    <InputForm action={'Upload the image you would like to save'}
                route={'save'}
                changeForm={changeForm}
    />}
    <Footer/>
  </div>

}

export default App;
