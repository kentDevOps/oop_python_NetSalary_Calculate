from cx_Freeze import setup, Executable

# Đường dẫn icon
icon_path = r"E:\HocTap\Net_Salary_Calculate\fil.ico"
#icon_path = "[TARGETDIR]fil.ico"
#E:\HocTap\Net_Salary_Calculate
# Cấu hình bảng shortcutpython
shortcut_table = [
    ("DesktopShortcut",  # Shortcut trên Desktop
     "DesktopFolder",  # Đặt shortcut trên Desktop
     "NetSalary",  # Tên shortcut
     "TARGETDIR",  # Thư mục cài đặt
     "[TARGETDIR]NetSalary",  # Đường dẫn đến file EXE
     None,  # Không có arguments
     "NetSalary Application",  # Mô tả shortcut
     icon_path,  # 📌 Đường dẫn icon
     0,  # 📌 Icon index
     None,  # ShowCmd
     "TARGETDIR",  # Working directory
     None
     ),

    ("StartMenuShortcut",  # Shortcut trong Start Menu
     "ProgramMenuFolder",  # Đặt shortcut trong Start Menu
     "NetSalary",  # Tên shortcut
     "TARGETDIR",  # Thư mục cài đặt
     "[TARGETDIR]NetSalary.exe",  # Đường dẫn đến file EXE
     None,  # Không có arguments
     "NetSalary Application",  # Mô tả shortcut
     icon_path,  # 📌 Đường dẫn icon
     0,  # 📌 Icon index
     None,  # ShowCmd
     "TARGETDIR",  # Working directory
     None
     ),
]

# Dữ liệu cho trình cài đặt MSI
msi_data = {"Shortcut": shortcut_table}

# Cấu hình setup
setup(
    name="NetSalary",
    version="1.0",
    description="NetSalary Calculation Tool",
    options={
    "build_exe": {
        "include_files": ["fil.ico"],  # Copy icon vào thư mục build
    },
        "bdist_msi": {
            "data": msi_data,
            "install_script": None,
            "target_name": "NetSalary.exe",
            "initial_target_dir": r"E:\OK\NetSalary",  # 📌 Đường dẫn hợp lệ
        }
    },
    executables=[Executable("main.py", target_name="NetSalary.exe", icon=icon_path)],  # 📌 Icon cho file EXE
)

#python setup.py bdist_msi

