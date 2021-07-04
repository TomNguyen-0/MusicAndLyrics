import { myDatabase } from './database.js';
import { mySearchDisplay, mySearch, create_link } from './search.js';

function display_menu(username, section_id){
    var database = myDatabase();
    for (var i = 0; i < database.length ; i++){
        var user = database[i].user;

        if ( user == username || user == "both" ){
            var title = database[i].title;
            var syntax = create_link(title)
            $(section_id).append(syntax);
        }
    }
}


function init(){
    navbar();
    var section_id = ".baby-music";
    var user = "baby";
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

export { display_menu };