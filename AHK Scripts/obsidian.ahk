#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.

#NoTrayIcon
DetectHiddenWindows, On

!+o::
{
	if !WinExist("ahk_exe Obsidian.exe")
	{
		run,  "C:\Users\Aarjav\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Obsidian.lnk"
		visible := true
		return
	}

	if (visible)
	{
		if WinActive("ahk_exe Obsidian.exe") {
			switch := true
		} else {
			switch := false
		}
		WinHide, ahk_exe Obsidian.exe
		visible := false
		if (switch) {
			Send, !{Tab}
		}
		Sleep, 50
	}
	else
	{
		WinShow, ahk_exe Obsidian.exe
		WinActivate, ahk_exe Obsidian.exe
		visible := true
	}

	return
}