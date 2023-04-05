#NoTrayIcon
#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.

#IfWinActive ahk_exe Todoist.exe
:*:phylec::{#}Physics & search:Lecture
:*:pclec::{#}Physical Chemistry & search:Lecture
:*:ioclec::{#}Inorganic Chemistry & search:Lecture
:*:oclec::{#}Organic Chemistry & search:Lecture
:*:mlec::{#}Mathematics & search:Lecture

:*:phyrev::{#}Physics & search:Revision
:*:pcrev::{#}Physical Chemistry & search:Revision
:*:iocrev::{#}Inorganic Chemistry & search:Revision
:*:ocrev::{#}Organic Chemistry & search:Revision
:*:mrev::{#}Mathematics & search:Revision

:*:phyhw::{#}Physics & search:Homework
:*:pchw::{#}Physical Chemistry & search:Homework
:*:iochw::{#}Inorganic Chemistry & search:Homework
:*:ochw::{#}Organic Chemistry & search:Homework
:*:mhw::{#}Mathematics & search:Homework

:*:lnss::@next-actions @study @short
:*:lnsm::@next-actions @study @medium
:*:lnsl::@next-actions @study @long
:*:lnis::@next-actions @interests @short
:*:lnim::@next-actions @interests @medium
:*:lnil::@next-actions @interests @long