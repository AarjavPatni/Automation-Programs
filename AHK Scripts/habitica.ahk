#NoTrayIcon
DetectHiddenWindows, On

!h::
{
	if !WinExist("Habitica")
	{
		run,  "C:\Users\Aarjav\Desktop\Habitica.lnk"
		visible := true
		return
	}

	if (visible)
	{
		if WinActive("Habitica") {
			switch := true
		} else {
			switch := false
		}
		WinHide, Habitica
		visible := false
		if (switch) {
			Send, !{Tab}
		}
		Sleep, 50
	}
	else
	{
		WinShow, Habitica
		WinActivate, Habitica
		visible := true
	}

	return
}