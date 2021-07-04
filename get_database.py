import os
"""
    Will get all the files in music directory and create a database.js in js folder
    How to run it:
        python ./get_database.py    
"""
babies = [
    "andrea_bocelli-the_prayer.html",
    "anne_marie-heavy.html",
    "celtic_woman-ave_maria.html",
    "daya-safe.html",
    "enya-marble_halls.html",
    "glee-like_a_prayer.html",
    "halsey-without_me.html",
    "hozier-take_me_to_church.html",
    "ilene_woods-a_dream_is_a_wish_your_heart_makes.html",
    "linkin_park-in_the_end.html",
    "linkin_park-numb.html",
    "phantom_of_the_opera-all_i_ask_of_you.html",
    "sarah_mclachlan-adia.html",
    "sarah_mclachlan-fallen.html",
    "sarah_mclachlan-sweet_surrender.html",
    "sia-chandelier.html",
    "the_greatest_showman_loren_allred-never_enough.html",
    "the_weeknd-save_your_tears.html",
    "tori_kelly-dont_you_worry_about_a_thing.html",
    "tori_kelly-hallelujah.html",
    "wizard_of_oz-somewhere_over_the_rainbow.html",
    "celtic_woman-ave_maria_sancta.html",
    "pia_mia_twocolors-lovefool.html",
    "katy_perry-firework.html",
    "disney-tangled_when_will_my_life_begin.html",
    "ariana_grande-ghostin.html",
    "nicole_scherzinger-dont_cry_for_me_argentina.html",
    "pia_toscano-all_by_myself.html",
    "tate_mcrae-you_broke_me_first.html",
    "ava_max-my_head_my_heart.html",
    "frou_frou-let_go.html",
    "lorde-buzzcut_season.html",
    "dido-life_for_rent.html",
    "dido-white_flag.html",
    "dido-thank_you.html",
    "dido-this_land_is_mine.html",
    "dido-sand_in_my_shoes.html",
    "dido-dont_leave_home.html",
    "astrid-its_okay_if_you_forget_me.html",
    "astrid-hurts_so_good.html",
    "charlotte_lawrence-jokes_on_you.html",
    "billie_eilish-bellyache.html",
    "kacey_musgraves-butterflies.html",
    "kacey_musgraves-oh_what_a_world.html",
    "chairlift-bruises.html",
    "billie_eilish-bored.html",
    "lauren_daigle-you_say.html",
    "evanescence-going_under.html",
    "my_chemical_romance-im_not_okay.html",
    "calvin_harris-sweet_nothing.html",
    "alan_walker-faded.html",
    "glee-its_all_coming_back.html",
    "sia-elastic_heart.html",
    "phantom_of_the_opera-think_of_me.html",
    "charlotte_lawrence-cold_as_stone.html",
    "hailee_steinfeld-let_me_go.html",
    "zara_larsson-i_cant_fall_in_love_without_you.html",
    "halsey-now_or_never.html",
    "halsey-sorry.html",
    "hailee_steinfeld-starving.html",
    "elohim-sleepy_eyes.html",
    "chainsmokers-kanye.html",
]

potatos = [
    "andrea_bocelli-the_prayer.html",
    "hozier-take_me_to_church.html",
    "linkin_park-in_the_end.html",
    "linkin_park-numb.html",
    "phantom_of_the_opera-all_i_ask_of_you.html",
    "the_weeknd-save_your_tears.html",
    "joan_osborne-one_of_us.html",
    "michael_smith-awesome_god.html",
    "aha-take_on_me.html",
    "chris_brown-yeah_3x.html",
    "chris_brown-dont_wake_me_up.html",
    "alphaville-forever_young.html",
    "the_weeknd-blinding_lights.html",
    "coldplay-yellow.html",
    "disney-hercules_go_the_distance.html",
    "disney-aladdin a whole new world.html",
    "disney-mulan_ill_make_a_man_out_of_you.html",
    "disney-tarzan_youll_be_in_my_heart .html",
    "disney-tangled_i_see_the_light.html",
    "troye_sivan_ariana_grande-dance_to_this.html",
    "bruno_mars-leave_the_door_open.html",
    "justin_bieber-sorry.html",
    "post_malone-white_iverson.html",
    "coldplay-scientitst.html",
    "coldplay-clocks.html",
    "coldplay-speed_of_sound.html",
    "post_malone-circles.html",
    "incubus-stellar.html",
    "ncubus-drive.html",
    "lewis_capaldi-someone_you_loved.html",
    "lewis_capaldi-before_you_go.html",
    "my_chemical_romance-im_not_okay.html",
    "citizen_cope-sideways.html",
    "harry_styles-watermelon_sugar.html",
]
def make_file_database():
    os.chdir("music")
    os.system(r'dir /b > ../file.txt')
    file_name = r'../file.txt'
    file = open(file_name,"r")
    database = 'const database = [ \n'
    counter = 0
    filled = False
    for item in file:
        # print(item.rstrip())
        item_title = item.rstrip()
        database += "{title" + ': "'+ item_title +'"'
        for baby in babies:
            if baby in item_title:
                if baby in potatos:
                    database += ", user: "+'"both"},\n'
                    filled = True
                    break
                else:
                    database += ", user: "+'"baby"},\n'
                    filled = False
                    break
            # if baby in potatos:
            #     database += ", user: "+'"both"},\n'
            #     break
        for potato in potatos:
            if filled == True:
                break
            elif potato in item_title:
                database += ", user: "+'"potato"},\n'
                break
        counter += 1
    database += ']\nexport function myDatabase(){return database;}'
    # print(database)
    file_write = open("../js/database.js","w")
    file_write.write(database)
    file.close()
    os.remove(file_name)


if __name__ == '__main__':
    make_file_database()
