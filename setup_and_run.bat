@echo off
SETLOCAL

REM Check if Python is installed
python --version >nul 2>&1
IF ERRORLEVEL 1 (
    echo Python is not installed. Please install Python 3.x.
    EXIT /B 1
)

REM Check if pip is installed
python -m pip --version >nul 2>&1
IF ERRORLEVEL 1 (
    echo pip is not installed. Installing pip...
    python -m ensurepip --default-pip
)

REM Check if virtualenv is installed
python -m virtualenv --version >nul 2>&1
IF ERRORLEVEL 1 (
    echo virtualenv is not installed. Installing virtualenv...
    python -m pip install virtualenv
)

REM Create a virtual environment if it doesn't exist
IF NOT EXIST "smartbankvenv" (
    echo Creating virtual environment...
    python -m virtualenv smartbankvenv
)

REM Activate the virtual environment
CALL smartbankvenv\Scripts\activate

REM Install required Python libraries
echo Installing required Python libraries...
pip install -r requirements.txt

REM for /f "tokens=*" %%i in (requirements.txt) do (
REM     echo Installing %%i...
REM     pip install %%i
REM     IF ERRORLEVEL 1 (
REM         echo Failed to install %%i. Skipping...
REM     )
REM )

REM Run the Python program
echo Running the Python program...
python bank_gui.py

REM Deactivate the virtual environment
echo Deactivating virtual environment...
CALL smartbankvenv\Scripts\deactivate
REM deactivate

ENDLOCAL
pause