# -*- coding: utf-8 -*-
"""
用张子健本科毕业论文《三元低共熔溶剂对毛竹组分可控分离》里的真实数据做演示
数据来源：论文第2章 图2-1/2-2/2-3、第3章 结晶度、第4章 漂白、第5章 2D-HSQC
"""
import matplotlib
matplotlib.use("Agg")
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams["font.sans-serif"] = ["Microsoft YaHei", "SimHei", "DejaVu Sans"]
plt.rcParams["axes.unicode_minus"] = False

# ============================================================
# 1. pandas：把论文里散落在三张图里的数字，整理成一张总表
# ============================================================
df_temp = pd.DataFrame({
    "温度": [30, 50, 60, 70, 90],
    "纤维素得率": [83, 61, 59, 44, 43],
    "木质素得率": [2, 8, 14, 19, 24],
})
df_time = pd.DataFrame({
    "时间": [2, 4, 6],
    "纤维素得率": [52, 43, 38],
    "木质素得率": [17, 24, 25],
})
df_hbd = pd.DataFrame({
    "氢键供体": ["甲酸FA", "乳酸LA", "草酸OA", "对甲苯磺酸TsOH"],
    "纤维素得率": [73, 72, 46, 43],
    "木质素得率": [2, 2, 11, 24],
})

print("=" * 58)
print("【1】pandas 干的活：三张图的数据合成一张表")
print("=" * 58)
print("温度系列：")
print(df_temp.to_string(index=False))
print()

# ============================================================
# 2. numpy：论文里没算过的东西 —— 边际效率
#    每损失 1% 纤维素，能换回多少木质素？
# ============================================================
df_temp["纤维素损失"] = -df_temp["纤维素得率"].diff()
df_temp["木质素增益"] = df_temp["木质素得率"].diff()
df_temp["换回效率"] = (df_temp["木质素增益"] / df_temp["纤维素损失"]).round(2)

print("=" * 58)
print("【2】numpy 干的活：算'升温值不值'（论文里没算过）")
print("=" * 58)
print(df_temp[["温度", "纤维素损失", "木质素增益", "换回效率"]].to_string(index=False, na_rep="-"))
print()
print("解读：50→60℃ 只用 2% 纤维素就换回 6% 木质素（效率 3.0），是相邻两段的 10 倍；")
print("      70→90℃ 只损失 1% 纤维素就换来 5% 木质素（效率 5.0）。")
print("      两个高效点 = 60℃ 和 90℃，正好就是你论文选的那两条工艺路线。")
print("      你当时是靠 SEM 和二维核磁得出的结论，纯算数字也能独立走到同一处。")
print()

# ============================================================
# 3. 机器学习的雏形：用 5 个已知温度点，预测你没做过的温度
# ============================================================
T = df_temp["温度"].to_numpy(float)
LIG = df_temp["木质素得率"].to_numpy(float)
CEL = df_temp["纤维素得率"].to_numpy(float)

coef_lig = np.polyfit(T, LIG, 2)
coef_cel = np.polyfit(T, CEL, 2)
T_grid = np.linspace(30, 90, 200)
lig_fit = np.polyval(coef_lig, T_grid)
cel_fit = np.polyval(coef_cel, T_grid)

print("=" * 58)
print("【3】这一步就是机器学习的雏形：用已有数据预测没做过的条件")
print("=" * 58)
print("你实际做了 5 个温度点：30/50/60/70/90 ℃")
print("下面这些温度你没做过，代码照样能给出预测值：\n")
for t in [40, 65, 75, 80, 85]:
    print(f"  {t}℃  ->  预测木质素得率 {np.polyval(coef_lig, t):5.1f}%   预测纤维素得率 {np.polyval(coef_cel, t):5.1f}%")
print()
print("拟合误差(R²)：木质素 %.4f   纤维素 %.4f" % (
    1 - np.sum((LIG - np.polyval(coef_lig, T))**2) / np.sum((LIG - LIG.mean())**2),
    1 - np.sum((CEL - np.polyval(coef_cel, T))**2) / np.sum((CEL - CEL.mean())**2),
))
print()
print("放大想：你有 4种供体 × 5个温度 × 3个时间 = 60 种组合，实际只做了 12 组。")
print("用机器学习就能用这 12 组预测另外 48 组，直接圈出最优工艺——这就是 AI 做材料。")
print()
print("注：本图只用了论文正文里明确给出的数字。第5章 2D-HSQC 只给了")
print("    L-60 的 β-O-4 = 10.4/100Ar、L-90 ≈ 0、S/G：MWL 1.08 → L-90 0.48，")
print("    MWL 的 β-O-4 与 L-60 的 S/G 论文未给具体值，所以没有画进图里。")
print()

# ============================================================
# 4. matplotlib：画一张论文里没有的图
# ============================================================
fig, ax = plt.subplots(2, 2, figsize=(13.5, 9.5), dpi=120)
BLUE, GREEN, RED, GRAY = "#185FA5", "#0F6E56", "#A32D2D", "#888780"

