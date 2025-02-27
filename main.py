from pathlib import Path
from typing import List, Dict
from datetime import datetime
import logging
from IPython import get_ipython

# 设置日志
logger = logging.getLogger(__name__)

def generate_html_report(self, results: List[Dict], group_name: str = "全部标的") -> str:
    timestamp = datetime.now().strftime('%Y%m%d_%H%M')
    filename = f"market_analysis_{group_name}_{timestamp}.html"
    file_path = self.results_path / filename

    # 生成 HTML 内容（此处省略具体实现）
    html_content = "<html><body>报告内容</body></html>"  # 示例內容

    # 写入文件
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(html_content)

    # 检查是否在 Colab 环境中
    IN_COLAB = 'google.colab' in str(get_ipython())
    if IN_COLAB:
        try:
            from google.colab import files
            # 检查 IPython 内核是否可用
            ipython = get_ipython()
            if ipython is not None and ipython.kernel is not None:
                files.download(str(file_path))
            else:
                logger.warning("IPython kernel is not available. Skipping file download.")
                print("IPython 内核不可用，请手动从文件浏览器下载报告文件。")
        except ImportError:
            logger.warning("Not in Colab environment. Skipping file download.")
            print("未在 Colab 环境中运行，请在本地文件中查看报告。")
    else:
        print("未在 Colab 环境中运行，请在本地文件中查看报告。")

    return str(file_path)
