[app]
# App details
title = Zombie Reality - GC
package.name = zombierealitygc
package.domain = org.gc
author = GC
source.include_exts = py,ogg,png
version = 1.0

# Requirements
requirements = python3,pygame

# Screen orientation
orientation = landscape
fullscreen = 1

# Icon
icon.filename = icon.png

# Android API settings (reduces APK size)
android.api = 29
android.minapi = 21

# Permissions
android.permissions =

# Release / Build optimization
android.debug = False       # Release mode (smaller APK)
android.minify = True       # Removes unused code
android.strip = True        # Removes debugging symbols
android.release_artifact = apk

# AndroidX & dependencies
android.enable_androidx = False
android.gradle_dependencies =
