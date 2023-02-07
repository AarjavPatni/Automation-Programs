; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.

sleep, 3

; Set the title of the windows to hide
window1Title = C:\Syncthing\syncthing.exe
window2Title = C:\Windows\System32\bash.exe
window3Title = C:\Program Files\Git\cmd\git.exe


; Set up a loop that will keep checking for the two windows
while (true) {
    check = 0
    ; Check if the first window is open
    IfWinExist, %window1Title%
        {
            ; Hide the window and show a tray icon for it
            WinHide, %window1Title%
            check++
        }

    ; Check if the second window is open
    IfWinExist, %window2Title%
        {
            ; Hide the window and show a tray icon for it
            WinHide, %window2Title%
            check++
        }

    ; Check if the second window is open
    IfWinExist, %window3Title%
        {
            ; Hide the window and show a tray icon for it
            WinHide, %window3Title%
            check++
        }

    ; Check if both windows are now hidden
    if (check >= 1)
        {
            TrayTip, All windows are hidden
            ; If both windows are hidden, break out of the loop
            break
        }
    sleep, 5000
}