#NoTrayIcon
#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.
SetTitleMatchMode, 2

SetDefaultMouseSpeed, 0
#If WinActive("Unacademy" "ahk_exe msedge.exe")
!1::
SysGet, Mon, Monitor
if (MonRight != 1920) {
MouseMove, 1144, 726
Sleep, 500
Click, 1144, 726
Sleep, 500
PixelGetColor, dark_mode, 1325, 358
PixelGetColor, speed_color, 1117, 507
if (speed_color == dark_mode) {
MouseMove, 1144, 470
Sleep, 500
Click, 1144, 470
} else {
MouseMove, 1144, 430
Sleep, 500
Click, 1144, 430
}
Sleep, 500
Click, 1144, 474
Sleep, 250
Click, 1144, 540
Click, 1291, 294
Send, k
Sleep 250
Send, k
return
} else {
MouseMove, 1731, 1028
Sleep, 50
Click, 1731, 1028
Sleep, 200
Click, 1731, 730
Sleep, 200
Click, 1731, 797
Sleep, 100
Click, 1825, 404
Send, k
Sleep, 100
Send, k
return
}

!2::
SysGet, Mon, Monitor
if (MonRight != 1920) {
MouseMove, 1144, 726
Sleep, 500
Click, 1144, 726
Sleep, 500
PixelGetColor, dark_mode, 1325, 358
PixelGetColor, speed_color, 1117, 507
if (speed_color == dark_mode) {
MouseMove, 1144, 470
Sleep, 500
Click, 1144, 470
} else {
MouseMove, 1144, 430
Sleep, 500
Click, 1144, 430
}
Sleep, 500
Click, 1144, 527
Sleep, 250
Click, 1144, 540
Click, 1291, 294
Send, k
Sleep 250
Send, k
return
} else {
MouseMove, 1731, 1028
Sleep, 50
Click, 1731, 1028
Sleep, 200
Click, 1731, 730
Sleep, 200
Click, 1731, 836
Sleep, 100
Click, 1825, 404
Send, k
Sleep, 100
Send, k
return
}

!3::
SysGet, Mon, Monitor
if (MonRight != 1920) {
MouseMove, 1144, 726
Sleep, 500
Click, 1144, 726
Sleep, 500
PixelGetColor, dark_mode, 1325, 358
PixelGetColor, speed_color, 1117, 507
if (speed_color == dark_mode) {
MouseMove, 1144, 470
Sleep, 500
Click, 1144, 470
} else {
MouseMove, 1144, 430
Sleep, 500
Click, 1144, 430
}
Sleep, 500
Click, 1144, 567
Sleep, 250
Click, 1144, 540
Click, 1291, 294
Send, k
Sleep 250
Send, k
return
} else {
MouseMove, 1731, 1028
Sleep, 50
Click, 1731, 1028
Sleep, 200
Click, 1731, 730
Sleep, 200
Click, 1731, 868
Sleep, 100
Click, 1825, 404
Send, k
Sleep, 100
Send, k
return
}

!4::
SysGet, Mon, Monitor
if (MonRight != 1920) {
MouseMove, 1144, 726
Sleep, 500
Click, 1144, 726
Sleep, 500
PixelGetColor, dark_mode, 1325, 358
PixelGetColor, speed_color, 1117, 507
if (speed_color == dark_mode) {
MouseMove, 1144, 470
Sleep, 500
Click, 1144, 470
} else {
MouseMove, 1144, 430
Sleep, 500
Click, 1144, 430
}
Sleep, 500
Click, 1144, 601
Sleep, 250
Click, 1144, 540
Click, 1291, 294
Send, k
Sleep 250
Send, k
return
} else {
MouseMove, 1731, 1028
Sleep, 50
Click, 1731, 1028
Sleep, 200
Click, 1731, 730
Sleep, 200
Click, 1731, 912
Sleep, 100
Click, 1825, 404
Send, k
Sleep, 100
Send, k
return
}

!5::
SysGet, Mon, Monitor
if (MonRight != 1920) {
MouseMove, 1144, 726
Sleep, 500
Click, 1144, 726
Sleep, 500
PixelGetColor, dark_mode, 1325, 358
PixelGetColor, speed_color, 1117, 507
if (speed_color == dark_mode) {
MouseMove, 1144, 470
Sleep, 500
Click, 1144, 470
} else {
MouseMove, 1144, 430
Sleep, 500
Click, 1144, 430
}
Sleep, 500
Click, 1144, 640
Sleep, 250
Click, 1144, 540
Click, 1291, 294
Send, k
Sleep 250
Send, k
return
} else {
MouseMove, 1731, 1028
Sleep, 50
Click, 1731, 1028
Sleep, 200
Click, 1731, 730
Sleep, 200
Click, 1731, 950
Sleep, 100
Click, 1825, 404
Send, k
Sleep, 100
Send, k
return
}

!0::
SysGet, Mon, Monitor
if (MonRight != 1920) {
MouseMove, 1144, 726
Sleep, 500
Click, 1144, 726
Sleep, 500
PixelGetColor, dark_mode, 1325, 358
PixelGetColor, speed_color, 1117, 507
if (speed_color == dark_mode)
{
MouseMove, 1144, 470
Sleep, 500
Click, 1144, 470
} else {
MouseMove, 1144, 430
Sleep, 500
Click, 1144, 430
}
Sleep, 500
Click, 1144, 453
Sleep, 250
Click, 1144, 540
Click, 1291, 294
Send, k
Sleep 250
Send, k
return
} else {
MouseMove, 1731, 1028
Sleep, 50
Click, 1731, 1028
Sleep, 250
Click, 1731, 730
Sleep, 250
Click, 1731, 756
Sleep, 100
Click, 1825, 404
Sleep 250
Send, k
Sleep, 100
Send, k
return
}

!d::
SysGet, Mon, Monitor
if (MonRight != 1920) {
MouseGetPos, xpos, ypos
Click, 1253, 133
Sleep, 800
Click, 1242, 404
Sleep, 500
Click, 68, 259
MouseMove, xpos, ypos
return
} else {
MouseGetPos, xpos, ypos
Click, 1534, 101
Sleep, 800
Click, 1534, 210
Sleep, 500
Click, 291, 492
MouseMove, xpos, ypos
return
}

!+d::
PixelGetColor, dark_color, 44, 76
if (dark_color == 0xFCFCFC)
{
Click, 1731, 1028
Sleep, 200
Click, 1655, 856
Sleep, 200
Click, 1831, 605
Send, k
Send, k
return
}
else
{
Click, 1731, 1028
Sleep, 200
Click, 1706, 858
Sleep, 200
Click, 1831, 605
Send, k
Send, k
return
}

!p::
SysGet, Mon, Monitor
if (MonRight != 1920) {
MouseGetPos, xpos, ypos
Click, 1349, 727
MouseMove, xpos, ypos
return
} else {
MouseGetPos, xpos, ypos
Click, 1890, 1048
MouseMove, xpos, ypos
return
}

!l::
MouseGetPos, xpos, ypos
Click, 1649, 1002
MouseMove, xpos, ypos
return

!r::
MouseGetPos, xpos, ypos
Click, 1651, 1034
MouseMove, xpos, ypos
return