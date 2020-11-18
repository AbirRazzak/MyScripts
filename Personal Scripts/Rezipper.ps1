# Rezipper - Unzips all zip files in the current directory to their own folders and then rezips each folder back into zip files
# Note: This script requires PowerShell v.5.0+ to be able to run.

# Script to unzip all zips in current dir
gci -Recurse -Filter *.zip |ForEach-Object {$n=($_.Fullname.trimend('.zip')); Expand-Archive -Path $_.Fullname -DestinationPath $n -Force}

# Do something to the files

# Script to zip everything in current dir, individually
gci |ForEach-Object {$n=($_.Fullname); Compress-Archive -Path $_\* -DestinationPath "$_.zip" -Force}
