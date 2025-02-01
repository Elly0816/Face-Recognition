

type HeaderProps = {
    changeForm: (from: boolean) => void
}
export default function Header({changeForm}:HeaderProps){

    
    function toFind(){
        changeForm(true);
    }

    function toSave(){
        changeForm(false);
    }
    /*The functions above change the toFind state in parent (App) component */

    return <header>
        <div className='title'>
        <div>
            <a href="/"><h1>fACE bLUR</h1></a>
        </div>
        </div>
        <div className='links'>
            <div>
                {/* <a href="#"><h5 onClick={toFind}>Find and blur this face</h5></a> */}
                <button type={'button'} onClick={toFind} title='Find and blur this face'>Find and blur this face</button>
            </div>
            
            <div>
                {/* <a href="#"><h5 onClick={toSave}>Add to Images</h5></a>     */}
                <button type={'button'} onClick={toSave} title='Add to Images'>Add to Images</button>
            </div>
        </div>
    </header>
}