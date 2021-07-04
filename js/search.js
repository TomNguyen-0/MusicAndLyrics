import { myDatabase } from './database.js';

function create_link(html_title){
    var title = html_title.replace(/_/g, ' ');
    title = title.replace(/.html/g, '');
    title = title.replace(/-/g, ' - ');
    var link_url = `
    <p><a class="a-link-title" href="./music/${html_title}">${title}</a></p>
    `;// <p><a class="a-link-title" href="./music/andrea_bocelli-the_prayer.html">andrea bocelli - the prayer</a></p>
    return link_url;
}

function mySearch() { //link isnt showing up
    var syntax = "";
    $(".search-result").html(syntax);

    var search_word_txt = $("#petSearchServiceTxt")[0]; // same as: var search_word_txt = document.getElementById("petSearchServiceTxt");
    search_word_txt = search_word_txt.value;
    // console.log(search_word_txt);
    search(search_word_txt, ".search-result");
    $('#petSearchServiceTxt').val('');
}

function search(key_word, id_name){
    var database = myDatabase();
    var syntax = "";
    var db_title = "";
    // $(".baby-music").html('');
    // console.log(key_word);
    for (var i = 0; i < database.length ; i++){
        db_title = database[i].title.toLowerCase();
        db_title = db_title.replace(/_|-|.html/g, ' ');
        if (db_title.includes(key_word.toLowerCase())){
            // console.log(db_title);
            syntax = create_link(database[i].title);
            $(id_name).append(syntax);
        }
    }
}

function mySearchDisplay(section_id){
    $(section_id).html('');
    // $(".search-result").html('');
    // $(".baby-music").html('');
    var search_word_txt = $("#petSearchServiceTxt")[0].value;
    // search(search_word_txt, ".search-result");
    search(search_word_txt, section_id);
}

function initSearch() {
    navbar();
    var title=document.title;
    if (title === "Home"){
        $('button').click(mySearch);
        $('#petSearchServiceTxt').keydown(function(){
            mySearchDisplay(".search-result");
        });
        
        $('#petSearchServiceTxt').keypress(function(e){
            //console.log(e.key);
            if(e.key==="Enter"){
                mySearch();

            }
        });  
    }
}

window.onload=initSearch;
export { mySearchDisplay,mySearch, create_link };