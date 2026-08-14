# OB-37 独立审稿裁决：\(q_j(T)\) 渐近式中的奇偶性

**送审件：** `OB-37-A-qj-parity.md`  
**审稿标准：** `REVIEW_PROMPT(3).md`（通用送审头 + Gate-A）  
**审稿日期：** 2026-08-14  
**审稿方式：** 不预设作者结论；一般系数独立推导；两个数值锚点以 Python 标准库 `fractions.Fraction` 作无浮点精确复算。

## 1. 最终裁决

- **数学主张：CONFIRMED。** 对每个固定整数 \(j\ge 1\) 及每个固定实数 \(\sigma_0\in(0,1)\)，
  \[
  q_j(T)=\frac{4j^2}{T^2}+O_{j,\sigma_0}(T^{-4})\qquad(T\to+\infty).
  \]
  \(T^{-3}\) 项确实恒等消失；\(\operatorname{Re}g(T)\) 的 \(T^{-2}\) 系数确为 \(j^2\)。事实上证明同样覆盖 \(\sigma_0=\tfrac12\)，只要按原定义把 \(Q\) 视为计重数的四元多重集。
- **非循环性：CONFIRMED。** 证明只用显式复数、实系数多项式、共轭、二项式定理及有理函数在无穷远处的 Laurent 展开；未使用 RH、RH 等价命题、\(\zeta\) 零点、函数方程、Euler 乘积或零点计数。
- **Gate-A：GATE-A CONDITIONAL。** 证明链无数学缺口，但送审文本尚不能原样标记为 `INDEPENDENTLY-CHECKED`：第二锚点的十进制近似错误，验收标准有一句把“\(g\) 的纯虚系数”误写成“\(\operatorname{Re}g\) 的纯虚系数”，并存在范围及模板文字不一致。第 7 节列出可直接执行的确切修改。完成这些文字修改后，本件可升级为 **GATE-A PASS**，无需改变证明实质。

## 2. 精确陈述、量词与定义核对

1. \(\varphi_j(\rho)=1-(1-\rho^{-1})^j\) 对 \(j\ge1\)、\(\rho\ne0\) 定义良好，且
   \[
   \varphi_j(\rho)=\sum_{k=1}^j(-1)^{k+1}\binom jk\rho^{-k}
   \]
   的系数全为实整数。
2. 当 \(\sigma_0\in(0,1)\) 时，\(\sigma_0\pm iT\) 与 \(1-\sigma_0\pm iT\) 在所有实 \(T\)（包括 \(T=0\)）均非零。送审件排除 \(T=0\) 并非错误，但对此渐近结论没有必要。
3. 当 \(\sigma_0=\tfrac12\) 时两对点重合，但作为多重集仍有四个计重数元素；所有求和及共轭配对公式不变。因此“Claim”中的 \(\sigma_0\ne\tfrac12\) 是应用背景的可选限制，不是证明所需假设。
4. 渐近式必须理解为：先固定 \(j,\sigma_0\)，再令 \(T\to+\infty\)。送审件未证明对无界的 \(j\) 一致的余项估计；通常记号也不应被理解为这种一致性。宜显式写成 \(O_{j,\sigma_0}(T^{-4})\)。
5. `Paper A, Lemma 2.9` 只出现在背景归属中，并非证明前提。附件未给出论文题名、作者、年份或版本，因此无法独立核对该内部标签是否确实对应所述命题；这不影响自包含命题的数学核验。若要把该归属也纳入审计，应补足书目信息或随件提供 Paper A。

## 3. 证明链逐环节核验

| 环节 | 独立判断 | 核验结果 |
|---|---|---|
| 实系数共轭相容性 | CONFIRMED | 逐项共轭给出 \(\varphi_j(\bar\rho)=\overline{\varphi_j(\rho)}\)。 |
| 四点求和化为 \(g\) | CONFIRMED | 四点和为 \(g(T)+\overline{g(T)}=2\operatorname{Re}g(T)\)；再乘 `Li` 定义中的 2，故 \(q_j=4\operatorname{Re}g\)。因子 4 正确。 |
| Step 1：\(g(-T)=\overline{g(T)}\) | CONFIRMED | 对两个实部参数 \(\sigma_0\) 与 \(1-\sigma_0\) 分别应用共轭相容性即可。 |
| Step 2：Laurent 展开存在 | CONFIRMED | 把实部有理化后可取实分母 \((\sigma^2+T^2)^j\)；令 \(x=1/T\) 后在 \(x=0\) 邻域解析。 |
| Step 2：奇次项消失 | CONFIRMED | \(h(T)=\operatorname{Re}g(T)\) 为偶函数，故 \(H(x)=h(1/x)\) 的解析 Taylor 展开满足 \(H(-x)=H(x)\)，所有奇次系数为零。 |
| Step 3：\(T^{-2}\) 系数 | CONFIRMED | 单个 \(\sigma\) 的系数是 \(j\sigma+\binom j2\)；对 \(\sigma_0,1-\sigma_0\) 求和得到 \(j+2\binom j2=j^2\)。 |
| 一致性检查：\(T^{-3}\) | CONFIRMED | \(g\) 的该阶系数为纯虚数 \(i[c_3(\sigma_0,j)+c_3(1-\sigma_0,j)]\)；所以 \(\operatorname{Re}g\) 的该阶系数是 0。 |
| 组合成最终渐近式 | CONFIRMED | Laurent 解析性排除了类似 \(|T|^{-3}\) 的非解析余项；因此从 \(j^2T^{-2}\) 之后直接进入 \(O(T^{-4})\)。 |
| 数值锚点 1 | CONFIRMED | 所有精确分数与送审件一致。 |
| 数值锚点 2 | PARTIAL（仅十进制笔误） | 精确分数一致；`≈14.876` 不正确，应为 `≈14.8726869068`（或三位小数 `≈14.873`）。 |

