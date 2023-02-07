#NoTrayIcon
DetectHiddenWindows, On

!m::
{
	if !WinExist("lofi.cafe")
	{
		run,  "C:\Users\Aarjav\Desktop\lofi.cafe.lnk"
		visible := true
		return
	}

	if (visible)
	{
		if WinActive("lofi.cafe") {
			switch := true
		} else {
			switch := false
		}
		WinHide, lofi.cafe
		visible := false
		if (switch) {
			Send, !{Tab}
		}
		Sleep, 50
	}
	else
	{
		WinShow, lofi.cafe
		WinActivate, lofi.cafe
		visible := true
	}

	return
}