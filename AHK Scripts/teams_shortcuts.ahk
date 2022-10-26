#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.

SetDefaultMouseSpeed, 0
#IfWinActive ahk_exe Teams.exe
!a::
SysGet, Mon, Monitor
if (MonRight != 1920) {
MouseGetPos, xpos, ypos
Click, 1163, 79
MouseMove, xpos, ypos
return
} else {
MouseGetPos, xpos, ypos
Click, 1707, 68
MouseMove, xpos, ypos
return
}

!v::
SysGet, Mon, Monitor
if (MonRight != 1920) {
MouseGetPos, xpos, ypos
Click, 1112, 77
MouseMove, xpos, ypos
return
} else {
MouseGetPos, xpos, ypos
Click, 1657, 64
MouseMove, xpos, ypos
return
}

!q::
SysGet, Mon, Monitor
if (MonRight != 1920) {
MouseGetPos, xpos, ypos
Click, 1289, 71
MouseMove, xpos, ypos
return
} else {
MouseGetPos, xpos, ypos
Click, 1849, 61
MouseMove, xpos, ypos
return
}

!m::
SysGet, Mon, Monitor
if (MonRight != 1920) {
MouseGetPos, xpos, ypos
Click, 936, 75
MouseMove, xpos, ypos
return
} else {
MouseGetPos, xpos, ypos
Click, 1489, 65
MouseMove, xpos, ypos
return
}

!p::
SysGet, Mon, Monitor
if (MonRight != 1920) {
MouseGetPos, xpos, ypos
Click, 889, 72
MouseMove, xpos, ypos
return
} else {
MouseGetPos, xpos, ypos
Click, 1441, 65
MouseMove, xpos, ypos
return
}

^+h::
SysGet, Mon, Monitor
if (MonRight != 1920) {
MouseGetPos, xpos, ypos
MouseMove, 986, 73
Sleep, 700
Click, 932, 115
MouseMove, xpos, ypos
return
} else {
MouseGetPos, xpos, ypos
MouseMove, 1538, 62
Sleep, 700
Click, 1488, 111
MouseMove, xpos, ypos
return
}

!h::
SysGet, Mon, Monitor
if (MonRight != 1920) {
MouseGetPos, xpos, ypos
MouseMove, 986, 73
Sleep, 700
Click, 984, 114
MouseMove, xpos, ypos
return
} else {
MouseGetPos, xpos, ypos
MouseMove, 1538, 62
Sleep, 700
Click, 1537, 113
MouseMove, xpos, ypos
return
}

^+t::
SysGet, Mon, Monitor
if (MonRight != 1920) {
MouseGetPos, xpos, ypos
MouseMove, 986, 73
Sleep, 700
Click, 828, 127
MouseMove, xpos, ypos
return
} else {
MouseGetPos, xpos, ypos
MouseMove, 1538, 62
Sleep, 700
Click, 1373, 114
MouseMove, xpos, ypos
return
}

^+c::
SysGet, Mon, Monitor
if (MonRight != 1920) {
MouseGetPos, xpos, ypos
MouseMove, 986, 73
Sleep, 700
Click, 895, 113
MouseMove, xpos, ypos
return
} else {
MouseGetPos, xpos, ypos
MouseMove, 1538, 62
Sleep, 700
Click, 1448, 113
MouseMove, xpos, ypos
return
}

!g::
SysGet, Mon, Monitor
if (MonRight != 1920) {
Click, 1033, 69
Sleep, 700
Click, 1118, 227
Click, 1365, 451
return
} else {
Click, 1587, 67
Sleep, 700
Click, 1118, 227
Click, 1365, 451
return
}

!l::
Click, 1033, 69
Sleep, 700
Click, 1131, 258
Click, 1365, 451
return

!f::
Click, 1033, 69
Sleep, 700
Click, 1134, 336
Click, 1365, 451
return

!d::
MouseGetPos, xpos, ypos
Click, 1163, 24
Sleep, 3000
Click, 1172, 248
PixelGetColor, hcon_col, 912, 170
while hcon_col != 0x000000 {
PixelGetColor, hcon_col, 912, 170
}
PixelGetColor, bg_col, 427, 446
if (bg_col == 0x272727) {
Click, 592, 159
PixelGetColor, bg_col, 427, 446
while bg_col != 0xFEFEFE {
PixelGetColor, bg_col, 427, 446
}
} else {
Click, 754, 172
PixelGetColor, bg_col, 427, 446
while bg_col != 0x282828 {
PixelGetColor, bg_col, 427, 446
}
}
Click, 1049, 36
MouseMove, xpos, ypos
return