各环节的输出恰好满足下一环节的输入：共轭相容性给出奇偶性；有理函数在无穷远的解析性使奇偶性可以作用于逐项 Laurent 系数；二项式展开给出首项；最后 `Li` 规范中的因子 2 把 \(2\operatorname{Re}g\) 变成 \(4\operatorname{Re}g\)。无缺口，也无循环。

## 4. 独立推导

令 \(x=T^{-1}\)。对任意固定实数 \(\sigma\)，在 \(x=0\) 邻域有收敛展开
\[
z_\sigma:=(\sigma+iT)^{-1}
=-ix+\sigma x^2+i\sigma^2x^3-\sigma^3x^4+O(x^5).
\]
由
\[
\varphi_j(\sigma+iT)
=jz_\sigma-\binom j2z_\sigma^2+\binom j3z_\sigma^3-\cdots
\]
得到
\[
\varphi_j(\sigma+iT)
=-ijx+\left(j\sigma+\binom j2\right)x^2
+i\left(j\sigma^2+j(j-1)\sigma+\binom j3\right)x^3
+O(x^4).
\]
这里 \(\binom j3=0\)（当 \(j<3\)）按通常约定理解。记
\[
c_3(\sigma,j)=j\sigma^2+j(j-1)\sigma+\binom j3\in\mathbb R.
\]
将 \(\sigma=\sigma_0\) 与 \(\sigma=1-\sigma_0\) 两式相加：
\[
g(T)=-\frac{2ij}{T}
+\frac{j\sigma_0+j(1-\sigma_0)+2\binom j2}{T^2}
+\frac{i[c_3(\sigma_0,j)+c_3(1-\sigma_0,j)]}{T^3}
+O(T^{-4}).
\]
而
\[
j\sigma_0+j(1-\sigma_0)+2\binom j2
=j+j(j-1)=j^2.
\]
故直接取实部已经给出
\[
\operatorname{Re}g(T)=\frac{j^2}{T^2}+O(T^{-4}).
\]

独立地，由实系数性
\[
g(-T)=\overline{g(T)},\qquad
\operatorname{Re}g(-T)=\operatorname{Re}g(T).
\]
令 \(H(x)=\operatorname{Re}g(1/x)\)。有理化后 \(H\) 在 \(x=0\) 解析，并满足 \(H(-x)=H(x)\)，因此其所有奇次 Taylor 系数均为零。这不仅消去 \(T^{-3}\) 项，也消去 \(\operatorname{Re}g\) 的每个奇次逆幂项。最后
\[
q_j(T)=4\operatorname{Re}g(T)=\frac{4j^2}{T^2}+O_{j,\sigma_0}(T^{-4}).
\]

这一推导也说明送审骨架中的关键逻辑限制：仅凭“偶函数 + 单侧 \(O(T^{-3})\)”一般不能自动提升余项；本件之所以能提升，是因为 \(H(x)\) 在 \(x=0\) 具有真正的解析幂级数。送审件已经给出了所需的有理函数依据，因此不存在该缺口，但正式证明应保留这句话。

## 5. 精确有理数复算

独立脚本把复数表示成一对 `Fraction`，从定义计算逆元、整数幂、\(\varphi_j\)、\(g\) 和 \(q_j\)，证书路径中没有浮点运算。所得结果为：

| 锚点 | \(q_j(3)\) | \(9q_j(3)\) | 与极限系数之差 |
|---|---:|---:|---:|
| \(j=1,\ \sigma_0=3/4\) | \(3136/7395\) | \(9408/2465\) | \(4-9q_1=452/2465\) |
| \(j=2,\ \sigma_0=3/4\) | \(10041088/6076225\) | \(90369792/6076225\) | \(16-9q_2=6849808/6076225\) |

