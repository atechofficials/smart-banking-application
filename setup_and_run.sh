#!/bin/bash

# Function to check if a command exists
command_exists() {
  command -v "$1" >/dev/null 2>&1
}

# Check if python3 and pip are installed
if ! command_exists python3; then
    echo "Python3 is not installed. Please install Python3."
    exit 1
fi

if ! command_exists pip3; then
    echo "pip3 is not installed. Installing pip3..."
    # Try to install pip3
    if command_exists apt-get; then
        sudo apt-get update
        sudo apt-get install -y python3-pip
    elif command_exists yum; then
        sudo yum install -y python3-pip
    else
        echo "Error: Cannot install pip3. Please install it manually."
        exit 1
    fi
fi

# Check if virtualenv is installed
if ! command_exists virtualenv; then
    echo "virtualenv is not installed. Installing virtualenv..."
    pip3 install --user virtualenv
fi

# Create a virtual environment if it doesn't exist
if [ ! -d "smartbankvenv" ]; then
    echo "Creating virtual environment..."
    python3 -m virtualenv smartbankvenv
fi

# Activate the virtual environment
echo "Activating virtual environment..."
source smartbankvenv/bin/activate

# Install required Python libraries
echo "Installing required Python libraries..."
pip install -r requirements.txt

# Install required Python libraries
# echo "Installing required Python libraries..."
# while IFS= read -r package; do
#     echo "Installing $package..."
#     pip install "$package"
#     if [ $? -ne 0 ]; then
#         echo "Failed to install $package. Skipping..."
#     fi
# done < requirements.txt

# Run the Python program
echo "Running the Python program..."
python3 bank_gui.py

# Deactivate the virtual environment
echo "Deactivating virtual environment..."
deactivate