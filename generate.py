import os
import glob

def generate_html_index(root_directory, output_file="./public/index.html"):
    """
    生成指定根目錄下所有日期文件夾中 HTML 檔案的索引 HTML 檔案。

    Args:
        root_directory (str): 要讀取的根目錄路徑。
        output_file (str, optional): 輸出 HTML 檔案的名稱。預設為 "index.html"。
    """

    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Index of {root_directory}</title>
    </head>
    <body>
        <h1>Index of {root_directory}</h1>
    """

    for date_folder in sorted(os.listdir(root_directory)):
        date_path = os.path.join(root_directory, date_folder)
        if os.path.isdir(date_path):
            html_files = glob.glob(os.path.join(date_path, "*.html"))

            if html_files:
                html_content += f"<h2>{date_folder}</h2>\n<ul>\n"
                for file_path in html_files:
                    file_name = os.path.basename(file_path)
                    html_content += f'  <li><a href="export/{os.path.join(date_folder, file_name)}">{file_name}</a></li>\n'
                html_content += "</ul>\n"

    html_content += """
    </body>
    </html>
    """

    # 寫入 HTML 檔案
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(html_content)

    print(f"已生成索引檔案：{output_file}")

if __name__ == "__main__":
    target_directory = "./public/export"  # 預設為目前目錄，你可以修改為任何本地目錄
    generate_html_index(target_directory)