第二行的精确值约为
\[
\frac{90369792}{6076225}=14.8726869067554\ldots,
\]
而不是送审件写的 \(14.876\)。其余精确分子、分母均复现。作为额外交叉检查，脚本从 \((\sigma+i/x)^{-1}\) 的定义独立构造截断幂级数，对 \(j=1,\ldots,8\) 及 \(\sigma\in\{1/7,1/2,3/4\}\) 验证了：\(g\) 的 \(x\) 系数为 \(-2ij\)，实 \(x^2\) 系数为 \(j^2\)，实 \(x^3,x^5\) 系数为 0。有限测试只是复算守卫；一般结论由第 4 节的符号推导证明。

## 6. Gate-A 问题逐项回答

1. **隐藏间隙或循环：** 未发现。奇偶性并非来自 \(\zeta\) 的函数方程，而是来自实系数多项式与复共轭。
2. **非平凡性：** 成立。\(T^{-2}\) 系数通过两个不同实部参数的非平凡抵消化为 \(j^2\)；下一允许阶一般为 \(T^{-4}\)，并非把零函数包装成渐近式。
3. **解析步骤与有限步骤的分离：** 清楚。有限代数给出前三个系数；“有理函数在 \(x=0\) 解析 + 偶性”负责排除所有奇次项。没有无限零点集合或极限交换。
4. **范围与逃逸声明：** 数学上对每个固定 \(j,\sigma_0\) 正确；文本应明确余项常数的参数依赖。\(\sigma_0=1/2\) 并不逃逸，反而也被证明覆盖。
5. **外部前提：** 无载荷性外部定理。`Paper A, Lemma 2.9` 的书目归属因附件信息不足而未核对，但它不参与推理。
6. **最终裁决：** 核心证明 **CONFIRMED**；送审文本为 **GATE-A CONDITIONAL**，条件仅是第 7 节的文字修复。

## 7. 升级为 GATE-A PASS 前的确切修改

以下 1–6 项均应执行：

1. 将 Background 中的
   > `independent verification of all three components`

   改为
   > `independent verification of all four components`。

2. 统一 \(\sigma_0\) 的范围。建议删除 Background、四点多重集定义及 Claim 中的
   > `\(\sigma_0\neq1/2\)`

   并把 Claim 首句替换为：
   > **For every fixed integer \(j\ge1\) and every fixed \(\sigma_0\in(0,1)\), as \(T\to+\infty\),**
   > \[q_j(T)=4j^2/T^2+O_{j,\sigma_0}(T^{-4}).\]

   若 Paper A 的应用必须排除中线，也可保留该限制，但须在验收标准的 accepted statement 中同步补回，并注明排除只是应用范围而非证明需要。

3. 将 Acceptance criterion 1 中
   > `the consistency check confirms the \(T^{-3}\) coefficient in \(\operatorname{Re}g\) is purely imaginary`

   替换为
   > `the consistency check confirms that the \(T^{-3}\) coefficient in \(g\) is purely imaginary, hence the \(T^{-3}\) coefficient in \(\operatorname{Re}g\) is zero`。

4. 将 Anchor 2 中
   > `\(90\,369\,792/6\,076\,225\approx14.876\)`

   改为
   > `\(90\,369\,792/6\,076\,225\approx14.8726869068\)`

   （若只保留三位小数，则写 `\(\approx14.873\)`）。精确分数无需修改。

5. 将 REFUTED 条目中的
   > `Provide the exact rational matrix`

   改为
   > `Provide the exact rational calculation (or exact rational value)`，

   因为本问题没有任何矩阵对象。

6. 将 Step 2 中“每个 \(\varphi_j(\sigma+iT)\) 的分母是 \((\sigma^2+T^2)^j\)”的句子改得精确：
   > `After rationalization, \(\varphi_j(\sigma+iT)\) and in particular its real part can be written with the real even denominator \((\sigma^2+T^2)^j\). Hence \(H(x)=\operatorname{Re}g(1/x)\) is rational and analytic near \(x=0\).`

   同时把该段的
   > `In particular \(a_1=0\) and \(a_3=0\)`

   改为
   > `If the series is indexed from \(k\ge1\), then \(a_1=0\); in the displayed series beginning at \(k=2\), the relevant conclusion is \(a_3=0\).`

建议但不作为数学通过条件：为 `Paper A, Lemma 2.9` 补充作者、题名、年份、版本及稳定定位；否则将其明确标成未经本件核验的内部背景交叉引用。

---

**裁决签署：GATE-A CONDITIONAL。** 条件仅为上述确切文字修复；核心渐近式、奇偶性论证、主系数、精确分数锚点及非循环性均已独立确认。
