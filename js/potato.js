import { mySearchDisplay, mySearch } from './search.js';
import { display_menu } from './music.js';


function init(){
    navbar();
    var section_id = ".potato-music";
    var user = "potato";
    // initSearch();
    display_menu(user, section_id);
    $('#petSearchServiceTxt').keydown(function(){
        mySearchDisplay(section_id);
    });
    $('button').click(mySearch);

    $('#petSearchServiceTxt').keypress(function(e){
        //console.log(e.key);
        if(e.key==="Enter"){
            if($('#petSearchServiceTxt')[0].value == ""){
                display_menu(user, section_id)
                // $(".search-result").html(''); // if you dont want the last result to be there
            }else{
                mySearch();
            }
        }
    });  
}

window.onload=init;