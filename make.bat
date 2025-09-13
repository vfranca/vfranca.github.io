@echo off
set cmd=%1

if /i "%cmd%" == "buildlocal" (
    goto :local
)

if /i "%cmd%" == "buildweb" (
    goto :web
)

if /i "%cmd%" == "serve" (
    goto :serve
)

if /i "%cmd%" == "serveopen" (
    goto :serveopen
)

echo Comando invalido: %cmd%
echo Uso: make [buildlocal] [buildweb] [serve] [serveopen]
goto :EOF

:local
echo Construindo para local...
pelican content
goto :EOF

:web
echo Construindo para web...
pelican content -s publishconf.py
goto :EOF

:serve
echo Executando servidor HTTP...
pelican --listen
goto :EOF

:serveopen
start http://localhost:8000
pelican --listen
goto :EOF

