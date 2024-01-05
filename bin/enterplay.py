# -*- coding: utf-8 -*-
# !/usr/bin/env python3

__author__ = "Vicentini Tommaso"
__version__ = "04.03"

import csv
import keyboard
import os
import platform
import time
from pygame import mixer


in_songfile = ".\\playlist.csv"
path_songs = ".\\tracks\\"
line_limit = 0
line_margin = 0
printime = True

if line_limit//2 <= line_margin:
    if line_limit % 2 == 0:
        line_margin = (line_limit//2) - 1 
    else:
        line_margin = (line_limit//2) 


class bcolors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


def init_files(file_ck, file_name):
    """
    check if there are any files needed to boot
    :param file_ck: file to check if exist
    :param file_name: the name to print when crated
    :return: 0
    """
    if str(os.path.exists(file_ck)) == "False":
        with open(file_ck, "a", encoding="utf-8") as f_link:
            f_link.close()
        print(f"""{file_name} FILE doesn't exist, just created""")
    return 0


def init_directory(dir_ck, dir_vsby, dir_name):
    """
    check if there are any dirs needed to boot
    :param dir_ck: directory to check if exist
    :param dir_vsby: if directory is visible or not (any str/h)
    :param dir_name: the name to print when crated
    :return: 0
    """
    if str(os.path.exists(dir_ck)) == "False":
        os.mkdir(dir_ck)
        msg = f"""{dir_name} DIRECTORY doesn't exist, just created"""
        if dir_vsby == "h":
            os.system(f"""attrib +h {dir_ck}""")
            msg = msg + " and hidden"
        print(msg)
    return 0


def os_ril():
    """
    legge il sistema operativo e ritona la stringa del comando "clear" del sistema operativo usato
    :return: cls_opsys
    """
    try:
        if platform.system() == "Windows":
            cls_opsys = "cls"
        elif platform.system() == "Darwin":
            cls_opsys = "clear"
        elif platform.system() == "Linux":
            cls_opsys = "clear"
    except:
        cls_opsys = ""
    return cls_opsys


def read_in(t_in_songfile):
    """
    legge il file di input ritonando i vetori del comando, livello_audio, suono
    :t_in_songfile: file di input
    :return: [t_command, t_lvl_audiorfade, t_song, t_channel, t_n_channels]
    """
    t_command = []
    t_lvl_audiorfade = []
    t_song = []
    t_channel = []
    t_n_channels = 0
    
    with open(t_in_songfile, "r", encoding="utf-8") as in_song:
        for i in list(csv.reader(in_song)):
            try:
                t_command.append(i[0])
                t_song.append(i[-1])
                if len(i) >= 3:
                    t_lvl_audiorfade.append(lvltracks(i[0], i[1]))
                if len(i) == 4:
                    t_channel.append(i[2])
            except IndexError:
                pass
        in_song.close()

        if t_channel == []:
            for i in t_command:
                t_channel.append("0")
        else:
            for i in range(0, len(t_channel)):
                if t_channel[i] == "":
                    t_channel[i] = "0"
        for i in range(0, len(t_channel)):
            if int(t_channel[i]) > t_n_channels:
                t_n_channels = int(t_channel[i])
        t_n_channels += 1
        if t_n_channels > 6:
            t_n_channels = 6
    return [t_command, t_lvl_audiorfade, t_song, t_channel, t_n_channels]


def lvltracks(t_cmd, t_str_lvl):
    """
    da il valore corretto dopo averlo ricevuto da 1 a 10
    se viene inserita qualsiasi altra strinaga il valore è 10
    :t_cmd: il comando della traccia audio
    :t_str_lvl:
    :return: il valore della tracia audio
    """
    if t_cmd == "PLAY" or t_cmd == "UNPA":
        if t_str_lvl == "01" or t_str_lvl == "1":
            return 0.1
        elif t_str_lvl == "02" or t_str_lvl == "2":
            return 0.2
        elif t_str_lvl == "03" or t_str_lvl == "3":
            return 0.3
        elif t_str_lvl == "04" or t_str_lvl == "4":
            return 0.4
        elif t_str_lvl == "05" or t_str_lvl == "5":
            return 0.5
        elif t_str_lvl == "06" or t_str_lvl == "6":
            return 0.6
        elif t_str_lvl == "07" or t_str_lvl == "7":
            return 0.7
        elif t_str_lvl == "08" or t_str_lvl == "8":
            return 0.8
        elif t_str_lvl == "09" or t_str_lvl == "9":
            return 0.9
        elif t_str_lvl == "10":
            return 1.0
        else:
            if t_cmd == "PLAY":
                return 1.0
            elif t_cmd == "UNPA":
                return ""
    elif t_cmd == "FOUT":
        return t_str_lvl
    else:
        return ""


def writecolor(t_operation):
    """
    assegna il colore alla scritta che viene data
    :t_operation: comando a cui dare colore di visualizzazione
    :return: Colore della scritta
    """
    if t_operation == "PLAY":
        return bcolors.OKGREEN
    elif t_operation == "PAUS":
        return bcolors.WARNING
    elif t_operation == "UNPA":
        return bcolors.OKCYAN
    elif t_operation == "STOP":
        return bcolors.FAIL
    elif t_operation == "FOUT":
        return bcolors.FAIL


def player(t_cmd, t_str_fadeout, t_track, t_channel):
    """
    esegue il comando sulla traccia
    :t_cmd: comando da eseguire
    :t_str_fadeout: valore in ms del fadeout
    :t_track: path file da riprodurre
    :t_channel: canale dove riprodurre la traccia
    :return: 0
    """
    if t_cmd == "PLAY":
        mixer.Channel(t_channel).play(mixer.Sound(t_track))
    elif t_cmd == "PAUS":
        mixer.Channel(t_channel).pause()
    elif t_cmd == "UNPA":
        mixer.Channel(t_channel).unpause()
    elif t_cmd == "STOP":
        mixer.Channel(t_channel).stop()
    elif t_cmd == "FOUT":
        mixer.Channel(t_channel).fadeout(int(t_str_fadeout))
    return 0


def grafic(t_i, t_line_limit, t_line_margin, t_songlist_print, t_cls_opsys, t_print_pos, t_underline_pos, moveorback):
    """
    interfaccia grafica del programma
    :t_i: INT posizione reale nella playlist
    :t_line_limit: INT righe da visualizzare a video
    :t_line_margin: INT numero di tracce che si vogliono visualizzare prima e dopo della traccia che verrà riprodotta
    :t_songlist_print: VETTORE lista delle canzoni
    :t_cls_opsys: STR stringa del comando per cancellare i precedennti print
    :t_print_pos: INT conteggio posizione da cui stampare a video
    :t_underline_pos: INT conteggio posizione linea sottolineata
    :moveorback: STR "+1", "-1" per sapere se manda avanti o indietro nella grafica
    :return: [t_print_pos, t_underline_pos]
    """
    if t_line_limit == 0:
        t_line_limit = len(t_songlist_print)
    if moveorback == "+1":
        if t_underline_pos != t_line_limit - (1 + t_line_margin):
            t_underline_pos += 1
        else:
            if len(t_songlist_print) - t_i <= line_margin + 1:
                t_underline_pos += 1
            else:
                t_print_pos += 1
            
    if moveorback == "-1":
        if t_underline_pos != 0 + t_line_margin:
            t_underline_pos -= 1
        else:
            if t_i <= line_margin:
                t_underline_pos -= 1
            else:
                t_print_pos -= 1
    os.system(t_cls_opsys)
    for f in range(0, t_line_limit):
        if t_underline_pos == f:
            print(str(bcolors.UNDERLINE + t_songlist_print[f + t_print_pos]))
        else:
            print(str(t_songlist_print[f + t_print_pos]))
    return [t_print_pos, t_underline_pos]


def main():
    """
    main
    :return: None
    """
    cmd_play = "space"
    cmd_next1 = "freccia giù"
    cmd_next2 = "freccia destra"
    cmd_prev1 = "freccia su"
    cmd_prev2 = "freccia sinistra"
    cmd_stop = "enter"

    init_files(in_songfile, "INPUT")
    init_directory(path_songs, "", "TRACKS")

    cls_opsys = os_ril()

    read_fin = read_in(in_songfile)
    command = read_fin[0]
    lvl_audiorfade = read_fin[1]
    song = read_fin[2]
    channel = read_fin[3]
    n_channels = read_fin[4]

    songlist_print = []
    for i in range(0, len(command)):
        color = writecolor(command[i])
        songlist_print.append(f"""{color}{command[i]} {song[i]}{bcolors.ENDC}""")

    mixer.pre_init(channels = n_channels)
    mixer.init()
    i = 0
    grafica = grafic(i, line_limit, line_margin, songlist_print, cls_opsys, 0, 0, "")
    while i < len(command):
        audiorfade = "0"
        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN and event.name == cmd_play:
            if command[i] == "PLAY":
                track = path_songs + song[i]
                if lvl_audiorfade != []:
                    mixer.Channel(int(channel[i])).set_volume(lvl_audiorfade[i])
                player(command[i], audiorfade, track, int(channel[i]))
            else:
                track = ""
                if command[i] == "UNPA" and lvl_audiorfade != [] and lvl_audiorfade[i] != "":
                    mixer.Channel(int(channel[i])).set_volume(lvl_audiorfade[i])
                if command[i] == "FOUT" and lvl_audiorfade != [] and lvl_audiorfade[i] != "":
                    audiorfade = lvl_audiorfade[i]
                player(command[i], audiorfade, track, int(channel[i]))

            if i != len(command)-1:
                grafica = grafic(i, line_limit, line_margin, songlist_print, cls_opsys, grafica[0], grafica[1], "+1")
                if command[i] == "PLAY" and printime:
                    print("\nDurata: ", time.strftime("%H:%M:%S", time.gmtime(mixer.Sound(track).get_length())))
                i += 1

        elif event.event_type == keyboard.KEY_DOWN and event.name == cmd_next1 or event.event_type == keyboard.KEY_DOWN and event.name == cmd_next2:
            if i != len(command)-1:
                grafica = grafic(i, line_limit, line_margin, songlist_print, cls_opsys, grafica[0], grafica[1], "+1")
                i += 1

        elif event.event_type == keyboard.KEY_DOWN and event.name == cmd_prev1 or event.event_type == keyboard.KEY_DOWN and event.name == cmd_prev2:
            if i != 0:
                grafica = grafic(i, line_limit, line_margin, songlist_print, cls_opsys, grafica[0], grafica[1], "-1")
                i -= 1
        elif event.event_type == keyboard.KEY_DOWN and event.name == cmd_stop:
            for f in range(0, n_channels):
                mixer.Channel(f).stop()

    return None


if __name__ == "__main__":
    main()
