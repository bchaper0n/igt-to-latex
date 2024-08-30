#include <iostream>
#include <string>
#include <algorithm>
#include <fstream>
#include <cstring>
using namespace std;

// no tones for now
char* igalaScripts[] = {"ẹ", "ọ", "py", "by", "kw", "gw", "fy", "my", "ny", "ng", "nw", "ñg" , "ñw", "ch", "j", "ly", "y"};
char* igalaIPAs[] = {"ɛ", "ɔ", "pʲ", "bʲ", "kʷ", "gʷ", "fʲ", "mʲ", "ɲ", "ŋ", "ŋʷ", "ŋ", "ŋʷ", "tʃ", "ʤ", "lʲ", "j"};

string ScriptToIPA(char* igalaScript){

    string igalaIPA;
    char* buffer;

    int len = strlen(igalaScript);

    buffer = new char[len];

    const char* igalaScriptStart;
    char* igalaIPAStart;

    int len;
    int old_len;
    int new_len;

    for(int i = 0; i < sizeof(igalaIPAs); i++){

        old_len = strlen(igalaScripts[i]);
        new_len = strlen(igalaIPAs[i]);

        igalaScriptStart = strstr(igalaScript, igalaScripts[i]);
        igalaIPAStart = buffer;

        // copy part of input string before old substring
        memcpy(igalaIPAStart, igalaScripts[i], igalaScriptStart - igalaScripts[i]);
        igalaIPAStart += igalaScriptStart - igalaScripts[i];

        // copy new substring
        memcpy(igalaIPAStart, igalaIPAs[i], new_len);
        igalaIPAStart += new_len;

        memcpy(igalaIPAStart, igalaScriptStart + old_len, len - (igalaScriptStart - igalaScripts[i] + old_len));
    
        //igalaIPA = replace(igalaScript.begin(), igalaScript.end(), igalaScripts[i], igalaIPAs[i]);
    }

    return igalaIPA;
}

extern "C" {
    string script_to_IPA(string igalaScript);
}