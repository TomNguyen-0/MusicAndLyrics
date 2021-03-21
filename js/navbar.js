function navbar(){
    var title=document.title;
    var syntax=`
    <div class="container-fluid">
        <div class="navbar-collapse" id="navbarNavAltMarkup">
            <div class="navbar-nav">
                <a class="nav-link" aria-current="page" href="index.html" id="homePage">Home</a>
                <a class="nav-link" href="music.html" id="musicPage">Music</a>

            </div>
        </div>
    </div>
    `;
    $(".navbar").append(syntax);
    if(title=="Home"){
        $("#homePage").addClass("active");
    }else if(title =="Music"){
        $("#musicPage").addClass("active");
    }else if(title =="Music-Lyrics"){
    $("#musicPage").addClass("active");
    }
}
