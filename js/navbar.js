function navbar(){
    var title=document.title;
    // if (title=="Home"){
        var syntax=`
        <div class="container-fluid">
            <div class="navbar-collapse" id="navbarNavAltMarkup">
                <div class="navbar-nav">
                    <a class="nav-link" aria-current="page" href="index.html" id="homePage">Home</a>
                    <a class="nav-link" href="music.html" id="musicPage">Music</a>
                   <a class ="nav-link" href="Potato.html" id="PotatoPage">Potato</a>
                </div>
                <input type="text" class="form-control margin-right-1rem width-800 mx-3" name="service" id="petSearchServiceTxt"> 
                <button type="button" class="btn btn-primary" > Search</button>
                </div>
        </div>
        `;
    // }else{
    //     var syntax=`
    //     <div class="container-fluid">
    //         <div class="navbar-collapse" id="navbarNavAltMarkup">
    //             <div class="navbar-nav">
    //                 <a class="nav-link" aria-current="page" href="index.html" id="homePage">Home</a>
    //                 <a class="nav-link" href="music.html" id="musicPage">Music</a>
    //                <a class ="nav-link" href="Potato.html" id="PotatoPage">Potato</a>
    //             </div>
    //             </div>
    //     </div>
    //     `;
    // }
    if(title=="Home"){
        $(".navbar").append(syntax);
        $("#homePage").addClass("active");
    }else if(title =="Music"){
        $(".navbar").append(syntax);
        $("#musicPage").addClass("active");
    }else if(title =="Potato"){
        $(".navbar").append(syntax);
        $("#PotatoPage").addClass("active");
    }else if(title =="Music-Lyrics"){
        var syntax=`
        <div class="container-fluid">
            <div class="navbar-collapse" id="navbarNavAltMarkup">
                <div class="navbar-nav">
                    <a class="nav-link" aria-current="page" href="../index.html" id="homePage">Home</a>
                    <a class="nav-link" href="../music.html" id="musicPage">Music</a>
                    <a class ="nav-link" href="../Potato.html" id="PotatoPage">Potato</a>
                </div>
            </div>
        </div>
        `;
        $(".navbar").append(syntax);
        $("#musicPage").addClass("active");
    }
}
