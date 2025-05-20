@echo off
if "%1" == "build" (
goto :build
)
if "%1" == "serve" (
goto :serve
)
if "%1" == "publish" (
goto :publish
) else (
echo opcoes:
echo build
echo serve
echo publish
)
goto :eof

:build
pelican content
goto :eof

:serve
pelican --listen
goto :eof

:publish
echo publish
goto :eof
