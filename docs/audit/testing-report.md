# 测试报告

执行环境为 Windows、Python 3.12，使用各专题安装的依赖环境；TaskFlow 与模板从本轮快照重新编辑安装。命令为 `python -m pytest -q`。

| 仓库 | 审计前提交 | 文件 | 本轮测试通过 |
| --- | --- | --- | --- |
| [python-learning-roadmap](https://github.com/zyy-stu/python-learning-roadmap) | [26a16a5](https://github.com/zyy-stu/python-learning-roadmap/commit/26a16a5fcc9a49aec6cb1fb08cdb7afcb79d3499) | 29 | 不适用 |
| [python-basic](https://github.com/zyy-stu/python-basic) | [fff664d](https://github.com/zyy-stu/python-basic/commit/fff664d025d71408a4b95346c8f6c3c0245daf84) | 78 | 115 |
| [python-advanced](https://github.com/zyy-stu/python-advanced) | [0bcb6c0](https://github.com/zyy-stu/python-advanced/commit/0bcb6c0961e8a1016a6dc80ad684ccb09fc209d1) | 67 | 9 |
| [python-web](https://github.com/zyy-stu/python-web) | [60e8574](https://github.com/zyy-stu/python-web/commit/60e85743259f3d645a56f562068c0152825205f3) | 102 | 15 |
| [python-data-science](https://github.com/zyy-stu/python-data-science) | [66f3f90](https://github.com/zyy-stu/python-data-science/commit/66f3f905cee6d93f15bbbdadeed0714974c30eed) | 146 | 18 |
| [python-ai](https://github.com/zyy-stu/python-ai) | [e933e34](https://github.com/zyy-stu/python-ai/commit/e933e34c4e716ed56708acd19e5c11610f8449d4) | 86 | 7 |
| [python-projects](https://github.com/zyy-stu/python-projects) | [c292385](https://github.com/zyy-stu/python-projects/commit/c292385b405346c5f826b20322b2e3da430feae0) | 157 | 40 |

六仓 204 项通过、零失败、零跳过。AI 包含 CPU PyTorch。主仓没有 Python 测试，按文档检查验收。上述为修复前审计复跑记录，本次修复后的项目复跑结果另在提交交付说明中报告。
