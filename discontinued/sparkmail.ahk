#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.

#NoTrayIcon
DetectHiddenWindows, On

#!+e::
{
	if !WinExist("ahk_exe Spark Desktop.exe")
	{
		run,  "C:\Users\Aarjav\AppData\Local\Programs\SparkDesktop\Spark Desktop.exe"
		visible := true
		return
	}

	if (visible)
	{
		if WinActive("Spark") {
			switch := true
		} else {
			switch := false
		}
		WinHide, ahk_exe Spark Desktop.exe
		visible := false
		if (switch) {
			Send, !{Tab}
		}
		Sleep, 50
	}
	else
	{
		WinShow, ahk_exe Spark Desktop.exe
		WinActivate, ahk_exe Spark Desktop.exe
		visible := true
	}

	return
}