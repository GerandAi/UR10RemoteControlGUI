@echo off
setlocal enabledelayedexpansion

::if defined i (echo i is being used) else (echo i is SAFE to use)
::if defined c (echo c is being used) else (echo c is SAFE to use)
::if defined b (echo b is being used) else (echo b is SAFE to use)
::if defined a (echo a is being used) else (echo a is SAFE to use)
::if defined x (echo x is being used) else (echo x is SAFE to use)
::if defined y (echo y is being used) else (echo y is SAFE to use)
::if defined z (echo z is being used) else (echo z is SAFE to use)
::if defined pitch (echo pitch is being used) else (echo pitch is SAFE to use)
::if defined roll (echo roll is being used) else (echo roll is SAFE to use)
::if defined yaw (echo yaw is being used) else (echo yaw is SAFE to use)


set /a b=10 && set /a a=1
echo [left:4] [right:6] [up:8] [down:2] [clear:C] [finish:0]
echo [W=retract] [S=extend] [(A/D)=yaw] [(Q/E)=roll] [(P/L)=pitch]
echo [SPACE=return] [ENTER=continue]

:clear
set /a x=0 && set /a y=0 && set /a z=0
set /a pitch=0 && set /a roll=0 && set /a yaw=0
echo cleared previously stored movement velocity

:halt
echo paused, waiting for command, or press ENTRE to continue with previous velocity
echo 0.0>coord.txt&&echo 0.000>>coord.txt&& echo 0.0>>coord.txt
echo 0.0>>coord.txt&& echo 0.0>>coord.txt&& echo 0.0>>coord.txt

for /L %%i in (1,1,9) do (
	set c=void
	set /p c=direction: 

	if !c! == 4 set /a x+=%b% && echo accelerating left
	if !c! == 6 set /a x-=%b% && echo accelerating right
	if !c! == 8 set /a z+=%b%  && echo accelerating up
	if !c! == 2 set /a z-=%b%  && echo accelerating down
	if "!c!" equ "c" goto clear
	if !c! equ 0 goto finish
	if "!c!" equ " " goto halt
	if "!c!" equ "s" set /a y-=%b% && echo extend faster a bit
	if "!c!" equ "w" set /a y+=%b% && echo retract faster a bit
	if "!c!" == "a" set /a yaw+=%a% && echo yaw left faster a bit
	if "!c!" == "d" set /a yaw-=%a% && echo yaw right faster a bit
	if "!c!" == "q" set /a roll+=%a% && echo roll left faster a bit
	if "!c!" == "e" set /a roll-=%a% && echo roll right faster a bit
	if "!c!" == "p" set /a pitch+=%a% && echo pitch up faster a bit
	if "!c!" == "l" set /a pitch-=%a% && echo pitch down faster a bit

	

	::sendpos
	echo !x!>coord.txt&& echo !y!>>coord.txt&& echo !z!>>coord.txt
	if !pitch! geq 0 (echo 0.!pitch!>>coord.txt) else (set /a modpitch=-!pitch! && echo -0.!modpitch!>>coord.txt)
	if !roll! geq 0 (echo 0.!roll!>>coord.txt) else (set /a modroll=-!roll! && echo -0.!modroll!>>coord.txt)
	if !yaw! geq 0 (echo 0.!yaw!>>coord.txt) else (set /a modyaw=-!yaw! && echo -0.!modyaw!>>coord.txt)
	
	::speed indication
	echo current relative velocity vector:
	type coord.txt
)
:finish
echo finished
echo 0.0>coord.txt&& echo 0.0>>coord.txt&& echo 0.0>>coord.txt
echo 0.0>>coord.txt&&echo 0.0>>coord.txt&& echo 0.0>>coord.txt

::pause


::if "!c!" equ "void" (echo stored velocity:) else (echo actual relative speed:)