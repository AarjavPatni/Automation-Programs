#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.

#NoTrayIcon

SetDefaultMouseSpeed, 0

+#^/:: Winset, Alwaysontop, , A
!+p:: run "python" "C:\Users\Aarjav\Documents\Automation-Programs\GTD Capture\GTDCapture.py"
;#o:: run "C:\Users\Aarjav\Documents\Automation Programs\enableCamera.lnk"
;#+o:: run "C:\Users\Aarjav\Documents\Automation Programs\disableCamera.lnk"
;#a:: run "C:\Users\Aarjav\Documents\Automation Programs\enableMic.lnk"
;#+a:: run "C:\Users\Aarjav\Documents\Automation Programs\disableMic.lnk"
#q:: Send !{f4}
#b:: Send #1
#f:: Send #e
#m:: Send #{UP}
#+m:: Send #{DOWN}
#+t:: Send ^+{Escape}
#e:: Send #+!e
#w:: return
#r:: return
:*:a2c::ApplyingToCollege

:*:emsch::aarjav.p_nms@gemselearning.com
:*:emgm::aarjav.patni1@gmail.com
:*:emout::aarjav.patni@outlook.com
:*:emapp::aarjavp@outlook.com
:*:emanon::anonymousse.anonaddy.com
:*:->::→
:*:---::---
:*:-.-::—
:*:=>::⇒

#t:: send, #3

#^s:: run "python" "C:\Users\Aarjav\Documents\TimeTrackr\trackr.py" "start"
#+s:: run "pythonw" "C:\Users\Aarjav\Documents\TimeTrackr\trackr.py" "contend"
#+a:: run "python" "C:\Users\Aarjav\Documents\TimeTrackr\trackr.py" "add"
#z:: run "pythonw" "C:\Users\Aarjav\Documents\TimeTrackr\trackr.py" "running"
#+g:: run "python" "C:\Users\Aarjav\Documents\TimeTrackr\trackr.py" "gsheets"
#+e:: run "pythonw" "C:\Users\Aarjav\Documents\TimeTrackr\trackr.py" "export" "today"
#+f:: run "pythonw" "C:\Users\Aarjav\Documents\Automation-Programs\Cold Turkey\focus.pyw"
!+b:: run "python" "C:\Users\Aarjav\Documents\Automation-Programs\Cold Turkey\add2block.pyw"

#IfWinActive ahk_exe Obsidian.exe
^v:: Send ^+v
^+v:: Send ^v

#IfWinActive ahk_exe Flow.Launcher.exe
ctrl & enter:: Send, ^o
^o:: Send, ^{Enter}

shift & delete::
KeyWait, LShift, T0.1
KeyWait, RShift, T0.1
KeyWait, Delete, T0.1
Sleep, 100
Send, ^o
Sleep, 100
Send, del
Sleep, 100
Send, {Enter}
Sleep, 100
Send, {Enter}
return

