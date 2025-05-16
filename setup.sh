#!/bin/bash
# SPDX-FileCopyrightText: © 2024 Jimmy Fitzpatrick <jcfitzpatrick12@gmail.com>
# This file is part of SPECTRE
# SPDX-License-Identifier: GPL-3.0-or-later

SPECTRE_GROUP=spectre-group
SPECTRE_SERVICE_PORT=5000
SPECTRE_SERVICE_HOST="0.0.0.0"
UDEV_FILE="/etc/udev/rules.d/99-spectre.rules"
DOTENV_FILE="./.env"

# Check if the script is run with root privileges.
if [ "$EUID" -ne 0 ]; then
    echo "❌ Please run this script as root: sudo ./setup.sh"
    exit 1
fi

# Create the group if it doesn't exist.
if getent group "$SPECTRE_GROUP" > /dev/null; then
    echo "✅ Group '$SPECTRE_GROUP' already exists"
else
    echo "➕ Creating group '$SPECTRE_GROUP'"
    groupadd "$SPECTRE_GROUP"
    echo "✅ Group '$SPECTRE_GROUP' created"
fi

# Add udev rule for USB access. The `SPECTRE_GROUP` group will have read/write access to USB devices.
echo "📝 Writing udev rule to $UDEV_FILE"
tee "$UDEV_FILE" > /dev/null <<EOF
SUBSYSTEM=="usb", MODE="0660", GROUP="$SPECTRE_GROUP"
EOF
echo "✅ Udev rule written"

# Reload udev rules and trigger them
echo "🔄 Reloading udev rules"
udevadm control --reload-rules
udevadm trigger
echo "✅ Udev rules reloaded"

# Get the group ID and write .env file for Docker Compose
GID=$(getent group "$SPECTRE_GROUP" | cut -d: -f3)
echo "📦 Writing environment variables to .env"
{
    echo "SPECTRE_GID=$GID" 
    echo "SPECTRE_SERVICE_PORT=$SPECTRE_SERVICE_PORT"
    echo "SPECTRE_SERVICE_HOST=$SPECTRE_SERVICE_HOST"
} > "$DOTENV_FILE"
echo "✅ $DOTENV_FILE written"

echo "🎉 Setup complete!"
echo "You can now run the application with: docker compose up --build"
