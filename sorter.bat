@echo off
REM SET PATH TO PYTHON
REM (THIS IS USUALLY DONE DURING PYTHON INSTALLATION)

REM Set the path to your Python script (THIS IS USUALLY DONE DURING PYTHON INSTALLATION)
SET SCRIPT_PATH= <placeholder path here>

SET CURRENT_PATH=%CD%

REM CHANGE "%cd" to your path for desired path


python "%SCRIPT_PATH%" -p "%CURRENT_PATH%"

REM example "python "%SCRIPT_PATH" -p "%CURRENT_PATH"" which is the default value
REM example "%PYTHON_PATH%" "%SCRIPT_PATH%" -p "%CURRENT_PATH%" can also be done
echo DONE!
pause
