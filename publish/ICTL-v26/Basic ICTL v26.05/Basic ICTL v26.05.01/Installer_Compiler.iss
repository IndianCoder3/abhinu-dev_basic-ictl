; Inno Setup Comipler for ICTL v26.05.01

#define MyAppName "Basic ICTL v26.05.01"
#define MyAppVersion "26.05.01"
#define MyAppPublisher "IndianCoder3"
#define MyAppURL "https://indiancoder3.github.io/basic-ictl_site/"
#define MyAppExeName "ictl.exe"
#define MyAppAssocName "Basic ICTL Code File"
#define MyAppAssocExt ".ictl"
#define MyAppAssocKey StringChange(MyAppAssocName, " ", "") + MyAppAssocExt

[Setup]
; NOTE: The value of AppId uniquely identifies this application. Do not use the same AppId value in installers for other applications.
; (To generate a new GUID, click Tools | Generate GUID inside the IDE.)
AppId={{55FBBA50-B0BC-439E-9E7B-8D696DA505B9}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
;AppVerName={#MyAppName} {#MyAppVersion}
AppPublisher={#MyAppPublisher}
AppPublisherURL={#MyAppURL}
AppSupportURL={#MyAppURL}
AppUpdatesURL={#MyAppURL}
DefaultDirName=C:\Program Files\IndianCoder3\Abhinu.Dev\Basic ICTL\v26\{#MyAppName}
UninstallDisplayIcon={app}\{#MyAppExeName}
; "ArchitecturesAllowed=x64compatible" specifies that Setup cannot run
; on anything but x64 and Windows 11 on Arm.
ArchitecturesAllowed=x64compatible
; "ArchitecturesInstallIn64BitMode=x64compatible" requests that the
; install be done in "64-bit mode" on x64 or Windows 11 on Arm,
; meaning it should use the native 64-bit Program Files directory and
; the 64-bit view of the registry.
ArchitecturesInstallIn64BitMode=x64compatible
ChangesAssociations=yes
DisableProgramGroupPage=yes
LicenseFile=E:\HDD\Coding\abhinu-dev_basic-ictl\publish\ICTL-v26\Basic ICTL v26.04\Basic ICTL v26.05.01\Interpreter\LICENSE.txt
InfoBeforeFile=E:\HDD\Coding\abhinu-dev_basic-ictl\publish\ICTL-v26\Basic ICTL v26.04\Basic ICTL v26.05.01\Interpreter\INFO.txt
; Uncomment the following line to run in non administrative install mode (install for current user only).
;PrivilegesRequired=lowest
OutputDir=E:\HDD\Coding\abhinu-dev_basic-ictl\publish\ICTL-v26\Basic ICTL v26.04\Basic ICTL v26.05.01
OutputBaseFilename=installer-ictl_v26-04-01
SetupIconFile=E:\HDD\Coding\abhinu-dev_basic-ictl\publish\ICTL-v26\Basic ICTL v26.04\Basic ICTL v26.05.01\Interpreter\ictl_icon.ico
SolidCompression=yes
WizardStyle=modern windows11
ChangesEnvironment=yes
PrivilegesRequired=admin

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked

[Files]
Source: "E:\HDD\Coding\abhinu-dev_basic-ictl\publish\ICTL-v26\Basic ICTL v26.04\Basic ICTL v26.05.01\Interpreter\{#MyAppExeName}"; DestDir: "{app}"; Flags: ignoreversion
Source: "E:\HDD\Coding\abhinu-dev_basic-ictl\publish\ICTL-v26\Basic ICTL v26.04\Basic ICTL v26.05.01\Interpreter\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs
; NOTE: Don't use "Flags: ignoreversion" on any shared system files

[Registry]
Root: HKA; Subkey: "Software\Classes\{#MyAppAssocExt}\OpenWithProgids"; ValueType: string; ValueName: "{#MyAppAssocKey}"; ValueData: ""; Flags: uninsdeletevalue
Root: HKA; Subkey: "Software\Classes\{#MyAppAssocKey}"; ValueType: string; ValueName: ""; ValueData: "{#MyAppAssocName}"; Flags: uninsdeletekey
Root: HKA; Subkey: "Software\Classes\{#MyAppAssocKey}\DefaultIcon"; ValueType: string; ValueName: ""; ValueData: "{app}\{#MyAppExeName},0"
Root: HKA; Subkey: "Software\Classes\{#MyAppAssocKey}\shell\open\command"; ValueType: string; ValueName: ""; ValueData: """{app}\{#MyAppExeName}"" ""%1"""
; PATH:
Root: HKLM; Subkey: "SYSTEM\CurrentControlSet\Control\Session Manager\Environment"; ValueType: expandsz; ValueName: "Path"; ValueData: "{olddata};{app}"; Flags: preservestringtype

[Icons]
Name: "{autoprograms}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"
Name: "{autodesktop}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; Tasks: desktopicon

[Run]
Filename: "{app}\{#MyAppExeName}"; Description: "{cm:LaunchProgram,{#StringChange(MyAppName, '&', '&&')}}"; Flags: nowait postinstall skipifsilent
