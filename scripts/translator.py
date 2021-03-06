import json

lookupTable = {
    "About_Title" : ["about", "title"],
    "copyright" : ["about", "copyright"],
    "Disclaimers" : ["about", "disclaimers"],
    "donate" : ["about", "donate"],
    "app_title" : ["cheats", "installed"],
    "app_label" : ["cheats", "label"],
    "text_download" : ["cheats", "downloading"],
    "text_download_list" : ["cheats", "dl_latest"],
    "text_title": ["cheats", "getting_cheats"],
    "Downloading" : ["common", "downloading"],
    "tool_extracting" : ["common", "extracting"],
    "Extracting" : ["common", "extracting"],
    "All_done" : ["common", "all_done"],
    "Changelog" : ["changelog", "changelog"],
    "cheat_menu" : ["cheats", "menu"],
    "cheat_view" : ["cheats", "view"],
    "cheat_exclude" : ["cheats", "exclude"],
    "cheat_delete_all_ex" : ["cheats", "delete_existing"],
    "cheat_delete_all_cheat" : ["cheats", "delete_all"],
    "cheat_Deleting" : ["cheats", "deleting"],
    "cheat_All_done" : ["common", "all_done"],
    "please_reboot" : ["sigpatches", "reboot"],
    "cheastlips_title" : ["cheats", "cheastlips_title"],
    "get_cheatslips" : ["cheats", "get_cheatslips"],
    "cheatslips_label" : ["cheats", "cheatslips_label"],
    "download_cheatslips" : ["cheats", "cheatslips_dl"],
    "delete_cheat" : ["cheats", "delete_file"],
    "couldnt_dl_cheats" : ["cheats", "cheatslips_error"],
    "quota_cheatslips" : ["cheats", "quota"],
    "cheat_cheat_content" : ["cheats", "sheet_content"],
    "app_cheatslips_label" : ["cheats", "cheatslips_select"],
    "wrong_cheatslips_id" : ["cheats", "cheatslips_wrong_id"],
    "keyboard_no_show" : ["cheats", "kb_error"],
    "see_more" : ["cheats", "cheatslips_see_more"],
    "download_cheats" : ["cheats", "cheatslips_dl_cheats"],
    "bid_not_found" : ["cheats", "bid_not_found"],
    "choice_yes": ["common", "Yes"],
    "choice_no": ["common", "No"],
    "Back" : ["common", "back"],
    "Continue" : ["common", "continue"],
    "Download_payloads" : ["payloads", "dl_payloads"],
    "select" : ["payloads", "select"],
    "Download" : ["common", "download"],
    "from" : ["common", "from"],
    "down" : ["common", "downloading"],
    "download_all_done" : ["common", "all_done"],
    "description" : ["payloads", "not_found"],
    "back" : ["common", "back"],
    "exclude_titles" : ["cheats", "exclude_titles"],
    "you_can" : ["cheats", "exclude_titles_desc"],
    "save" : ["cheats", "exclude_titles_save"],
    "joy_con" : ["joy_con", "title"],
    "jc_you_can_1" : ["joy_con", "desc_1"],
    "jc_you_can_goto" : ["joy_con", "desc_2"],
    "jc_you_can_2" : ["joy_con", "desc_3"],
    "jc_backup" : ["joy_con", "backup"],
    "jc_color" : ["joy_con", "label"],
    "jc_backing" : ["joy_con", "backing_up"],
    "jc_all_done" : ["common", "all_done"],
    "jc_change" : ["joy_con", "changing"],
    "jc_all_" : ["joy_con", "all_done"],
    "pro_con" :  ["pro_con", "title"],
    "pc_you_can" : ["pro_con", "desc"],
    "pc_color" : ["pro_con", "label"],
    "pc_backing" : ["pro_con", "backing_up"],
    "pc_all_done" : ["pro_con", "all_done"],
    "Getting" : ["main", "getting"],
    "firmware_text" : ["main", "firmware_text"],
    "currentCeatsver" : ["main", "cheats_text"],
    "operation_1" : ["main", "sigpatches"],
    "list_sigpatches" : ["main", "sigpatches_text"],
    "operation_2" : ["main", "firmware"],
    "list_not" : ["main", "not_found"],
    "list_latest" : ["main", "latest_cheats"],
    "list_app" : ["main", "app"],
    "list_cfw" : ["main", "cfw"],
    "list_ams": ["main", "ams_text"],
    "list_main" : ["main", "cfw_text"],
    "list_latest_ver" : ["main", "cheats_text"],
    "list_cheats" : ["main", "cheats"],
    "list_down" : ["common", "download"],
    "list_from" : ["common", "from"],
    "list_downing" : ["common", "downloading"],
    "list_extracting" : ["common", "extracting"],
    "list_All" : ["common", "all_done"],
    "list_could_done" : ["main", "links_not_found"],
    "main_app" : ["main", "new_update"],
    "main_about" : ["main", "about"],
    "main_update_ams" : ["main", "update_ams"],
    "main_update_cfw" : ["main", "update_cfw"],
    "main_update_si" : ["main", "update_sigpatches"],
    "main_firmwares" : ["main", "download_firmware"],
    "main_cheats" : ["main", "download_cheats"],
    "main_tools" : ["main", "tools"],
    "payload_reboot" : ["payloads", "reboot_title"],
    "payload_select" : ["payloads", "select"],
    "payload_set" : ["payloads", "set_reboot_payload"],
    "payload_set_up" : ["payloads", "set_update_bin"],
    "payload_success" : ["payloads", "copy_success"],
    "payload_to" : ["payloads", "to"],
    "payload_ok" : ["common", "ok"],
    "payload_shut" : ["common", "shut_down"],
    "payload_reboot_2" : ["common", "reboot"],
    "hide_tabs_page" : ["hide", "title"],
    "hide_tabs_label" : ["hide", "desc"],
    "tool_cheats" : ["tools", "cheats"],
    "tool_change" : ["tools", "joy_cons"],
    "tool_change_procon" : ["tools", "pro_cons"],
    "tool_download" : ["tools", "dl_payloads"],
    "tool_inject" : ["tools", "inject_payloads"],
    "tool_update" : ["tools", "update_app"],
    "tool_DownLoad" : ["tools", "dl_app"],
    "tool_updating" : ["common", "updating"],
    "tool_downloading" : ["common", "downloading"],
    "tool_all_done" : ["common", "all_done"],
    "tool_changelog" : ["tools", "changelog"],
    "tool_cleanUp" : ["tools", "clean_up"],
    "hide_tabs" : ["tools", "hide_tabs"],
    "tool_net_settings" : ["tools", "internet_settings"],
    "tool_browser" : ["tools", "browser"],
    "utils_because" : ["utils", "fw_warning"],
    "utils_ok" : ["common", "ok"],
    "utils_do" : ["utils", "overwrite"],
    "utils_no" : ["common", "no"],
    "utils_yes" : ["common", "yes"],
    "utils_the" : ["utils", "wrong_type_sigpatches"],
    "utils_the_downloaded" : ["utils", "wrong_type_fw"],
    "ultils_overwrite" : ["utils", "overwrite_inis"],
    "ultis_file" : ["utils", "wrong_type_cfw"],
    "reboot_rcm" : ["ams_update", "reboot_rcm"],
    "hekate_dialogue" : ["ams_update", "install_hekate"],
    "Yes" : ["common", "yes"],
    "No" : ["common", "no"],
    "net_settings" : ["net", "title"],
    "go_back" : ["common", "go_back"],
    "Confirm_button" : ["common", "confirm"],
    "Cancel_button" : ["common", "cancel"],
    "tool_copyFiles" : ["tools", "batch_copy"],
    "files_not_found" : ["tools", "batch_copy_not_found"],
    "copy_files_not_found" : ["tools", "batch_copy_config_not_found"],
    "delete_contents" : ["ams_update", "delete_contents"],
    "launch_warning" : ["main", "launch_warning"]
}

lookupTableSmol = {
    "About_Title" : ["about", "title"],
    "copyright" : ["about", "copyright"],
    "Disclaimers" : ["about", "disclaimer"]
}

with open('menus.json') as json_file: 
    data = json.load(json_file) 

def populate(data, t):
    res = {}
    for e in t:
        if(e in data):
            if(t[e][0] not in res):
                res[t[e][0]] = {}
            res[t[e][0]][t[e][1]] = data[e]
    return res

def sed_command(t):
    command = "'"
    for e in t:
        command += "s#" + "menus/" + e + "#" + "menus/" + t[e][0] + "/" + t[e][1] + "#g;"
    command += command[:-1] + "'"
    return command

with open("menus.json", "w") as outfile:
    json.dump(populate(data, lookupTable), outfile, ensure_ascii=False, indent=2)

print(sed_command(lookupTable))