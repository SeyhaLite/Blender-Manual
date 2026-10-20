@ECHO OFF

pushd %~dp0

REM Windows build entry point for the Khmer Blender Manual.
REM Mirrors the Makefile targets: html (default), livehtml, gettext, clean.

if "%SPHINXBUILD%"=="" set SPHINXBUILD=sphinx-build
if "%SPHINXOPTS%"=="" set SPHINXOPTS=
if "%SOURCEDIR%"=="" set SOURCEDIR=manual
if "%BUILDDIR%"=="" set BUILDDIR=build

REM Use the virtual environment when it exists.
if exist .venv\Scripts\sphinx-build.exe set SPHINXBUILD=.venv\Scripts\sphinx-build

if "%1"=="" goto html
if "%1"=="help" goto help
goto run

:help
echo Targets:
echo   html        build HTML into %BUILDDIR%\html, failing on any warning
echo   html-quick  build HTML without treating warnings as errors
echo   gettext     extract .pot catalogs into %BUILDDIR%\locale
echo   clean       remove %BUILDDIR%
echo   check       run tools\check_translation.py
goto end

:html
%SPHINXBUILD% -M html %SOURCEDIR% %BUILDDIR% %SPHINXOPTS% -W --keep-going
goto end

:html-quick
%SPHINXBUILD% -M html %SOURCEDIR% %BUILDDIR% %SPHINXOPTS%
goto end

:gettext
%SPHINXBUILD% -b gettext %SOURCEDIR% %BUILDDIR%\locale %SPHINXOPTS%
goto end

:clean
if exist %BUILDDIR% rmdir /s /q %BUILDDIR%
goto end

:check
python tools\check_translation.py
goto end

:run
%SPHINXBUILD% -M %1 %SOURCEDIR% %BUILDDIR% %SPHINXOPTS%

:end
popd
