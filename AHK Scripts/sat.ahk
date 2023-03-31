#NoTrayIcon

#IfWinActive ahk_exe Bluebook.exe
!a:: Send, ^+1
!b:: Send, ^+2
!c:: Send, ^+3
!d:: Send, ^+4

!m:: Send, ^!m

!+a:: Send, ^!1
!+b:: Send, ^!2
!+c:: Send, ^!3
!+d:: Send, ^!4

!w:: Send, ^!a

^Enter::
Send, {Tab}
Send, {Enter}
return

!q::
Send, +{Tab}
Send, {Enter}
return

!k:: Send, ^!b
!l:: Send, ^!x
!r:: Send, ^!r