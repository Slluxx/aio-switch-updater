#include "JC_color_swapper.hpp"
#include <iomanip>
#include <string>
#include <fstream>
#include <sstream>
#include <filesystem>
#include <tuple>

#include "constants.hpp"
#include "progress_event.hpp"
#include "utils.hpp"

using json = nlohmann::json;

int hexToBGR(std::string hex){
    std::string R = hex.substr(0, 2);
    std::string G = hex.substr(2, 2);
    std::string B = hex.substr(4, 2);
    return std::stoi(B + G + R, 0, 16);
}

std::string BGRToHex(int v){
    std::stringstream ss;
    v = ((v & 0xFF) << 16) + (v & 0xFF00) + (v >> 16) + 256;
    ss << std::setfill('0') << std::setw(6) << std::right << std::hex << v;
    return ss.str();
}

bool isHexaAnd3Bytes(std::string str){
    if(str.size()!=6) return false;
    for(char const &c : str){
        if(!isxdigit(c)) return false;
    }
    return true;
}

int setColor(std::vector<int> colors){
    Result pads, ljc, rjc;
    int res = 0;
    s32 nbEntries;
    HidsysUniquePadId UniquePadIds[2] = {};

    pads = hidsysGetUniquePadsFromNpad(HidNpadIdType_Handheld, UniquePadIds, 2,&nbEntries);
    if(R_SUCCEEDED(pads)){
        ljc = hiddbgUpdateControllerColor(colors[0], colors[1], UniquePadIds[0]);
        if (R_FAILED(ljc)) res +=1;
        rjc = hiddbgUpdateControllerColor(colors[2], colors[3], UniquePadIds[1]);
        if (R_FAILED(rjc)) res +=2;
    }
    else{
        res +=4;
    }
    return res;
}

int backupToJSON(json &profiles, const char* path){
    HidNpadControllerColor color_left;
    HidNpadControllerColor color_right;
    Result res = hidGetNpadControllerColorSplit(HidNpadIdType_Handheld, &color_left, &color_right);
    std::vector<int> oldBackups;
    if (R_SUCCEEDED(res)) {
        int i = 0;
        for (const auto& x : profiles.items()){
            if(x.value()["name"] == "_backup") {
                oldBackups.push_back(i);
            }
            i++;
        }
        for (auto &k : oldBackups){
            profiles.erase(profiles.begin() + k);
        }
        json newBackup = json::object({
            {"name", "_backup"},
            {"L_JC", BGRToHex(color_left.main)},
            {"L_BTN", BGRToHex(color_left.sub)},
            {"R_JC", BGRToHex(color_right.main)},
            {"R_BTN", BGRToHex(color_right.sub)}
        });
        profiles.push_back(newBackup);
        writeJSONToFile(profiles, path);
        return 0;
    }
    else{
        return -1;
    }
}

json backupProfile(){
    json newBackup;
    HidNpadControllerColor color_left;
    HidNpadControllerColor color_right;
    Result res = hidGetNpadControllerColorSplit(HidNpadIdType_Handheld, &color_left, &color_right);
    if (R_SUCCEEDED(res)) {
        newBackup = json::object({
            {"name", "_backup"},
            {"L_JC", BGRToHex(color_left.main)},
            {"L_BTN", BGRToHex(color_left.sub)},
            {"R_JC", BGRToHex(color_right.main)},
            {"R_BTN", BGRToHex(color_right.sub)}
        });
    }
    return newBackup;

}

void writeJSONToFile(json &profiles, const char* path){
    std::fstream newProfiles;
    newProfiles.open(path, std::fstream::out | std::fstream::trunc);
    newProfiles << std::setw(4) << profiles << std::endl;
    newProfiles.close();
}

std::tuple<std::vector<std::string>, std::vector<std::vector<int>>> getProfiles(const char* path){
    std::vector<std::string> names;
    std::vector<std::vector<int>> colorValues;
    bool properData;
    std::fstream profilesFile;
    json profilesJson;
    if(std::filesystem::exists(path)){
        profilesFile.open(path, std::fstream::in);
        profilesFile >> profilesJson;
        profilesFile.close();
    }
    if(profilesJson.empty()){
        profilesJson = {{
            {"L_BTN", "0A1E0A"},
            {"L_JC", "82FF96"},
            {"R_BTN", "0A1E28"},
            {"R_JC", "96F5F5"},
            {"name", "Animal Crossing: New Horizons"}
        }};
        writeJSONToFile(profilesJson, path);
    }
    for (const auto& x : profilesJson.items()){
        std::string name = x.value()["name"];
        std::vector<std::string> values = {
            std::string(x.value()["L_JC"]),
            std::string(x.value()["L_BTN"]),
            std::string(x.value()["R_JC"]),
            std::string(x.value()["R_BTN"])
        };
        properData = true;
        for(auto& str : values){
            if(!isHexaAnd3Bytes(str)){
                properData = false;
            }
        }
        if(properData){
            if(name == "") name = "Unamed";
            names.push_back(name);
            colorValues.push_back({
                hexToBGR(values[0]),
                hexToBGR(values[1]),
                hexToBGR(values[2]),
                hexToBGR(values[3])
            });
        }
    }
    return std::make_tuple(names, colorValues);
}

void changeJCColor(std::vector<int> values){
    hiddbgInitialize();
    hidsysInitialize();
    ProgressEvent::instance().reset();
    ProgressEvent::instance().setStep(1);
    int res = setColor(values);
    if(res != 0){
        showDialogBox("Could not change the Joy-Cons color. Make sure they're docked and try again.\nError :" + std::to_string(res), "Ok");
    }
    hiddbgExit();
    hidsysExit();
    ProgressEvent::instance().setStep(ProgressEvent::instance().getMax());
}

void backupJCColor(const char* path){
    hiddbgInitialize();
    hidsysInitialize();
    ProgressEvent::instance().reset();
    ProgressEvent::instance().setStep(1);
    json backup;
    json profiles;
    std::fstream profilesFile;
    if(std::filesystem::exists(path)){
        profilesFile.open(path, std::fstream::in);
        profilesFile >> profiles;
        profilesFile.close();
    }

    std::vector<int> oldBackups;
    int i = 0;
    for (const auto& x : profiles.items()){
        if(x.value()["name"] == "_backup") {
            oldBackups.push_back(i);
        }
        i++;
    }
    for (auto &k : oldBackups){
        profiles.erase(profiles.begin() + k);
    }

    while(backup.empty()){
        backup = backupProfile();
    }

    profiles.push_back(backup);
    //backup.push_back(profiles);
    writeJSONToFile(profiles, path);
    hiddbgExit();
    hidsysExit();
    ProgressEvent::instance().setStep(ProgressEvent::instance().getMax());
}