[app]

# (str) Title of your application
title = BFJI Database

# (str) Package name
package.name = bfjidatabase

# (str) Package domain (needed for android/ios packaging)
package.domain = com.yourdomain

# (str) Source code where the main.py live
source.dir = .

# (str) Application versioning (method 1)
version = 0.1

# (int) Version code of your application
version.code = 1

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
orientation = portrait

# (list) List of service to declare
services = CAMERA

# (list) Permissions
android.permissions = CAMERA,INTERNET,ACCESS_NETWORK_STATE,WRITE_EXTERNAL_STORAGE

# (str) Android API to use
android.api = 29

# (int) Minimum API required
android.minapi = 21

# (int) Android SDK version to use
# android.sdk = 27

# (str) Android NDK version to use
android.ndk = 21.4.7075529

# (list) Android NDK modules to add (currently supported: sdl2, python3)
android.ndk_modules = python3

# (str) Android NDK toolchain to use
android.toolchain = clang

# (bool) Avoid print error traceback in console
log_level = 2

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy,pandas,pyzbar,Pillow,plyer,pydrive

# (str) Path to a custom kivy bootstrap template
#kivy.bootstrap = 

# (str) Color palette (testing only)
#osx.python_version = 3

# (bool) Kivy settings widget
#kivy.settings = default

# (str) iOS only: Xcode project to add (e.g. Plyer ios subproject)
#ios.add_xcodeproj = 

# (list) iOS framework directories (up to 2)
#ios.framework_dirs = 

# (list) iOS frameworks to link (up to 2)
#ios.frameworks = 

# (str) iOS icon (72x72)
#ios.icon = 

# (str) iOS launch image (320x50)
#ios.launch_image = 

# (str) iOS launch image ipad (768x1004)
#ios.launch_image_ipad = 

# (str) iOS launch image ipad landscape (1024x748)
#ios.launch_image_ipad_landscape = 

# (str) iOS launch image ipad retina (1536x2008)
#ios.launch_image_ipad_retina = 

# (str) iOS launch image ipad retina landscape (2048x1496)
#ios.launch_image_ipad_retina_landscape = 

# (str) iOS iPad App bundle (iPad)
#ios.plist = 

# (str) iOS iPad App bundle (iPad)
#ios.bundle_identifier = 

# (str) iOS add settings.bundle or not
#ios.settings_bundle = 

# (str) iOS Frameworks to use
#ios.frameworks = 

# (bool) Compile with clang
#ios.clang = 0

# (str) Log directory
#log_dir = $HOME

# (bool) Use a black terminal for the application
#blacklist_externals = 

# (bool) Uses an optimized python for android (only available for arch armeabi)
#armeabi_optimizations = false

# (str) iOS app export method (export, adhoc, development, enterprise, appstore)
#ios.export_method = appstore

# (bool) Use the --private command line argument
#private = 

# (str) Keystore path (used for android packaging)
#android.keystore = /path/to/keystore

# (str) Keystore password (used for android packaging)
#android.keystore_pass = password

# (str) Key alias (used for android packaging)
#android.key_alias = 

# (str) Key password (used for android packaging)
#android.key_pass = 

# (str) Android logcat filters to use
#android.logcat_filters = *:S python:D

# (bool) Copy host python instead of the precompiled one
#copy_host_python = False

# (bool) Create a package using zip
#package.zipapp = False

# (str) Android entry point, default is ok for Kivy-based app
#android.entrypoint = org.renpy.android.PythonActivity

# (str) Android app theme, default is okay for Kivy-based app
#android.app_theme = @android:style/Theme.NoTitleBar.Fullscreen

# (list) Pattern to whitelist for the whole project
#source.whitelist = 

# (str) Path to a custom source patch
#source.patch = 

# (list) Apply a patch from a file to source
#source.patch.source = 

# (list) Apply a patch to source
#source.patch.return_value = 

# (str) SDL2 image (bmp, pnm, xpm, xcf, pcx, gif, jpeg, jpg, png, webp)
#source.include_exts = 

# (str) Path to a custom sdl2 image directory (if not in the default directory)
#source.sdl2_image = 

# (str) SDL2 mixer (ogg, wav, mp3)
#source.exclude_exts = 

# (str) Path to a custom sdl2 mixer directory (if not in the default directory)
#source.sdl2_mixer = 

# (str) SDL2 ttf (ttf)
#source.exclude_dirs = 

# (str) Path to a custom sdl2 ttf directory (if not in the default directory)
#source.sdl2_ttf = 

# (str) SDL2 (SDL2, image, ttf, mixer, ...) SDL2_gfx (SDL2, image, ttf, mixer, ...)
#source.ios_frameworks = 

# (str) Custom source files (Separate with commas)
#source.custom_dir = 

# (str) Android assets directory
#source.android_assets_dir = 

# (str) Android strings filename to include
#source.android_strings = 

# (str) Android ignore paths
#source.android_ignore = 

# (str) Custom source files (Separate with commas)
#source.custom_dir = 

# (str) iOS frameworks to include (delimited by commas)
#ios.frameworks =

# (str) iOS plist dictionary to include (just like in Xcode)
#ios.plist =

# (list) List of Java .jar files to add to the .jar dependency.
#android.add_jars = foo.jar,bar.jar

# (list) List of Java files to add to the .jar dependency.
#android.add_jars_src = foo/src/,bar/src/