# --- (a) 温度扫描 + 拟合曲线 + 预测带 ---
a = ax[0, 0]
a.plot(T, LIG, "o", color=RED, ms=8, label="木质素得率（实测）", zorder=3)
a.plot(T, CEL, "s", color=BLUE, ms=8, label="纤维素得率（实测）", zorder=3)
a.plot(T_grid, lig_fit, "-", color=RED, lw=1.6, alpha=0.85, label="木质素（拟合外推）")
a.plot(T_grid, cel_fit, "-", color=BLUE, lw=1.6, alpha=0.85, label="纤维素（拟合外推）")
for t in [65, 75, 80, 85]:
    a.axvline(t, color=GRAY, ls=":", lw=0.9)
    a.plot(t, np.polyval(coef_lig, t), "x", color=RED, ms=7, mew=1.6)
    a.plot(t, np.polyval(coef_cel, t), "x", color=BLUE, ms=7, mew=1.6)
a.set_xlabel("反应温度 (℃)"); a.set_ylabel("得率 (%)")
a.set_title("(a) 温度扫描：实测点 + 预测未做过的温度（× 为预测值）", fontsize=12)
a.legend(fontsize=9, frameon=False); a.grid(alpha=0.25, lw=0.5)

# --- (b) 权衡图：纤维素 vs 木质素 ---
b = ax[0, 1]
b.plot(df_temp["纤维素得率"], df_temp["木质素得率"], "-o", color=BLUE, lw=1.8, ms=8)
for _, r in df_temp.iterrows():
    b.annotate(f"{int(r['温度'])}℃", (r["纤维素得率"], r["木质素得率"]),
               textcoords="offset points", xytext=(8, -3), fontsize=9)
b.scatter([59], [14], s=260, facecolors="none", edgecolors=GREEN, lw=2.2, zorder=4)
b.scatter([43], [24], s=260, facecolors="none", edgecolors=RED, lw=2.2, zorder=4)
b.annotate("60℃ 木质素工艺\n（结构完整）", (59, 14), textcoords="offset points",
           xytext=(-118, 22), fontsize=9, color=GREEN,
           arrowprops=dict(arrowstyle="->", color=GREEN, lw=1.2))
b.annotate("90℃ 纤维素工艺\n（木质素得率最高）", (43, 24), textcoords="offset points",
           xytext=(-30, -46), fontsize=9, color=RED,
           arrowprops=dict(arrowstyle="->", color=RED, lw=1.2))
b.set_xlabel("纤维素固含物得率 (%)"); b.set_ylabel("木质素得率 (%)")
b.set_title("(b) 得率权衡：两条工艺路线各取一端", fontsize=12)
b.grid(alpha=0.25, lw=0.5)

# --- (c) 结晶度三级台阶 ---
c = ax[1, 0]
stages = ["毛竹原料\n47.6%", "纤维素固含物\n53.02%", "漂白纤维素\n62.79%"]
vals = [47.6, 53.02, 62.79]
bars = c.bar(stages, vals, color=["#B4B2A9", "#378ADD", "#0F6E56"], width=0.55)
for bb, v in zip(bars, vals):
    c.text(bb.get_x() + bb.get_width()/2, v + 1.2, f"{v}%", ha="center", fontsize=11)
c.set_ylim(0, 75); c.set_ylabel("相对结晶度 (%)")
c.set_title("(c) 相对结晶度：47.6% → 53.02% → 62.79%", fontsize=12)
c.grid(alpha=0.25, axis="y", lw=0.5)

# --- (d) 时间系列：只画论文里真实给过的数据 ---
d = ax[1, 1]
x = np.arange(3); w = 0.36
d.bar(x - w/2, df_time["纤维素得率"], w, label="纤维素得率", color="#378ADD")
d.bar(x + w/2, df_time["木质素得率"], w, label="木质素得率", color="#A32D2D")
for xi, v in zip(x - w/2, df_time["纤维素得率"]):
    d.text(xi, v + 1, f"{v}%", ha="center", fontsize=9)
for xi, v in zip(x + w/2, df_time["木质素得率"]):
    d.text(xi, v + 1, f"{v}%", ha="center", fontsize=9)
d.set_xticks(x); d.set_xticklabels(["2 h", "4 h", "6 h"], fontsize=11)
d.set_xlabel("反应时间（60℃）"); d.set_ylabel("得率 (%)")
d.annotate("4h→6h：木质素只 +1%，\n纤维素却 -5%，不划算",
           xy=(2 + w/2, 25), xytext=(0.62, 0.72), textcoords="axes fraction",
           fontsize=9, color="#5F5E5A",
           arrowprops=dict(arrowstyle="->", color="#888780", lw=1.2))
d.set_title("(d) 时间系列：为什么停在 4 h", fontsize=12)
d.legend(fontsize=9, frameon=False); d.grid(alpha=0.25, axis="y", lw=0.5)
d.set_ylim(0, 62)

for axx in ax.ravel():
    for s in ["top", "right"]:
        axx.spines[s].set_visible(False)

plt.suptitle("用《三元低共熔溶剂对毛竹组分可控分离》的真实数据重画的一张图", fontsize=14, y=0.985)
plt.tight_layout(rect=[0, 0, 1, 0.965])
out = r"C:/Users/a/WorkBuddy/2026-10-13-16-58-34/我的论文数据重绘图.png"
plt.savefig(out, dpi=120, facecolor="white")
print("图已保存:", out)
