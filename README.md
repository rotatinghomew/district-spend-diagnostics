# district-spend-diagnostics

节会期间的商品净额、商户覆盖与数据恢复记录。 其中人物代号、机构、交易及历史回执均为合成资料。

## 数据约定

`data/layout.json` 逐一解释业务表及 CSV 列顺序，`data/rules.json` 记录运营口径。CSV 使用 UTF-8、首行为列名；空白字段表示未提供或不适用，`+` 隔开多值字段。历史记录的业务时刻与送交时刻含义不同，按各表说明解释。

- `register.csv`：本地统计日开始小时和商户基准覆盖日历；控制商圈仅是候选比较，不等于可信对照。
- `coverage.csv`：当日覆盖状态或缺访上界，缺访金额不计作零。
- `sales.csv`：单位、净前金额、可核定的履约到达时间以及有交叉记录时的可归属候选。
- `payment.csv`：可用于关联的财务记录，不等同于商品履约。
- `refunds.csv`：退回关联、金额和以同号 revision 替换的事实。
- `bulletins.csv`：已发通报的原始判断和下一次复盘请求；原判断允许被外部资料纠正。
- `terminals.csv`：一组可共享故障的终端及门店；同版本记录是运行事实而非分析结论。
- `recoveries.csv`：按终端窗口的故障、接单和部分恢复回执；新行用 ref 引用原记录。
- `comparison_calendar.csv`：编辑明确留作比较的经营时段与通报分析截面。

## 本地检查

使用 Python 3.11 及标准库。`python3 inspect_inputs.py` 读取原始资料并列出记录数；`python3 -m unittest discover -s tests` 检查输入资料。检查不计算或发布业务结论。
