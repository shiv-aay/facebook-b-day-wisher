$value=Test-Path ("$pwd"+"\chromedriver.exe")
pip install selenium
if($value -notmatch 'True')
{
    Write-Output "Downloading chrome driver"
    $ver=(Get-Item (Get-ItemProperty 'HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths\chrome.exe').'(Default)').VersionInfo.ProductVersion
    $client = new-object System.Net.WebClient
    $URI="https://chromedriver.storage.googleapis.com/LATEST_RELEASE_"+$ver[0]+$ver[1]
    $HTML=Invoke-WebRequest -Uri $URI
    $driver=$HTML.Content
    $client.DownloadFile("https://chromedriver.storage.googleapis.com/"+$driver+"/chromedriver_win32.zip","$PWD"+'\chromedriver_win32.zip')
    Expand-Archive -LiteralPath ("$PWD"+"\chromedriver_win32.zip") -DestinationPath "$pwd"
    Remove-Item -Path ("$PWD"+"\chromedriver_win32.zip")
}

$key=Test-Path ("$pwd"+'\credentials.txt')
if($key -notmatch 'True')
{
    $name = Read-Host 'What is your username/mobile number for facebook?'
    $choice = Read-Host 'Do you want to post wishes instantaneously?'
    $pass = Read-Host 'What is your password?' -AsSecureString
    $path="$pwd"+"\credentials.txt"
    $name | Out-File -FilePath $path
    $choice | Out-File -FilePath $path -Append
    [Runtime.InteropServices.Marshal]::PtrToStringAuto(
        [Runtime.InteropServices.Marshal]::SecureStringToBSTR($pass)) | Out-File -FilePath $path -Append
}